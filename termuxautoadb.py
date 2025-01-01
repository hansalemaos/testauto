from collections import deque
from collections import namedtuple
from cythondfprint import add_printer
from exceptdrucker import errwrite
from functools import lru_cache
from functools import partial
from normaltext import lookup
from platform import platform
from time import sleep
import base64
import ctypes
import io
import numpy as np
import os
import pandas as pd
import random
import regex as re
import requests
import string
import subprocess
import sys
import tarfile
import tempfile
import threading
import time
import unicodedata
from typing import Literal
from winandrodumpi import parse_window_elements
import pathlib
from pprint import pprint
import struct
from math import ceil, floor

sconfig = sys.modules[__name__]
sconfig.mycfg_su = "su"
sconfig.mycfg_shell = "sh"
sconfig.mycfg_system_folder = "/system/bin/"

screenres_reg_cur = re.compile(rb"\bcur=(\d+)x(\d+)\b")
screenres_reg = re.compile(rb"\bcur=(\d+)x(\d+)\b")

re_split_quotes = re.compile(r"(['\"])")
valid_input_devices = Literal[
    "dpad",
    "keyboard",
    "mouse",
    "touchpad",
    "gamepad",
    "touchnavigation",
    "joystick",
    "touchscreen",
    "stylus",
    "trackball",
    "",
]


compiledregex = re.compile(r"^[A-Z]:\\", flags=re.I)

ADB_SHELL_SOME_SPEED_UP_CONFIG = f"""start_settings_secure() {{
    local settings="$1"

    printf "%s\n" "$settings put secure accessibility_button_mode 1" | sh
    printf "%s\n" "$settings put secure accessibility_display_daltonizer_enabled 0" | sh
    printf "%s\n" "$settings put secure accessibility_display_inversion_enabled 0" | sh
    printf "%s\n" "$settings put secure accessibility_display_magnification_enabled 0" | sh
    printf "%s\n" "$settings put secure accessibility_display_magnification_scale 2.0" | sh
    printf "%s\n" "$settings put secure accessibility_enabled 1" | sh
    printf "%s\n" "$settings put secure accessibility_magnification_capability 3" | sh
    printf "%s\n" "$settings put secure adaptive_sleep 0" | sh
    printf "%s\n" "$settings put secure assistant 0" | sh
    printf "%s\n" "$settings put secure autofill_field_classification 1" | sh
    printf "%s\n" "$settings put secure autofill_service null" | sh
    printf "%s\n" "$settings put secure automatic_storage_manager_enabled 0" | sh
    printf "%s\n" "$settings put secure aware_enabled 0" | sh
    printf "%s\n" "$settings put secure aware_lock_enabled 0" | sh
    printf "%s\n" "$settings put secure backup_enabled 0" | sh
    printf "%s\n" "$settings put secure brightness_slider_style 0" | sh
    printf "%s\n" "$settings put secure camera_double_tap_power_gesture_disabled 1" | sh
    printf "%s\n" "$settings put secure camera_privacy_indicator 0" | sh
    printf "%s\n" "$settings put secure charging_sounds_enabled 0" | sh
    printf "%s\n" "$settings put secure charging_vibration_enabled 0" | sh
    printf "%s\n" "$settings put secure clipboard_show_access_notifications 0" | sh
    printf "%s\n" "$settings put secure clock_seconds null" | sh
    printf "%s\n" "$settings put secure default_input_method com.android.inputmethod.latin/.LatinIME" | sh
    printf "%s\n" "$settings put secure device_state_rotation_lock 1" | sh
    printf "%s\n" "$settings put secure double_tap_to_wake 0" | sh
    printf "%s\n" "$settings put secure double_tap_to_wake_enabled 0" | sh
    printf "%s\n" "$settings put secure doze_pulse_on_double_tap null" | sh
    printf "%s\n" "$settings put secure doze_tap_gesture null" | sh
    printf "%s\n" "$settings put secure dropbox:data_app_anr disabled" | sh
    printf "%s\n" "$settings put secure dropbox:data_app_crash disabled" | sh
    printf "%s\n" "$settings put secure dropbox:data_app_wtf disabled" | sh
    printf "%s\n" "$settings put secure emergency_gesture_enabled 0" | sh
    printf "%s\n" "$settings put secure enabled_input_methods com.android.inputmethod.latin/.LatinIME" | sh
    printf "%s\n" "$settings put secure face_unlock_method 0" | sh
    printf "%s\n" "$settings put secure facelock_detection_threshold 0.0" | sh
    printf "%s\n" "$settings put secure facelock_liveliness_recognition_threshold 2.2" | sh
    printf "%s\n" "$settings put secure facelock_max_center_movement 10.0" | sh
    printf "%s\n" "$settings put secure feature_touch_hovering 0" | sh
    printf "%s\n" "$settings put secure fod_vibration 0" | sh
    printf "%s\n" "$settings put secure hide_qs_call_strength 1" | sh
    printf "%s\n" "$settings put secure high_priority 0" | sh
    printf "%s\n" "$settings put secure high_text_contrast_enabled 1" | sh
    printf "%s\n" "$settings put secure hush_gesture_used 0" | sh
    printf "%s\n" "$settings put secure icon_blacklist null" | sh
    printf "%s\n" "$settings put secure immersive_mode_confirmations " | sh
    printf "%s\n" "$settings put secure install_non_market_apps 1" | sh
    printf "%s\n" "$settings put secure keyguard_slice_uri null" | sh
    printf "%s\n" "$settings put secure known_trust_agents_initialized 1" | sh
    printf "%s\n" "$settings put secure last_setup_shown eclair_1" | sh
    printf "%s\n" "$settings put secure launcher_taskbar_education_showing 0" | sh
    printf "%s\n" "$settings put secure location_mode 0" | sh
    printf "%s\n" "$settings put secure location_privacy_indicator 0" | sh
    printf "%s\n" "$settings put secure location_providers_allowed -gps" | sh
    printf "%s\n" "$settings put secure lock_screen_allow_private_notifications 0" | sh
    printf "%s\n" "$settings put secure lock_screen_owner_info_enabled 0" | sh
    printf "%s\n" "$settings put secure lock_screen_show_notifications 0" | sh
    printf "%s\n" "$settings put secure lock_screen_show_only_unseen_notifications 0" | sh
    printf "%s\n" "$settings put secure lock_screen_show_qr_code_scanner 0" | sh
    printf "%s\n" "$settings put secure lockscreen.disabled 0" | sh
    printf "%s\n" "$settings put secure lockscreen_media_metadata 0" | sh
    printf "%s\n" "$settings put secure lockscreen_show_controls 0" | sh
    printf "%s\n" "$settings put secure lockscreen_show_wallet 0" | sh
    printf "%s\n" "$settings put secure long_press_timeout 400" | sh
    printf "%s\n" "$settings put secure low_power_warning_acknowledged 0" | sh
    printf "%s\n" "$settings put secure manual_ringer_toggle_count 0" | sh
    printf "%s\n" "$settings put secure masterLocationPackagePrefixBlacklist com.google.,com.semaphoremobile.zagat.android" | sh
    printf "%s\n" "$settings put secure masterLocationPackagePrefixWhitelist com.google.android.gms" | sh
    printf "%s\n" "$settings put secure media_controls_lock_screen 0" | sh
    printf "%s\n" "$settings put secure mock_location 0" | sh
    printf "%s\n" "$settings put secure mount_play_not_snd 1" | sh
    printf "%s\n" "$settings put secure mount_ums_autostart 0" | sh
    printf "%s\n" "$settings put secure mount_ums_notify_enabled 0" | sh
    printf "%s\n" "$settings put secure mount_ums_prompt 0" | sh
    printf "%s\n" "$settings put secure multi_press_timeout 300" | sh
    printf "%s\n" "$settings put secure nas_settings_updated 1" | sh
    printf "%s\n" "$settings put secure navigation_bar_hint null" | sh
    printf "%s\n" "$settings put secure navigation_mode 2" | sh
    printf "%s\n" "$settings put secure notification_badging 0" | sh
    printf "%s\n" "$settings put secure notification_bubbles 0" | sh
    printf "%s\n" "$settings put secure notification_history_enabled null" | sh
    printf "%s\n" "$settings put secure one_handed_mode_activated 0" | sh
    printf "%s\n" "$settings put secure one_handed_mode_enabled 0" | sh
    printf "%s\n" "$settings put secure package_verifier_state 1" | sh
    printf "%s\n" "$settings put secure pai_selection_page_complete 1" | sh
    printf "%s\n" "$settings put secure permission_revocation_first_enabled_timestamp_ms 0" | sh
    printf "%s\n" "$settings put secure power_menu_locked_show_content 0" | sh
    printf "%s\n" "$settings put secure projection_privacy_indicator 1" | sh
    printf "%s\n" "$settings put secure qs_auto_brightness 0" | sh
    printf "%s\n" "$settings put secure qs_brightness_slider 0" | sh
    printf "%s\n" "$settings put secure qs_brightness_slider_position 0" | sh
    printf "%s\n" "$settings put secure qs_show_data_usage 0" | sh
    printf "%s\n" "$settings put secure quick_settings_vibrate 0" | sh
    printf "%s\n" "$settings put secure screen_off_udfps_enabled 0" | sh
    printf "%s\n" "$settings put secure screensaver_activate_on_dock 0" | sh
    printf "%s\n" "$settings put secure screensaver_activate_on_sleep 0" | sh
    printf "%s\n" "$settings put secure screensaver_enabled 0" | sh
    printf "%s\n" "$settings put secure selected_input_method_subtype -1" | sh
    printf "%s\n" "$settings put secure selected_spell_checker null" | sh
    printf "%s\n" "$settings put secure selected_spell_checker_subtype 0" | sh
    printf "%s\n" "$settings put secure send_action_app_error 1" | sh
    printf "%s\n" "$settings put secure show_clipboard_overlay 0" | sh
    printf "%s\n" "$settings put secure show_ime_with_hard_keyboard 0" | sh
    printf "%s\n" "$settings put secure show_wifi_standard_icon 0" | sh
    printf "%s\n" "$settings put secure show_zen_settings_suggestion 0" | sh
    printf "%s\n" "$settings put secure silence_gesture 0" | sh
    printf "%s\n" "$settings put secure skip_gesture 0" | sh
    printf "%s\n" "$settings put secure sleep_timeout 86400000" | sh
    printf "%s\n" "$settings put secure snoozed_schedule_condition_provider " | sh
    printf "%s\n" "$settings put secure speak_password 0" | sh
    printf "%s\n" "$settings put secure spell_checker_enabled 0" | sh
    printf "%s\n" "$settings put secure swipe_bottom_to_notification_enabled 0" | sh
    printf "%s\n" "$settings put secure sync_parent_sounds 0" | sh
    printf "%s\n" "$settings put secure system_black_theme 0" | sh
    printf "%s\n" "$settings put secure sysui_do_not_disturb 0" | sh
    printf "%s\n" "$settings put secure sysui_nav_bar_inverse null" | sh
    printf "%s\n" "$settings put secure sysui_qs_tiles internet,saver" | sh
    printf "%s\n" "$settings put secure sysui_rounded_size null" | sh
    printf "%s\n" "$settings put secure sysui_tuner_version 4" | sh
    printf "%s\n" "$settings put secure sysui_volume_down_silent null" | sh
    printf "%s\n" "$settings put secure sysui_volume_up_silent null" | sh
    printf "%s\n" "$settings put secure touch_exploration_enabled 0" | sh
    printf "%s\n" "$settings put secure trust_agents_initialized 1" | sh
    printf "%s\n" "$settings put secure unknown_sources_default_reversed 1" | sh
    printf "%s\n" "$settings put secure usb_migration_expected_version 1" | sh
    printf "%s\n" "$settings put secure usb_migration_state 0" | sh
    printf "%s\n" "$settings put secure usb_migration_state_version 1" | sh
    printf "%s\n" "$settings put secure user_setup_complete 1" | sh
    printf "%s\n" "$settings put secure user_setup_personalization_state 10" | sh
    printf "%s\n" "$settings put secure voice_interaction_service " | sh
    printf "%s\n" "$settings put secure volume_hush_gesture 0" | sh
    printf "%s\n" "$settings put secure volume_panel_on_left 0" | sh
    printf "%s\n" "$settings put secure wake_gesture_enabled 0" | sh
    printf "%s\n" "$settings put secure web_autofill_query_url null" | sh
    printf "%s\n" "$settings put secure window_ignore_secure 0" | sh
    printf "%s\n" "$settings put secure zen_duration 0" | sh
    printf "%s\n" "$settings put secure zen_settings_suggestion_viewed 0" | sh
    printf "%s\n" "$settings put secure zen_settings_updated 1" | sh
    printf "%s\n" "$settings put secure allow_heat_cooldown_schedule true" | sh
    printf "%s\n" "$settings put secure allow_heat_cooldown_always 1" | sh
    printf "%s\n" "$settings put secure heat_cooldown_schedule 30s" | sh
    printf "%s\n" "$settings put secure allow_more_heat_value 40" | sh
    printf "%s\n" "$settings put secure long_press_timeout 200" | sh
    printf "%s\n" "$settings put secure multi_press_timeout 200" | sh
    printf "%s\n" "$settings put secure accessibility_captioning_enabled 1" | sh
    printf "%s\n" "$settings put secure accessibility_captioning_font_scale 0.7" | sh
    printf "%s\n" "$settings put secure odi_captions_enabled 0" | sh
    printf "%s\n" "$settings put secure odi_captions_volume_ui_enabled 0" | sh
    printf "%s\n" "$settings put secure display_white_balance_enabled 0" | sh
    printf "%s\n" "$settings put secure night_display_activated 0" | sh
    printf "%s\n" "$settings put secure night_display_auto_mode 0" | sh
    printf "%s\n" "$settings put secure charging_sounds_enabled 0" | sh
    printf "%s\n" "$settings put secure charging_vibration_enabled 0" | sh
    printf "%s\n" "$settings put secure adaptive_sleep 0" | sh
    printf "%s\n" "$settings put secure aware_enabled 0" | sh
    printf "%s\n" "$settings put secure aware_lock_enabled 0" | sh
    printf "%s\n" "$settings put secure double_tap_to_wake 0" | sh
    printf "%s\n" "$settings put secure emergency_gesture_enabled 0" | sh
    printf "%s\n" "$settings put secure hush_gesture_used 0" | sh
    printf "%s\n" "$settings put secure silence_gesture 0" | sh
    printf "%s\n" "$settings put secure skip_gesture 0" | sh
    printf "%s\n" "$settings put secure volume_hush_gesture 0" | sh
    printf "%s\n" "$settings put secure wake_gesture_enabled 0" | sh
    printf "%s\n" "$settings put secure assistant 0" | sh
    printf "%s\n" "$settings put secure smartspace 0" | sh
    printf "%s\n" "$settings put secure brightness_on_top 1" | sh
    printf "%s\n" "$settings put secure fmm_community_finding 0" | sh
    printf "%s\n" "$settings put secure fmm_unlock_recovery 0" | sh
    printf "%s\n" "$settings put secure friends_plugin_connected 0" | sh
    printf "%s\n" "$settings put secure game_home_enable 0" | sh
    printf "%s\n" "$settings put secure ltw_clipboard_sync_state 0" | sh
    printf "%s\n" "$settings put secure mcf_continuity_nearby_device_state 0" | sh
    printf "%s\n" "$settings put secure multi_control_connection_state 0" | sh
    printf "%s\n" "$settings put secure samsungflow_clipboard_sync_state 0" | sh
    printf "%s\n" "$settings put secure screen_extra_brightness 1" | sh
    printf "%s\n" "$settings put secure settings_secure_routine_enabled 0" | sh
    printf "%s\n" "$settings put secure sm_connectivity_disable 0" | sh
    printf "%s\n" "$settings put secure wifi_ap_powersave_mode_checked 1" | sh
    printf "%s\n" "$settings put secure wifi_ap_wifi_sharing 0" | sh
    printf "%s\n" "$settings put secure screensaver_enabled 0" | sh
    printf "%s\n" "$settings put secure screensaver_activate_on_sleep 0" | sh
    printf "%s\n" "$settings put secure screensaver_activate_on_dock 0" | sh
    printf "%s\n" "$settings put secure backup_enabled 1" | sh
    printf "%s\n" "$settings put secure clipboard_show_access_notifications 0" | sh
    printf "%s\n" "$settings put secure notification_badging 0" | sh
    printf "%s\n" "$settings put secure notification_bubbles 0" | sh
    printf "%s\n" "$settings put secure show_notification_snooze 0" | sh
    printf "%s\n" "$settings put secure spell_checker_enabled 0" | sh
    printf "%s\n" "$settings put secure tap_duration_threshold 0" | sh
    printf "%s\n" "$settings put secure touch_blocking_period 0" | sh
    printf "%s\n" "$settings put secure package_verifier_state 0" | sh
    printf "%s\n" "$settings put secure kv_backup_agent_timeout_millis=1,full_backup_agent_timeout_millis=1" | sh
    printf "%s\n" "$settings put secure screensaver_activate_on_dock 0" | sh

}}

start_global_settings() {{
    local settings="$1"
    printf "%s\n" "$settings put global BATTERY_DISCHARGE_INFO null" | sh
    printf "%s\n" "$settings put global activity_starts_logging_enabled 0" | sh
    printf "%s\n" "$settings put global adaptive_battery_management_enabled 0" | sh
    printf "%s\n" "$settings put global adb_enabled 1" | sh
    printf "%s\n" "$settings put global adb_wifi_enabled 0" | sh
    printf "%s\n" "$settings put global add_users_when_locked 0" | sh
    printf "%s\n" "$settings put global airplane_mode_on 0" | sh
    printf "%s\n" "$settings put global airplane_mode_radios cell,bluetooth,wifi,nfc,wimax" | sh
    printf "%s\n" "$settings put global airplane_mode_toggleable_radios bluetooth,wifi,nfc" | sh
    printf "%s\n" "$settings put global alarm_manager_dummy_flags null" | sh
    printf "%s\n" "$settings put global always_finish_activities 1" | sh
    printf "%s\n" "$settings put global always_on_display_constants null" | sh
    printf "%s\n" "$settings put global ambient_enabled 0" | sh
    printf "%s\n" "$settings put global ambient_force_when_docked 0" | sh
    printf "%s\n" "$settings put global ambient_low_bit_enabled 0" | sh
    printf "%s\n" "$settings put global ambient_low_bit_enabled_dev 0" | sh
    printf "%s\n" "$settings put global ambient_plugged_timeout_min -1" | sh
    printf "%s\n" "$settings put global ambient_tilt_to_bright 0" | sh
    printf "%s\n" "$settings put global ambient_tilt_to_wake 1" | sh
    printf "%s\n" "$settings put global ambient_touch_to_wake 0" | sh
    printf "%s\n" "$settings put global analytics_enabled 0" | sh
    printf "%s\n" "$settings put global android_wear_system_edition 1" | sh
    printf "%s\n" "$settings put global android_wear_version 2" | sh
    printf "%s\n" "$settings put global animator_duration_scale 0" | sh
    printf "%s\n" "$settings put global anomaly_config_version 11" | sh
    printf "%s\n" "$settings put global anomaly_detection_constants null" | sh
    printf "%s\n" "$settings put global apm_enhancement_enabled 0" | sh
    printf "%s\n" "$settings put global app_auto_restriction_enabled 0" | sh
    printf "%s\n" "$settings put global app_standby_enabled 0" | sh
    printf "%s\n" "$settings put global assisted_gps_enabled 0" | sh
    printf "%s\n" "$settings put global audio_safe_volume_state 0" | sh
    printf "%s\n" "$settings put global auto_sync 0" | sh
    printf "%s\n" "$settings put global auto_time 1" | sh
    printf "%s\n" "$settings put global auto_time_zone 1" | sh
    printf "%s\n" "$settings put global auto_wifi 1" | sh
    printf "%s\n" "$settings put global hide_secure_folder_flag 1" | sh
    printf "%s\n" "$settings put global backup_enabled 0" | sh
    printf "%s\n" "$settings put global battery_saver_enabled false" | sh
    printf "%s\n" "$settings put global battery_stats_constants track_cpu_times_by_proc_state false" | sh
    printf "%s\n" "$settings put global battery_tip_constants app_restriction_enabled false" | sh
    printf "%s\n" "$settings put global batterystats null" | sh
    printf "%s\n" "$settings put global ble_scan_always_enabled 0" | sh
    printf "%s\n" "$settings put global ble_scan_balanced_interval_ms 730" | sh
    printf "%s\n" "$settings put global ble_scan_balanced_window_ms 183" | sh
    printf "%s\n" "$settings put global ble_scan_low_power_interval_ms 1400" | sh
    printf "%s\n" "$settings put global ble_scan_low_power_window_ms 140" | sh
    printf "%s\n" "$settings put global blocking_helper_dismiss_to_view_ratio null" | sh
    printf "%s\n" "$settings put global blocking_helper_streak_limit null" | sh
    printf "%s\n" "$settings put global bluetooth_disabled_profiles 0" | sh
    printf "%s\n" "$settings put global bluetooth_on 0" | sh
    printf "%s\n" "$settings put global bt_default_apm_state 0" | sh
    printf "%s\n" "$settings put global bug_report 0" | sh
    printf "%s\n" "$settings put global burn_in_protection 0" | sh
    printf "%s\n" "$settings put global button_set 0" | sh
    printf "%s\n" "$settings put global call_auto_retry 0" | sh
    printf "%s\n" "$settings put global cdma_cell_broadcast_sms 1" | sh
    printf "%s\n" "$settings put global cell_on 1" | sh
    printf "%s\n" "$settings put global clockwork_24hr_time 0" | sh
    printf "%s\n" "$settings put global clockwork_auto_time 1" | sh
    printf "%s\n" "$settings put global clockwork_auto_time_zone 1" | sh
    printf "%s\n" "$settings put global content_capture_service_explicitly_enabled default" | sh
    printf "%s\n" "$settings put global corner_roundness 0" | sh
    printf "%s\n" "$settings put global current_watchface_decomposable 0" | sh
    printf "%s\n" "$settings put global data_roaming 1" | sh
    printf "%s\n" "$settings put global debug_app null" | sh
    printf "%s\n" "$settings put global default_install_location 0" | sh
    printf "%s\n" "$settings put global default_restrict_background_data 0" | sh
    printf "%s\n" "$settings put global development_settings_enabled 1" | sh
    printf "%s\n" "$settings put global device_provisioned 1" | sh
    printf "%s\n" "$settings put global diskstats null" | sh
    printf "%s\n" "$settings put global dock_audio_media_enabled 0" | sh
    printf "%s\n" "$settings put global dock_sounds_enabled 0" | sh
    printf "%s\n" "$settings put global dock_sounds_enabled_when_accessbility 0" | sh
    printf "%s\n" "$settings put global dropbox:BATTERY_DISCHARGE_INFO disabled" | sh
    printf "%s\n" "$settings put global dropbox:SYSTEM_AUDIT enabled" | sh
    printf "%s\n" "$settings put global dropbox:SYSTEM_BOOT enabled" | sh
    printf "%s\n" "$settings put global dropbox:SYSTEM_FSCK enabled" | sh
    printf "%s\n" "$settings put global dropbox:SYSTEM_RESTART enabled" | sh
    printf "%s\n" "$settings put global dropbox:_STR_HASH enabled" | sh
    printf "%s\n" "$settings put global dropbox:dumpsys:account enabled" | sh
    printf "%s\n" "$settings put global dropbox:dumpsys:batterystats disabled" | sh
    printf "%s\n" "$settings put global dropbox:dumpsys:diskstats disabled" | sh
    printf "%s\n" "$settings put global dropbox:dumpsys:package enabled" | sh
    printf "%s\n" "$settings put global dropbox:dumpsys:procstats disabled" | sh
    printf "%s\n" "$settings put global dropbox:dumpsys:usagestats disabled" | sh
    printf "%s\n" "$settings put global dropbox:dumpsys:user enabled" | sh
    printf "%s\n" "$settings put global dropbox:event_data disabled" | sh
    printf "%s\n" "$settings put global dropbox:event_log disabled" | sh
    printf "%s\n" "$settings put global dropbox:netstats_error disabled" | sh
    printf "%s\n" "$settings put global dropbox:storage_trim enabled" | sh
    printf "%s\n" "$settings put global dropbox:system_server_lowmem enabled" | sh
    printf "%s\n" "$settings put global dropbox_reserve_percent 0" | sh
    printf "%s\n" "$settings put global emergency_call_codes_data null" | sh
    printf "%s\n" "$settings put global emergency_gesture_power_button_cooldown_period_ms 3000" | sh
    printf "%s\n" "$settings put global emergency_tone 0" | sh
    printf "%s\n" "$settings put global enable_non_resizable_multi_window 0" | sh
    printf "%s\n" "$settings put global event_data null" | sh
    printf "%s\n" "$settings put global event_log null" | sh
    printf "%s\n" "$settings put global gms_checkin_timeout_min 6" | sh
    printf "%s\n" "$settings put global has_pay_tokens 0" | sh
    printf "%s\n" "$settings put global heads_up_notifications_enabled 1" | sh
    printf "%s\n" "$settings put global high_performance 1" | sh
    printf "%s\n" "$settings put global hotword_detection_enabled 0" | sh
    printf "%s\n" "$settings put global ingress_rate_limit_bytes_per_second -1" | sh
    printf "%s\n" "$settings put global last_call_forward_action -1" | sh
    printf "%s\n" "$settings put global lid_behavior 0" | sh
    printf "%s\n" "$settings put global location_background_throttle_interval_ms 600000" | sh
    printf "%s\n" "$settings put global lock_sound /product/media/audio/ui/Lock.ogg" | sh
    printf "%s\n" "$settings put global logcat_enabled 0" | sh
    printf "%s\n" "$settings put global low_battery_sound /product/media/audio/ui/LowBattery.ogg" | sh
    printf "%s\n" "$settings put global low_battery_sound_timeout 0" | sh
    printf "%s\n" "$settings put global low_power 0" | sh
    printf "%s\n" "$settings put global low_power_sticky_auto_disable_enabled 0" | sh
    printf "%s\n" "$settings put global max_sound_trigger_detection_service_ops_per_day 0" | sh
    printf "%s\n" "$settings put global mobile_data 1" | sh
    printf "%s\n" "$settings put global mobile_data_always_on 1" | sh
    printf "%s\n" "$settings put global mobile_signal_detector 1" | sh
    printf "%s\n" "$settings put global mode_ringer 2" | sh
    printf "%s\n" "$settings put global multi_cb 0" | sh
    printf "%s\n" "$settings put global netstats_enabled 10" | sh
    printf "%s\n" "$settings put global netstats_error null" | sh
    printf "%s\n" "$settings put global network_recommendations_enabled 0" | sh
    printf "%s\n" "$settings put global network_scoring_ui_enabled 0" | sh
    printf "%s\n" "$settings put global network_watchlist_enabled " | sh
    printf "%s\n" "$settings put global night_display_forced_auto_mode_available 0" | sh
    printf "%s\n" "$settings put global non_persistent_mac_randomization_force_enabled 1" | sh
    printf "%s\n" "$settings put global notification_snooze_options null" | sh
    printf "%s\n" "$settings put global obtain_mute_when_off_body 1" | sh
    printf "%s\n" "$settings put global obtain_paired_device_location 0" | sh
    printf "%s\n" "$settings put global paired_device_os_type 0" | sh
    printf "%s\n" "$settings put global phenotype_test_setting V15AboveDefault" | sh
    printf "%s\n" "$settings put global phone_play_store_availability 1" | sh
    printf "%s\n" "$settings put global power_sounds_enabled 1" | sh
    printf "%s\n" "$settings put global preferred_network_mode 0" | sh
    printf "%s\n" "$settings put global restrict_background_data 1" | sh
    printf "%s\n" "$settings put global restricted_networking_mode 0" | sh
    printf "%s\n" "$settings put global retail_mode 0" | sh
    printf "%s\n" "$settings put global send_action_app_error 1" | sh
    printf "%s\n" "$settings put global set_install_location 0" | sh
    printf "%s\n" "$settings put global settings_use_external_provider_api 1" | sh
    printf "%s\n" "$settings put global settings_use_psd_api 1" | sh
    printf "%s\n" "$settings put global setup_skipped 0" | sh
    printf "%s\n" "$settings put global side_button 1" | sh
    printf "%s\n" "$settings put global smart_illuminate_enabled 1" | sh
    printf "%s\n" "$settings put global smart_replies_enabled 0" | sh
    printf "%s\n" "$settings put global smart_replies_in_notifications_flags enabled true,max_squeeze_remeasure_attempts 3,requires_targeting_p true" | sh
    printf "%s\n" "$settings put global sound_trigger_detection_service_op_timeout 15000" | sh
    printf "%s\n" "$settings put global stay_on_while_plugged_in 15" | sh
    printf "%s\n" "$settings put global storage_trim null" | sh
    printf "%s\n" "$settings put global subscription_mode 0" | sh
    printf "%s\n" "$settings put global system_capabilities 115" | sh
    printf "%s\n" "$settings put global system_server_lowmem null" | sh
    printf "%s\n" "$settings put global sysui_demo_allowed 0" | sh
    printf "%s\n" "$settings put global sysui_tuner_demo_on 0" | sh
    printf "%s\n" "$settings put global text_classifier_constants null" | sh
    printf "%s\n" "$settings put global theater_mode_on 0" | sh
    printf "%s\n" "$settings put global transition_animation_scale 0" | sh
    printf "%s\n" "$settings put global upload_apk_enable 1" | sh
    printf "%s\n" "$settings put global usagestats null" | sh
    printf "%s\n" "$settings put global usb_mass_storage_enabled 1" | sh
    printf "%s\n" "$settings put global user null" | sh
    printf "%s\n" "$settings put global user_disabled_hdr_formats " | sh
    printf "%s\n" "$settings put global user_hfp_client_setting 0" | sh
    printf "%s\n" "$settings put global verifier_timeout 17000" | sh
    printf "%s\n" "$settings put global wait_for_debugger 0" | sh
    printf "%s\n" "$settings put global wear_companion_os_version -1" | sh
    printf "%s\n" "$settings put global wear_os_version_string " | sh
    printf "%s\n" "$settings put global wear_platform_mr_number 0" | sh
    printf "%s\n" "$settings put global wifi_display_on 0" | sh
    printf "%s\n" "$settings put global wifi_max_dhcp_retry_count 109" | sh
    printf "%s\n" "$settings put global wifi_migration_completed 1" | sh
    printf "%s\n" "$settings put global wifi_networks_available_notification_on 1" | sh
    printf "%s\n" "$settings put global wifi_on 1" | sh
    printf "%s\n" "$settings put global wifi_power_save 120" | sh
    printf "%s\n" "$settings put global wifi_scan_always_enabled 1" | sh
    printf "%s\n" "$settings put global wifi_sleep_policy 2" | sh
    printf "%s\n" "$settings put global wifi_wakeup_enabled 1" | sh
    printf "%s\n" "$settings put global window_animation_scale 0" | sh
    printf "%s\n" "$settings put global zen_duration null" | sh
    printf "%s\n" "$settings put global zen_mode 1" | sh
    printf "%s\n" "$settings put global zen_mode_ringer_level 2" | sh
    printf "%s\n" "$settings put global zram_enabled 1" | sh
    printf "%s\n" "$settings put global adaptive_battery_management_enabled 0" | sh
    printf "%s\n" "$settings put global cached_apps_freezer enabled" | sh
    printf "%s\n" "$settings put global dock_audio_media_enabled 0" | sh
    printf "%s\n" "$settings put global dock_sounds_enabled 0" | sh
    printf "%s\n" "$settings put global emergency_tone 0" | sh
    printf "%s\n" "$settings put global power_sounds_enabled 0" | sh
    printf "%s\n" "$settings put global aware_allowed 0" | sh
    printf "%s\n" "$settings put global google_core_control 0" | sh
    printf "%s\n" "$settings put global hotword_detection_enabled 0" | sh
    printf "%s\n" "$settings put global ble_scan_always_enabled 0" | sh
    printf "%s\n" "$settings put global network_recommendations_enabled 0" | sh
    printf "%s\n" "$settings put global network_scoring_ui_enabled 0" | sh
    printf "%s\n" "$settings put global sem_wifi_network_rating_scorer_enabled 0" | sh
    printf "%s\n" "$settings put global sem_wifi_switch_to_better_wifi_enabled 0" | sh
    printf "%s\n" "$settings put global sem_wifi_switch_to_better_wifi_supported 0" | sh
    printf "%s\n" "$settings put global swipe_to_call_message 0" | sh
    printf "%s\n" "$settings put global wifi_networks_available_notification_on 0" | sh
    printf "%s\n" "$settings put global wifi_scan_always_enabled 1" | sh
    printf "%s\n" "$settings put global edge_enable 0" | sh
    printf "%s\n" "$settings put global multisound_state 0" | sh
    printf "%s\n" "$settings put global online_manual_url 0" | sh
    printf "%s\n" "$settings put global assisted_gps_enabled 1" | sh
    printf "%s\n" "$settings put global auto_wifi 1" | sh
    printf "%s\n" "$settings put global bug_report 0" | sh
    printf "%s\n" "$settings put global debug_app 0" | sh
    printf "%s\n" "$settings put global package_verifier_user_consent 0" | sh
    printf "%s\n" "$settings put global retail_mode 0" | sh
    printf "%s\n" "$settings put global uwb_enabled 0" | sh
    printf "%s\n" "$settings put global wait_for_debugger 0" | sh
    printf "%s\n" "$settings put global sound_detector 0" | sh
}}

start_system_settings() {{
    local settings="$1"
    printf "%s\n" "$settings put system accelerometer_rotation 0" | sh
    printf "%s\n" "$settings put system alarm_alert_set 0" | sh
    printf "%s\n" "$settings put system alert_window_bypass_low_ram 0" | sh
    printf "%s\n" "$settings put system anim_tile_duration 0" | sh
    printf "%s\n" "$settings put system anim_tile_interpolator 0" | sh
    printf "%s\n" "$settings put system anim_tile_style 0" | sh
    printf "%s\n" "$settings put system apply_ramping_ringer 0" | sh
    printf "%s\n" "$settings put system data_disabled_icon 1" | sh
    printf "%s\n" "$settings put system dim_screen 0" | sh
    printf "%s\n" "$settings put system double_tap_sleep_gesture 0" | sh
    printf "%s\n" "$settings put system double_tap_sleep_lockscreen 0" | sh
    printf "%s\n" "$settings put system double_tap_to_wake 0" | sh
    printf "%s\n" "$settings put system double_tap_to_wake_enabled 0" | sh
    printf "%s\n" "$settings put system dtmf_tone 0" | sh
    printf "%s\n" "$settings put system dtmf_tone_type 0" | sh
    printf "%s\n" "$settings put system dummy_show_battery_percent 0" | sh
    printf "%s\n" "$settings put system enable_ripple_effect 0" | sh
    printf "%s\n" "$settings put system end_button_behavior 2" | sh
    printf "%s\n" "$settings put system flashlight_on_call 0" | sh
    printf "%s\n" "$settings put system flashlight_on_call_ignore_dnd 0" | sh
    printf "%s\n" "$settings put system fod_vibration 0" | sh
    printf "%s\n" "$settings put system font_scale 1" | sh
    printf "%s\n" "$settings put system force_mouse_as_touch 0" | sh
    printf "%s\n" "$settings put system gearhead:driving_mode_settings_enabled 0" | sh
    printf "%s\n" "$settings put system haptic_feedback_enabled 0" | sh
    printf "%s\n" "$settings put system hearing_aid 0" | sh
    printf "%s\n" "$settings put system hide_rotation_lock_toggle_for_accessibility 1" | sh
    printf "%s\n" "$settings put system high_touch_polling_rate_enable 0" | sh
    printf "%s\n" "$settings put system high_touch_sensitivity_enable 0" | sh
    printf "%s\n" "$settings put system increasing_ring 0" | sh
    printf "%s\n" "$settings put system less_boring_heads_up 0" | sh
    printf "%s\n" "$settings put system lockscreen_battery_info 0" | sh
    printf "%s\n" "$settings put system lockscreen_charge_temp_unit 0" | sh
    printf "%s\n" "$settings put system lockscreen_sounds_enabled 0" | sh
    printf "%s\n" "$settings put system lockscreen_weather_enabled 0" | sh
    printf "%s\n" "$settings put system lockscreen_weather_style 0" | sh
    printf "%s\n" "$settings put system master_mono 1" | sh
    printf "%s\n" "$settings put system mode_ringer_streams_affected 422" | sh
    printf "%s\n" "$settings put system multi_audio_focus_enabled 0" | sh
    printf "%s\n" "$settings put system mute_streams_affected 111" | sh
    printf "%s\n" "$settings put system network_traffic_autohide_threshold 0" | sh
    printf "%s\n" "$settings put system network_traffic_state 0" | sh
    printf "%s\n" "$settings put system notification_light_pulse 1" | sh
    printf "%s\n" "$settings put system notification_sound_set 1" | sh
    printf "%s\n" "$settings put system pointer_location 0" | sh
    printf "%s\n" "$settings put system pointer_speed 0" | sh
    printf "%s\n" "$settings put system power_menu_animations 0" | sh
    printf "%s\n" "$settings put system powermenu_advanced 0" | sh
    printf "%s\n" "$settings put system powermenu_emergency 0" | sh
    printf "%s\n" "$settings put system powermenu_lockdown 0" | sh
    printf "%s\n" "$settings put system powermenu_logout 0" | sh
    printf "%s\n" "$settings put system powermenu_onthego 0" | sh
    printf "%s\n" "$settings put system powermenu_power 1" | sh
    printf "%s\n" "$settings put system powermenu_restart 0" | sh
    printf "%s\n" "$settings put system powermenu_screenshot 0" | sh
    printf "%s\n" "$settings put system powermenu_settings 0" | sh
    printf "%s\n" "$settings put system powermenu_sleep 0" | sh
    printf "%s\n" "$settings put system powermenu_users 0" | sh
    printf "%s\n" "$settings put system prevent_pointer_acceleration 1" | sh
    printf "%s\n" "$settings put system proximity_on_wake 0" | sh
    printf "%s\n" "$settings put system qs_transparency 0" | sh
    printf "%s\n" "$settings put system reticker_colored 0" | sh
    printf "%s\n" "$settings put system reticker_landscape_only 0" | sh
    printf "%s\n" "$settings put system reticker_status 0" | sh
    printf "%s\n" "$settings put system ringtone_set 1" | sh
    printf "%s\n" "$settings put system screen_brightness 100" | sh
    printf "%s\n" "$settings put system screen_brightness_for_vr 86" | sh
    printf "%s\n" "$settings put system screen_brightness_mode 0" | sh
    printf "%s\n" "$settings put system screen_off_animation 0" | sh
    printf "%s\n" "$settings put system screen_off_timeout 600000000" | sh
    printf "%s\n" "$settings put system show_app_volume 0" | sh
    printf "%s\n" "$settings put system show_fourg_icon 0" | sh
    printf "%s\n" "$settings put system show_touches 0" | sh
    printf "%s\n" "$settings put system sound_effects_enabled 0" | sh
    printf "%s\n" "$settings put system status_bar_battery_style 5" | sh
    printf "%s\n" "$settings put system status_bar_battery_text_charging 0" | sh
    printf "%s\n" "$settings put system status_bar_show_battery_percent 0" | sh
    printf "%s\n" "$settings put system statusbar_battery_bar null" | sh
    printf "%s\n" "$settings put system statusbar_battery_bar_style null" | sh
    printf "%s\n" "$settings put system statusbar_battery_bar_thickness null" | sh
    printf "%s\n" "$settings put system statusbar_colored_icons 0" | sh
    printf "%s\n" "$settings put system system_locales pt-BR" | sh
    printf "%s\n" "$settings put system toast_icon 0" | sh
    printf "%s\n" "$settings put system transistent_task_mode 0" | sh
    printf "%s\n" "$settings put system transparent_power_dialog_dim 0" | sh
    printf "%s\n" "$settings put system tty_mode 0" | sh
    printf "%s\n" "$settings put system use_old_mobiletype 0" | sh
    printf "%s\n" "$settings put system user_rotation 0" | sh
    printf "%s\n" "$settings put system vibrate_on_callwaiting 0" | sh
    printf "%s\n" "$settings put system vibrate_on_connect 0" | sh
    printf "%s\n" "$settings put system vibrate_on_disconnect 0" | sh
    printf "%s\n" "$settings put system vibrate_when_ringing 0" | sh
    printf "%s\n" "$settings put system volume_alarm 0" | sh
    printf "%s\n" "$settings put system volume_bluetooth_sco 0" | sh
    printf "%s\n" "$settings put system volume_button_music_control 1" | sh
    printf "%s\n" "$settings put system volume_key_cursor_control 1" | sh
    printf "%s\n" "$settings put system volume_media_output_toggle null" | sh
    printf "%s\n" "$settings put system volume_music 15" | sh
    printf "%s\n" "$settings put system volume_music_0x0 15" | sh
    printf "%s\n" "$settings put system volume_notification 0" | sh
    printf "%s\n" "$settings put system volume_ring 0" | sh
    printf "%s\n" "$settings put system volume_ring_0x0 0" | sh
    printf "%s\n" "$settings put system volume_rocker_wake 0" | sh
    printf "%s\n" "$settings put system volume_system 7" | sh
    printf "%s\n" "$settings put system volume_voice 0" | sh
    printf "%s\n" "$settings put system volume_voice_0x0 0" | sh
    printf "%s\n" "$settings put system blue_light_filter 0" | sh
    printf "%s\n" "$settings put system blue_light_filter_adaptive_mode 0" | sh
    printf "%s\n" "$settings put system blue_light_filter_scheduled 0" | sh
    printf "%s\n" "$settings put system screen_mode_automatic_setting 0" | sh
    printf "%s\n" "$settings put system screen_off_pocket 0" | sh
    printf "%s\n" "$settings put system camera_feedback_vibrate 0" | sh
    printf "%s\n" "$settings put system dialing_keypad_vibrate 0" | sh
    printf "%s\n" "$settings put system dtmf_tone 0" | sh
    printf "%s\n" "$settings put system haptic_feedback_enabled 0" | sh
    printf "%s\n" "$settings put system lockscreen_sounds_enabled 0" | sh
    printf "%s\n" "$settings put system navigation_gestures_vibrate 0" | sh
    printf "%s\n" "$settings put system SEM_VIBRATION_FORCE_TOUCH_INTENSITY 0" | sh
    printf "%s\n" "$settings put system SEM_VIBRATION_NOTIFICATION_INTENSITY 0" | sh
    printf "%s\n" "$settings put system SEM_VIBRATION_RING_INTENSITY 0" | sh
    printf "%s\n" "$settings put system sound_effects_enabled 0" | sh
    printf "%s\n" "$settings put system sync_vibration_with_notification 0" | sh
    printf "%s\n" "$settings put system sync_vibration_with_ringtone 0" | sh
    printf "%s\n" "$settings put system vibrate_when_ringing 0" | sh
    printf "%s\n" "$settings put system vibration_sound_enabled 0" | sh
    printf "%s\n" "$settings put system VIB_FEEDBACK_MAGNITUDE 0" | sh
    printf "%s\n" "$settings put system VIB_RECVCALL_MAGNITUDE 0" | sh
    printf "%s\n" "$settings put system double_tap_to_sleep 0" | sh
    printf "%s\n" "$settings put system mcf_continuity 0" | sh
    printf "%s\n" "$settings put system master_motion 0" | sh
    printf "%s\n" "$settings put system motion_engine 0" | sh
    printf "%s\n" "$settings put system motion_pick_up 0" | sh
    printf "%s\n" "$settings put system surface_palm_swipe 0" | sh
    printf "%s\n" "$settings put system surface_palm_touch 0" | sh
    printf "%s\n" "$settings put system air_motion_engine 0" | sh
    printf "%s\n" "$settings put system air_motion_wake_up 0" | sh
    printf "%s\n" "$settings put system add_info_alarm 0" | sh
    printf "%s\n" "$settings put system add_info_today_schedule 0" | sh
    printf "%s\n" "$settings put system add_info_music_control 0" | sh
    printf "%s\n" "$settings put system facewidget_music_transparency 0" | sh
    printf "%s\n" "$settings put system lock_editor_support_touch_hold 0" | sh
    printf "%s\n" "$settings put system lock_noticard_opacity 0" | sh
    printf "%s\n" "$settings put system screen_transition_effect 0" | sh
    printf "%s\n" "$settings put system cocktail_bar_enabled_cocktails 0" | sh
    printf "%s\n" "$settings put system device_visibility_enabled 0" | sh
    printf "%s\n" "$settings put system dexonpc_connection_state 0" | sh
    printf "%s\n" "$settings put system edge_lighting 0" | sh
    printf "%s\n" "$settings put system enable_smart_capture 0" | sh
    printf "%s\n" "$settings put system ltw_connected 0" | sh
    printf "%s\n" "$settings put system ltw_smartview_connected 0" | sh
    printf "%s\n" "$settings put system multi_control_enabled 0" | sh
    printf "%s\n" "$settings put system multi_window_enabled 0" | sh
    printf "%s\n" "$settings put system nearby_scanning_enabled 0" | sh
    printf "%s\n" "$settings put system people_stripe 0" | sh
    printf "%s\n" "$settings put system quickshare_enabled 0" | sh
    printf "%s\n" "$settings put system remote_control 0" | sh
    printf "%s\n" "$settings put system sound_alive_effect 0" | sh
    printf "%s\n" "$settings put system support_split_sound 0" | sh
    printf "%s\n" "$settings put system access_control_enabled 0" | sh
    printf "%s\n" "$settings put system adaptive_fast_charging 1" | sh
    printf "%s\n" "$settings put system nearby_scanning_enabled 0" | sh
}}

start_settings_secure {sconfig.mycfg_system_folder}settings
start_system_settings {sconfig.mycfg_system_folder}settings
start_global_settings {sconfig.mycfg_system_folder}settings"""

ADB_SHELL_DISABLE_INPUT_DEVICE = "chmod a-w %s"
ADB_SHELL_REALPATH = """realpath %s"""
ADB_SHELL_DIRNAME = "dirname %s"
ADB_SHELL_MD5SUM = """md5sum -b %s"""
ADB_SHELL_GET_FILE_EXTENSION = """filename="FILEPATH"\necho \"${filename##*.}\""""
ADB_SHELL_REMOVE_STDERR_TMPFILES = (
    r"cd /sdcard/ && find . -type f -name 'xxxstd*' -exec rm {} \;"
)
ADB_SHELL_PASTE_DS = "paste -d '%s' -s %s"
ADB_SHELL_REMOVE_STDOUT_TMPFILES = (
    r"cd /sdcard/ && find . -type f -name 'xxxxstd*' -exec rm {} \;"
)
ADB_SHELL_REMOVE_STDERR_TMPFILES_G = (
    r"cd /sdcard/ && find . -type f -name 'errortmp*' -exec rm {} \;"
)
ADB_SHELL_REMOVE_STDOUT_TMPFILES_G = (
    r"cd /sdcard/ && find . -type f -name 'outputtmp*' -exec rm {} \;"
)
ADB_SHELL_GET_USER_ROTATION = (
    f"{sconfig.mycfg_system_folder}settings get system user_rotation"
)
ADB_SHELL_CRATE_BACKUP = "cp %s{,.bak}"
ADB_SHELL_COPY_DIR_RECURSIVE = "cp -R %s %s"
ADB_SHELL_REMOVE_FOLDER = "rm -r -f %s"
ADB_SHELL_WHOAMI = "whoami"
ADB_SHELL_ID = "id"
ADB_SHELL_USER_GROUPS = "groups"
ADB_SHELL_GET_FILETYPE = "file %s"
ADB_SHELL_COUNT_LINES_WORDS_CHARS = "wc %s"
ADB_SHELL_CHANGE_DICT = "cd %s"
ADB_SHELL_LS = "ls"
ADB_SHELL_REVOKE_OR_GRAND_RIGHTS = r"""#!/usr/bin/env sh
grant=REVOKEORGRANT
package=ANDROIDPACKAGE

givepermission(){
    cmdxx=$(dumpsys package "$package" | grep permission | tr -d " " | awk 'BEGIN{FS=":"} {print $1}' | grep -oE '^.*[A-Z_0-9]+$' | uniq)
    while IFS= read -r permission; do
        pm "$1" "$package" "$permission" 2>/dev/null
    done <<<"$cmdxx"
}
if [ "$grant" -eq 0 ]; then
    givepermission revoke
else
    givepermission grant
fi
    """
ADB_SHELL_GET_ALL_CHMOD_IN_FOLDER = """stat -c '%A %a %n' REPLACE_FOLDER*"""
ADB_SHELL_CHANGE_TO_PREV_WORKING_DICT = "cd -"
ADB_SHELL_EMPTY_FILE = "> %s"
ADB_SHELL_CAT_FILE = "cat %s"
ADB_SHELL_CREATE_NESTED_FOLDER = "mkdir -p %s"
ADB_SHELL_TOUCH = "touch %s"
ADB_SHELL_ALL_KEYBOARDS = f"{sconfig.mycfg_system_folder}ime list -s -a"
ADB_SHELL_LIST_ALL_LISTENING_PORT_AND_PIDS = "netstat -tlnp"
ADB_GET_DEFAULT_KEYBOARD = (
    f"{sconfig.mycfg_system_folder}settings get secure default_input_method"
)
ADB_LIST_ALL_KEYBOARDS = f"{sconfig.mycfg_system_folder}ime list -a"
ADB_ENABLE_KEYBOARD = f"{sconfig.mycfg_system_folder}ime enable %s"
ADB_DISABLE_KEYBOARD = f"{sconfig.mycfg_system_folder}ime disable %s"
ADB_SET_KEYBOARD = f"{sconfig.mycfg_system_folder}ime set %s"
ADB_IS_KEYBOARD_SHOWN = f"{sconfig.mycfg_system_folder}dumpsys input_method"
ADB_KEYBOARD_NAME = "com.android.adbkeyboard/.AdbIME"
ADB_SHOW_TOUCHES = f"{sconfig.mycfg_system_folder}settings put system show_touches 1"
ADB_SHOW_TOUCHES_NOT = (
    f"{sconfig.mycfg_system_folder}settings put system show_touches 0"
)
ADB_KEYBOARD_COMMAND = (
    f"{sconfig.mycfg_system_folder}am broadcast -a ADB_INPUT_B64 --es msg %s"
)
ADB_SELECTED_INPUT_METHOD = f"{sconfig.mycfg_system_folder}cmd settings put secure selected_input_method_subtype 0"
ADB_SHOW_IME_WITH_HARD_KEYBOARD = (
    "cmd settings put secure show_ime_with_hard_keyboard 1"
)
ADB_SHELL_GET_ANDROID_ID = 'sqlite3 /data/*/*/*/gservices.db "select * from main where name = \\"android_id\\";"'
ADB_SHELL_DISABLE_IPV6 = """echo 0 > /proc/sys/net/ipv6/conf/all/accept_ra
echo 0 > /proc/sys/net/ipv6/conf/wlan0/accept_ra
echo 1 > /proc/sys/net/ipv6/conf/all/disable_ipv6
echo 1 > /proc/sys/net/ipv6/conf/wlan0/disable_ipv6
"""
ADB_SHELL_GET_MOUNTED_DEVICES = """mount -v | grep " on " | awk '{print "Partition identifier: " $1  "\\t Mountpoint: "  $3}'"""
ADB_SHELL_SWIPE = f"{sconfig.mycfg_system_folder}input swipe %d %d %d %d %d"
ADB_SHELL_PATH_EXISTS = "if [ -e '%s' ]; then echo '1'; else echo '0'; fi"
ADB_SHELL_IS_FOLDER = "ls -i -H -las -s -d %s"
ADB_SHELL_IS_FILE = """if [ -f "%s" ]; then
    echo 1
else
    echo 0
fi
"""
ADB_SHELL_MKDIR = "mkdir -p %s"
ADB_SHELL_RENAME_FILE = "mv %s %s"
ADB_SHELL_DATE_SETTINGS = (
    f"{sconfig.mycfg_system_folder}am start -a android.settings.DATE_SETTINGS"
)
ADB_SHELL_APPLICATION_DEVELOPMENT_SETTINGS = f"{sconfig.mycfg_system_folder}am start -a com.android.settings.APPLICATION_DEVELOPMENT_SETTINGS"
ADB_SHELL_LOCATION_SOURCE_SETTINGS = f"{sconfig.mycfg_system_folder}am start -a android.settings.LOCATION_SOURCE_SETTINGS"
ADB_SHELL_MEMORY_CARD_SETTINGS = (
    f"{sconfig.mycfg_system_folder}am start -a android.settings.MEMORY_CARD_SETTINGS"
)
ADB_SHELL_LOCALE_SETTINGS = (
    f"{sconfig.mycfg_system_folder}am start -a android.settings.LOCALE_SETTINGS"
)
ADB_SHELL_SEARCH_SETTINGS = (
    f"{sconfig.mycfg_system_folder}am start -a android.search.action.SEARCH_SETTINGS"
)
ADB_SHELL_SETTINGS = (
    f"{sconfig.mycfg_system_folder}am start -a android.net.vpn.SETTINGS"
)
ADB_SHELL_ACCOUNT_SYNC_SETTINGS = (
    f"{sconfig.mycfg_system_folder}am start -a android.settings.ACCOUNT_SYNC_SETTINGS"
)
ADB_SHELL_DISPLAY_SETTINGS = (
    f"{sconfig.mycfg_system_folder}am start -a com.android.settings.DISPLAY_SETTINGS"
)
ADB_SHELL_INPUT_METHOD_SETTINGS = (
    f"{sconfig.mycfg_system_folder}am start -a android.settings.INPUT_METHOD_SETTINGS"
)
ADB_SHELL_SOUND_SETTINGS = (
    f"{sconfig.mycfg_system_folder}am start -a android.settings.SOUND_SETTINGS"
)
ADB_SHELL_WIFI_SETTINGS = (
    f"{sconfig.mycfg_system_folder}am start -a android.settings.WIFI_SETTINGS"
)
ADB_SHELL_APPLICATION_SETTINGS = (
    f"{sconfig.mycfg_system_folder}am start -a android.settings.APPLICATION_SETTINGS"
)
ADB_SHELL_ACCOUNT_SYNC_SETTINGS_ADD_ACCOUNT = f"{sconfig.mycfg_system_folder}am start -a android.settings.ACCOUNT_SYNC_SETTINGS_ADD_ACCOUNT"
ADB_SHELL_MANAGE_APPLICATIONS_SETTINGS = f"{sconfig.mycfg_system_folder}am start -a android.settings.MANAGE_APPLICATIONS_SETTINGS"
ADB_SHELL_SYNC_SETTINGS = (
    f"{sconfig.mycfg_system_folder}am start -a android.settings.SYNC_SETTINGS"
)
ADB_SHELL_DOCK_SETTINGS = (
    f"{sconfig.mycfg_system_folder}am start -a com.android.settings.DOCK_SETTINGS"
)
ADB_SHELL_ADD_ACCOUNT_SETTINGS = (
    f"{sconfig.mycfg_system_folder}am start -a android.settings.ADD_ACCOUNT_SETTINGS"
)
ADB_SHELL_SECURITY_SETTINGS = (
    f"{sconfig.mycfg_system_folder}am start -a android.settings.SECURITY_SETTINGS"
)
ADB_SHELL_DEVICE_INFO_SETTINGS = (
    f"{sconfig.mycfg_system_folder}am start -a android.settings.DEVICE_INFO_SETTINGS"
)
ADB_SHELL_WIRELESS_SETTINGS = (
    f"{sconfig.mycfg_system_folder}am start -a android.settings.WIRELESS_SETTINGS"
)
ADB_SHELL_SYSTEM_UPDATE_SETTINGS = (
    f"{sconfig.mycfg_system_folder}am start -a android.settings.SYSTEM_UPDATE_SETTINGS"
)
ADB_SHELL_MANAGE_ALL_APPLICATIONS_SETTINGS = f"{sconfig.mycfg_system_folder}am start -a android.settings.MANAGE_ALL_APPLICATIONS_SETTINGS"
ADB_SHELL_DATA_ROAMING_SETTINGS = (
    f"{sconfig.mycfg_system_folder}am start -a android.settings.DATA_ROAMING_SETTINGS"
)
ADB_SHELL_APN_SETTINGS = (
    f"{sconfig.mycfg_system_folder}am start -a android.settings.APN_SETTINGS"
)
ADB_SHELL_USER_DICTIONARY_SETTINGS = f"{sconfig.mycfg_system_folder}am start -a android.settings.USER_DICTIONARY_SETTINGS"
ADB_SHELL_VOICE_INPUT_OUTPUT_SETTINGS = f"{sconfig.mycfg_system_folder}am start -a com.android.settings.VOICE_INPUT_OUTPUT_SETTINGS"
ADB_SHELL_TTS_SETTINGS = (
    f"{sconfig.mycfg_system_folder}am start -a com.android.settings.TTS_SETTINGS"
)
ADB_SHELL_WIFI_IP_SETTINGS = (
    f"{sconfig.mycfg_system_folder}am start -a android.settings.WIFI_IP_SETTINGS"
)
ADB_SHELL_WEB_SEARCH_SETTINGS = f"{sconfig.mycfg_system_folder}am start -a android.search.action.WEB_SEARCH_SETTINGS"
ADB_SHELL_BLUETOOTH_SETTINGS = (
    f"{sconfig.mycfg_system_folder}am start -a android.settings.BLUETOOTH_SETTINGS"
)
ADB_SHELL_AIRPLANE_MODE_SETTINGS = (
    f"{sconfig.mycfg_system_folder}am start -a android.settings.AIRPLANE_MODE_SETTINGS"
)
ADB_SHELL_INTERNAL_STORAGE_SETTINGS = f"{sconfig.mycfg_system_folder}am start -a android.settings.INTERNAL_STORAGE_SETTINGS"
ADB_SHELL_ACCESSIBILITY_SETTINGS = (
    f"{sconfig.mycfg_system_folder}am start -a android.settings.ACCESSIBILITY_SETTINGS"
)
ADB_SHELL_QUICK_LAUNCH_SETTINGS = f"{sconfig.mycfg_system_folder}am start -a com.android.settings.QUICK_LAUNCH_SETTINGS"
ADB_SHELL_PRIVACY_SETTINGS = (
    f"{sconfig.mycfg_system_folder}am start -a android.settings.PRIVACY_SETTINGS"
)
ADB_SHELL_DUMPSYS_INPUT = f"{sconfig.mycfg_system_folder}dumpsys input"
ADB_SHELL_RESCAN_ALL_MEDIA = """find %s | while read f; do am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d \"file://${f}\"; done"""
ADB_SHELL_RESCAN_ONE_MEDIA = f"{sconfig.mycfg_system_folder}am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d %s"
ADB_SHELL_LIST_USERS = f"{sconfig.mycfg_system_folder}pm list users"

ADB_SHELL_SCREEN_COMPAT_ON = f"{sconfig.mycfg_system_folder}am screen-compat on %s"
ADB_SHELL_SCREEN_COMPAT_OFF = f"{sconfig.mycfg_system_folder}am screen-compat off %s"
ADB_SHELL_ENABLE_NOTIFICATIONS = (
    f"{sconfig.mycfg_system_folder}settings put global heads_up_notifications_enabled 1"
)
ADB_SHELL_DISABLE_NOTIFICATIONS = (
    f"{sconfig.mycfg_system_folder}settings put global heads_up_notifications_enabled 0"
)
ADB_SHELL_REMOVE_FILE = "rm -f %s"
ADB_SHELL_UNPACK_TAR = "tar xvf %s"
ADB_SHELL_MEMDUMP = memdumpfunction = (
    r"""
getmemdump() {
    cat /proc/$1/maps | grep -v -E "rw-p.*deleted\)" | grep -E "rw-p.*" | awk '{print $1}' | (
        IFS="-"
        while read a b; do
            adec=$(printf "%d\n" 0x"$a")
            bdec=$(printf "%d\n" 0x"$b")
            si=$((bdec - adec))
            fina="/sdcard/$1_mem_$a.bin"
            echo "$fina"
            echo "$adec"
            echo "$bdec"
            echo "$si"
            dd if=/proc/$1/mem ibs=1 obs="$si" skip="$adec" count="$si" of="$fina"
            cat "$fina"
            rm -f "$fina"
        done
    )
}
oldIFS=$IFS
getmemdump
IFS=$oldIFS

"""
    + "\n\n"
)

ADB_GET_imsi = f"{sconfig.mycfg_system_folder}service call iphonesubinfo 7 i32 2"
ADB_GET_imei = f"{sconfig.mycfg_system_folder}service call iphonesubinfo 3 i32 2"
ADB_GET_sims = f"{sconfig.mycfg_system_folder}service call iphonesubinfo 11 i32 2"

ADB_IMEI_MULTI1 = r"""service call iphonesubinfo 4 i32 2 | awk -F "'" '{print $2}' | sed '1 d' | tr -d '.' | awk '{print}' ORS="""
ADB_IMEI_MULTI2 = r"""service call iphonesubinfo 4 i32 1 | awk -F "'" '{print $2}' | sed '1 d' | tr -d '.' | awk '{print}' ORS="""

ADB_IMEI_ANDROID14 = """service call iphonesubinfo 1 s16 com.android.shell | cut -c 52-66 | tr -d '.[:space:]'"""
ADB_SHELL_CLEAR_PACKAGE = f"{sconfig.mycfg_system_folder}pm clear %s"
ADB_SHELL_STILL_IMAGE_CAMERA = (
    f"{sconfig.mycfg_system_folder}am start -a android.media.action.STILL_IMAGE_CAMERA"
)
ADB_SHELL_MAKE_CALL = (
    f"{sconfig.mycfg_system_folder}am start -a android.intent.action.CALL -d tel:%s"
)
ADB_SHELL_DUMPSYS_ACTIVITY_SETTINGS = (
    f"{sconfig.mycfg_system_folder}dumpsys activity settings"
)
ADB_SHELL_DUMPSYS_ACTIVITY_ALLOWED_ASSOCIATIONS = (
    "dumpsys activity allowed-associations"
)
ADB_SHELL_DUMPSYS_ACTIVITY_INTENTS = (
    f"{sconfig.mycfg_system_folder}dumpsys activity intents"
)
ADB_SHELL_DUMPSYS_ACTIVITY_BROADCASTS = (
    f"{sconfig.mycfg_system_folder}dumpsys activity broadcasts"
)
ADB_SHELL_DUMPSYS_ACTIVITY_BROADCAST_STATS = (
    f"{sconfig.mycfg_system_folder}dumpsys activity broadcast-stats"
)
ADB_SHELL_DUMPSYS_ACTIVITY_PROVIDERS = (
    f"{sconfig.mycfg_system_folder}dumpsys activity providers"
)
ADB_SHELL_DUMPSYS_ACTIVITY_PERMISSIONS = (
    f"{sconfig.mycfg_system_folder}dumpsys activity permissions"
)
ADB_SHELL_DUMPSYS_ACTIVITY_SERVICES = (
    f"{sconfig.mycfg_system_folder}dumpsys activity services"
)
ADB_SHELL_DUMPSYS_ACTIVITY_RECENTS = (
    f"{sconfig.mycfg_system_folder}dumpsys activity recents"
)
ADB_SHELL_DUMPSYS_ACTIVITY_LASTANR = (
    f"{sconfig.mycfg_system_folder}dumpsys activity lastanr"
)
ADB_SHELL_DUMPSYS_ACTIVITY_STARTER = (
    f"{sconfig.mycfg_system_folder}dumpsys activity starter"
)
ADB_SHELL_DUMPSYS_ACTIVITY_ACTIVITIES = (
    f"{sconfig.mycfg_system_folder}dumpsys activity activities"
)
ADB_SHELL_DUMPSYS_ACTIVITY_EXIT_INFO = (
    f"{sconfig.mycfg_system_folder}dumpsys activity exit-info"
)
ADB_SHELL_DUMPSYS_ACTIVITY_PROCESSES = (
    f"{sconfig.mycfg_system_folder}dumpsys activity processes"
)
ADB_SHELL_DUMPSYS_ACTIVITY_LRU = f"{sconfig.mycfg_system_folder}dumpsys activity lru"
ADB_SHELL_PM_DUMP = f"{sconfig.mycfg_system_folder}pm dump %s"
ADB_SHELL_GET_WM_SIZE = f"{sconfig.mycfg_system_folder}wm size"
ADB_SHELL_CHANGE_WM_SIZE = f"{sconfig.mycfg_system_folder}wm size %sx%s"
ADB_SHELL_WM_RESET_SIZE = f"{sconfig.mycfg_system_folder}wm size reset"
ADB_SHELL_GET_WM_DENSITY = f"{sconfig.mycfg_system_folder}wm density"
ADB_SHELL_CHANGE_WM_DENSITY = f"{sconfig.mycfg_system_folder}wm density %s"
ADB_SHELL_WM_RESET_DENSITY = f"{sconfig.mycfg_system_folder}wm density reset"
ADB_SHELL_LIST_FEATURES = f"{sconfig.mycfg_system_folder}pm list features"
ADB_SHELL_PWD = "pwd"
ADB_SHELL_LIST_SERVICES = f"{sconfig.mycfg_system_folder}service list"
ADB_SHELL_PS_A_T_L_Z = "ps -A -T -l -Z"
ADB_SHELL_OPEN_URL = (
    f"{sconfig.mycfg_system_folder}am start -a android.intent.action.VIEW -d %s"
)
ADB_SHELL_GET_NTP_SERVER = (
    f"{sconfig.mycfg_system_folder}settings get global ntp_server"
)
ADB_SHELL_SET_NTP_SERVER = 'settings put global ntp_server "%s"'
ADB_SHELL_PM_LIST_PACKAGES_F_I_U = (
    f"{sconfig.mycfg_system_folder}pm list packages -f -i -U"
)
ADB_SHELL_PM_LIST_PACKAGES_3 = f"{sconfig.mycfg_system_folder}pm list packages -3"
ADB_SHELL_PM_LIST_PACKAGES_S = f"{sconfig.mycfg_system_folder}pm list packages -s"
ADB_SHELL_MOUNT = "mount"
ADB_SHELL_CAT = "cat %s"
ADB_SHELL_DISABLE_NETWORK_INTERFACE = "ifconfig %s down &"
ADB_SHELL_ENABLE_NETWORK_INTERFACE = "ifconfig %s up &"
ADB_SHELL_LINUX_VERSION = "uname -a"
ADB_SHELL_CPU_INFO = "cat /proc/cpuinfo"
ADB_SHELL_MEM_INFO = "cat /proc/meminfo"
ADB_SHELL_SCREENCAP = f"{sconfig.mycfg_system_folder}screencap -p"
ADB_SHELL_SCREENCAPRAW = f"{sconfig.mycfg_system_folder}screencap "
ADB_SHELL_REMOUNT_ALL_RW = "mount -o remount,rw /"
ADB_SHELL_REMOUNT_ALL_RO = "mount -o remount,ro /"
ADB_SHELL_REMOVE_DATA_CACHE = r"mount -o remount,rw /; rm -r -f /data/cache"
ADB_SHELL_REMOVE_DALVIK_CACHE = r"mount -o remount,rw /; rm -r -f /data/dalvik-cache"
ADB_SHELL_REMOVE_USER_CACHE = r'mount -o remount,rw /; for cache in /data/user*/*/*/cache/*; do rm -rf "$cache"; done'
ADB_SHELL_GET_ANDROID_VERSION = (
    f"{sconfig.mycfg_system_folder}getprop ro.build.version.release"
)
ADB_SHELL_NETSTAT = r"netstat -n -W -p -a -e"
ADB_SHELL_START_PACKAGE = f"{sconfig.mycfg_system_folder}monkey -p %s 1"
ADB_SHELL_EXPAND_NOTIFICATIONS = (
    f"{sconfig.mycfg_system_folder}cmd statusbar expand-notifications"
)
ADB_SHELL_EXPAND_SETTINGS = (
    f"{sconfig.mycfg_system_folder}cmd statusbar expand-settings"
)
ADB_SHELL_RESOLVE_ACTIVITY_BRIEF = (
    f"{sconfig.mycfg_system_folder}cmd package resolve-activity --brief %s"
)
ADB_SHELL_RESOLVE_ACTIVITY = (
    f"{sconfig.mycfg_system_folder}cmd package resolve-activity %s"
)
ADB_SHELL_LIST_PERMISSION_GROUPS = (
    f"{sconfig.mycfg_system_folder}pm list permission-groups"
)
ADB_SHELL_DUMPSYS_WINDOW = f"{sconfig.mycfg_system_folder}dumpsys window"
ADB_SHELL_INPUT_TAP = f"{sconfig.mycfg_system_folder}input tap %s %s"
ADB_SHELL_INPUT_DPAD_TAP = f"{sconfig.mycfg_system_folder}input dpad tap %s %s"
ADB_SHELL_INPUT_KEYBOARD_TAP = f"{sconfig.mycfg_system_folder}input keyboard tap %s %s"
ADB_SHELL_INPUT_MOUSE_TAP = f"{sconfig.mycfg_system_folder}input mouse tap %s %s"
ADB_SHELL_INPUT_TOUCHPAD_TAP = f"{sconfig.mycfg_system_folder}input touchpad tap %s %s"
ADB_SHELL_INPUT_GAMEPAD_TAP = f"{sconfig.mycfg_system_folder}input gamepad tap %s %s"
ADB_SHELL_INPUT_TOUCHNAVIGATION_TAP = (
    f"{sconfig.mycfg_system_folder}input touchnavigation tap %s %s"
)
ADB_SHELL_INPUT_JOYSTICK_TAP = f"{sconfig.mycfg_system_folder}input joystick tap %s %s"
ADB_SHELL_INPUT_TOUCHSCREEN_TAP = (
    f"{sconfig.mycfg_system_folder}input touchscreen tap %s %s"
)
ADB_SHELL_INPUT_STYLUS_TAP = f"{sconfig.mycfg_system_folder}input stylus tap %s %s"
ADB_SHELL_INPUT_TRACKBALL_TAP = (
    f"{sconfig.mycfg_system_folder}input trackball tap %s %s"
)
ADB_SHELL_INPUT_DPAD_SWIPE = (
    f"{sconfig.mycfg_system_folder}input dpad swipe %s %s %s %s %s"
)
ADB_SHELL_INPUT_DPAD_DRAGANDDROP = (
    f"{sconfig.mycfg_system_folder}input dpad draganddrop %s %s %s %s %s"
)
ADB_SHELL_INPUT_DPAD_ROLL = f"{sconfig.mycfg_system_folder}input dpad roll %s %s"
ADB_SHELL_INPUT_KEYBOARD_SWIPE = (
    f"{sconfig.mycfg_system_folder}input keyboard swipe %s %s %s %s %s"
)
ADB_SHELL_INPUT_KEYBOARD_DRAGANDDROP = (
    f"{sconfig.mycfg_system_folder}input keyboard draganddrop %s %s %s %s %s"
)
ADB_SHELL_INPUT_KEYBOARD_ROLL = (
    f"{sconfig.mycfg_system_folder}input keyboard roll %s %s"
)
ADB_SHELL_INPUT_MOUSE_SWIPE = (
    f"{sconfig.mycfg_system_folder}input mouse swipe %s %s %s %s %s"
)
ADB_SHELL_INPUT_MOUSE_DRAGANDDROP = (
    f"{sconfig.mycfg_system_folder}input mouse draganddrop %s %s %s %s %s"
)
ADB_SHELL_INPUT_MOUSE_ROLL = f"{sconfig.mycfg_system_folder}input mouse roll %s %s"
ADB_SHELL_INPUT_TOUCHPAD_SWIPE = (
    f"{sconfig.mycfg_system_folder}input touchpad swipe %s %s %s %s %s"
)
ADB_SHELL_INPUT_TOUCHPAD_DRAGANDDROP = (
    f"{sconfig.mycfg_system_folder}input touchpad draganddrop %s %s %s %s %s"
)
ADB_SHELL_INPUT_TOUCHPAD_ROLL = (
    f"{sconfig.mycfg_system_folder}input touchpad roll %s %s"
)
ADB_SHELL_INPUT_GAMEPAD_SWIPE = (
    f"{sconfig.mycfg_system_folder}input gamepad swipe %s %s %s %s %s"
)
ADB_SHELL_INPUT_GAMEPAD_DRAGANDDROP = (
    f"{sconfig.mycfg_system_folder}input gamepad draganddrop %s %s %s %s %s"
)
ADB_SHELL_INPUT_GAMEPAD_ROLL = f"{sconfig.mycfg_system_folder}input gamepad roll %s %s"
ADB_SHELL_INPUT_TOUCHNAVIGATION_SWIPE = (
    f"{sconfig.mycfg_system_folder}input touchnavigation swipe %s %s %s %s %s"
)
ADB_SHELL_INPUT_TOUCHNAVIGATION_DRAGANDDROP = (
    "input touchnavigation draganddrop %s %s %s %s %s"
)
ADB_SHELL_INPUT_TOUCHNAVIGATION_ROLL = (
    f"{sconfig.mycfg_system_folder}input touchnavigation roll %s %s"
)
ADB_SHELL_INPUT_JOYSTICK_SWIPE = (
    f"{sconfig.mycfg_system_folder}input joystick swipe %s %s %s %s %s"
)
ADB_SHELL_INPUT_JOYSTICK_DRAGANDDROP = (
    f"{sconfig.mycfg_system_folder}input joystick draganddrop %s %s %s %s %s"
)
ADB_SHELL_INPUT_JOYSTICK_ROLL = (
    f"{sconfig.mycfg_system_folder}input joystick roll %s %s"
)
ADB_SHELL_INPUT_TOUCHSCREEN_SWIPE = (
    f"{sconfig.mycfg_system_folder}input touchscreen swipe %s %s %s %s %s"
)
ADB_SHELL_INPUT_TOUCHSCREEN_DRAGANDDROP = (
    f"{sconfig.mycfg_system_folder}input touchscreen draganddrop %s %s %s %s %s"
)
ADB_SHELL_INPUT_TOUCHSCREEN_ROLL = (
    f"{sconfig.mycfg_system_folder}input touchscreen roll %s %s"
)
ADB_SHELL_INPUT_STYLUS_SWIPE = (
    f"{sconfig.mycfg_system_folder}input stylus swipe %s %s %s %s %s"
)
ADB_SHELL_INPUT_STYLUS_DRAGANDDROP = (
    f"{sconfig.mycfg_system_folder}input stylus draganddrop %s %s %s %s %s"
)
ADB_SHELL_INPUT_STYLUS_ROLL = f"{sconfig.mycfg_system_folder}input stylus roll %s %s"
ADB_SHELL_INPUT_TRACKBALL_SWIPE = (
    f"{sconfig.mycfg_system_folder}input trackball swipe %s %s %s %s %s"
)
ADB_SHELL_INPUT_TRACKBALL_DRAGANDDROP = (
    f"{sconfig.mycfg_system_folder}input trackball draganddrop %s %s %s %s %s"
)
ADB_SHELL_INPUT_TRACKBALL_ROLL = (
    f"{sconfig.mycfg_system_folder}input trackball roll %s %s"
)
ADB_SHELL_GET_PIDOF = "pidof %s"
ADB_SHELL_AM_FORCE_STOP = f"{sconfig.mycfg_system_folder}am force-stop %s"
ADB_SHELL_KILLALL_9 = "killall -9 %s"
ADB_SHELL_AM_KILL = f"{sconfig.mycfg_system_folder}am kill %s"
ADB_SHELL_PKILL = "pkill %s"
ADB_SHELL_AWK_CALCULATOR = 'calc(){ awk "BEGIN{ print $* }" ;}\ncalc %s'
ADB_SHELL_GET_TREEVIEW = r"""(ls %s -R | grep ":$" | sed -e 's/:$//' -e 's/[^-][^\/]*\//--/g' -e 's/^/   /' -e 's/-/|/')"""
ADB_SHELL_GET_LINES_IN_FILE = r"""sed -n '%s,%sp' %s"""
ADB_SHELL_SPECIFIC_LINE_IN_FILE = r"""sed -n %sp %s"""
ADB_SHELL_REMOVE_SPECIFIC_LINE_IN_FILE = r"""sed -i %sd %s"""
ADB_SHELL_CHMOD_ALL_FILES_IN_FOLDER = r"find %s -type f -exec chmod %s {} \;"
ADB_SHELL_COUNT_NETWORK_CONNECTIONS = (
    R"""netstat -ant | awk '{print $NF}' | grep -v '[a-z]' | sort | uniq -c"""
)
ADB_SHELL_CREATE_DICT_AND_CD = """md () { mkdir -p "$@" && cd "$@"; }\nmd %s"""
ADB_SHELL_ALL_CONNECTED_IPS = """netstat -lantp | grep ESTABLISHED |awk '{print $5}' | awk -F: '{print $1}' | sort -u"""
ADB_SHELL_GET_BIOS_INFORMATION = (
    R"""dd if=/dev/mem bs=1k skip=768 count=256 2>/dev/null | strings -n 8"""
)
ADB_SHELL_HEXDUMP = "hexdump -c %s"
ADB_SHELL_COUNT_LINES_IN_FILE = "wc -l %s"
ADB_SHELL_LS_FOLDER = "ls %s"
ADB_SHELL_KERNEL_INFOS = r"""lsmod | cut -d' ' -f1 | xargs modinfo | egrep '^file|^desc|^dep' | sed -e'/^dep/s/$/\n/g'"""
ADB_SHELL_GET_IP_FROM_HOST = (
    R"""ping -c 1 %s | egrep -m1 -o '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'"""
)
ADB_SHELL_NEWEST_FILE_IN_FOLDER = R"""newest () { DIR=${1:-'.'};  CANDIDATE=`find $DIR -type f|head -n1`; while [[ ! -z $CANDIDATE ]]; do BEST=$CANDIDATE; CANDIDATE=`find $DIR -newer "$BEST" -type f|head -n1`; done; echo "$BEST"; }; newest %s"""
ADB_SHELL_GET_IPS = "ip addr show"
ADB_SHELL_PRINT_FILE_WITH_LINENUMBERS = R"""grep -n "^" %s"""
ADB_SHELL_ABS_VALUE_OF_NUMBER = """abs_value=%s; echo ${abs_value#-}"""
ADB_SHELL_GET_DETAILS_FROM_PROCESS = """lsof -p$! %s"""
ADB_SHELL_NETSTAT_TLNP = "netstat -tlnp"
ADB_GET_DETAILS_FROM_ALL_PROCS = "lsof"
ADB_KILL_A_PROCESS_THAT_IS_LOCKING_A_FILE = """fuser -k %s"""
ADB_SHELL_PRINT_LINES_LONGER_THAN = """awk 'length>%s' %s"""
ADB_SHELL_FOLDER_IN_PATH_VAR = """echo "${PATH//:/$\'\\\\n\'}\""""
ADB_SHELL_COMPARE_2_FILES = "cmp %s %s"
ADB_SHELL_SUBSTRING_FROM_STRING = """var='%s'; echo ${var:%s:%s}"""
ADB_SHELL_RM_DRY_RUN = "echo rm %s"
ADB_SHELL_IPV4_INTERFACES = R"""ifconfig -a| awk '/^wlan|^eth|^lo/ {;a=$1;FS=":"; nextline=NR+1; next}{ if (NR==nextline) { split($2,b," ")}{ if ($2 ~ /[0-9]\./) {print a,b[1]}; FS=" "}}'"""
ADB_SHELL_LIST_PROCS_CPU_USAGE = """ps -ef --sort=-%cpu"""
ADB_SHELL_CURRENT_RUNNING_PROCESSES = """ps -eo pcpu,pid,args | sort -n"""
ADB_SHELL_INTERFACES_AND_MAC = R"""for f in /sys/class/net/*; do echo -e "$(basename $f)\t\t$(cat $f/address)"; done"""
ADB_SHELL_FILES_IN_FOLDER_NEWEST_FIRST = """ls -lt %s"""
ADB_SHELL_UPPER_TO_LOWER = """echo %s | tr '[:upper:]' '[:lower:]'"""
ADB_SHELL_NUMBER_OF_CPUS = """grep "processor" /proc/cpuinfo | wc -l"""
ADB_SHELL_GET_INTERNAL_IPS = R"""ifconfig $devices | grep "inet addr" | sed 's/.*inet addr:\([0-9\.]*\).*/\1/g'"""
ADB_SHELL_GET_EXTERNAL_IP = """wget -qO- ifconfig.me/ip"""
ADB_SHELL_GET_EXTERNAL_IP2 = "wget -O - -q icanhazip.com"
ADB_SHELL_TAIL_BYTES = "tail -c %s %s"
ADB_SHELL_TAIL_LINES = "tail -n %s %s"
ADB_SHELL_HEAD_BYTES = "head -c %s %s"
ADB_SHELL_HEAD_LINES = "head -n %s %s"
ADB_SHELL_GET_ALL_MAC_ADDRESSES = (
    R"""ifconfig -a| grep -o -E '([[:xdigit:]]{1,2}:){5}[[:xdigit:]]{1,2}'"""
)
ADB_SHELL_NUMBER_OF_TCP_CONNECTIONS = '''netstat -an|grep -ci "tcp.*established"'''
ADB_SHELL_APPEND_LINE_TO_FILE = """echo "%s" | tee -a %s"""
ADB_SHELL_DUMP_ALL_DB_FILES = R"""#!/bin/bash
for dbfile in `find / -type f -iname "*.db" 2>/dev/null`;do
	echo "$dbfile"
	table_names=$(sqlite3 "$dbfile" '.tables')
	    for table_name in $table_names; do
        echo "Dumping data from $dbfile as CSV for table $table_name:"
        outputfile="/sdcard/${filename}_${table_name}_text.csv"
        sqlite3 "$dbfile" <<EOF | awk -F "|" -v file="$dbfile" -v table="$table_name" 'BEGIN {OFS=","} {print file, table, $1, $2, $3, $4, $5, $6, $7}'
.headers on
.mode list
.output stdout
SELECT * FROM "$table_name";
.quit
EOF
    done
    rm -f /sdcard/*_text.csv
done
"""
ADB_SHELL_DUMP_ALL_DATABASES_IN_DATA_DATA = R"""
#!/bin/bash
for dbfile in `find /data/data -type f -iname "*.db" 2>/dev/null`;do
	echo "$dbfile"
	table_names=$(sqlite3 "$dbfile" '.tables')
	    for table_name in $table_names; do
        echo "Dumping data from $dbfile as CSV for table $table_name:"
        outputfile="/sdcard/${filename}_${table_name}_text.csv"
        sqlite3 "$dbfile" <<EOF | awk -F "|" -v file="$dbfile" -v table="$table_name" 'BEGIN {OFS=","} {print file, table, $1, $2, $3, $4, $5, $6, $7}'
.headers on
.mode list
.output stdout
SELECT * FROM "$table_name";
.quit
EOF
    done
    rm -f /sdcard/*_text.csv
done


"""
ADB_SHELL_CAT_FILE_JOIN_NEWLINES = '''cat %s | tr "\\\\n", " "'''
ADB_SHELL_CHECK_OPEN_PORTS = """netstat -plnt"""
ADB_SHELL_COUNT_FILES_IN_FOLDER = """find %s -maxdepth 1 -type f | wc -l"""
ADB_SHELL_LIST_INPUT_DEVICES = """getevent -pl"""
ADB_SHELL_GET_SENDEVENT_INPUT_DEVICES = R"""
#!/bin/bash
input_dir="/dev/input/"
for event_file in "$input_dir"event*; do
    if [ -e "$event_file" ]; then
        numeric_value=$(getevent -lp "$event_file" | awk -F'[[:space:]]max[[:space:]]|:' '/max/ { split($3, parts, ","); if (parts[1] != " value 0") print parts[1] }')
        if [[ -n "$numeric_value" ]]; then
            echo "$event_file $numeric_value"
        fi
    fi
done
"""

ADB_SHELL_RENAME_FILE_TO_MD5 = """
#!/bin/bash
filename="FINOPATH"
extension=${filename##*.}
md5s=$(md5sum -b "$filename")
dirn=$(dirname "$filename")
wholepath="$dirn/$md5s.$extension"
mv "$filename" "$wholepath"
echo "$wholepath"
"""
ADB_SHELL_GET_SIZE_OF_TERMINAL = "echo $COLUMNS x $LINES"
ADB_SHELL_REMOVE_NEWLINES_FROM_FILE_AND_CAT = R"""tr -d "\n" <"%s" | cat"""
ADB_SHELL_ONE_TIME_PING = """ping -q -c 1 %s"""
ADB_SHELL_CAT_FILE_WITHOUT_LEADING_WHITESPACES = (
    """cat %s | sed -e 's/^[ \\\\t]*//;s/[ \\\\t]*$//'"""
)
ADB_SHELL_VARIABLE_EXISTS = '''[ -z "$%s" ] && echo "0" || echo "1"'''
ADB_SHELL_GET_FILE_WITH_TIMESTAMP = """
get_file_with_tstamp(){
    echo "$1$(date '+_%Y_%m_%d_%H_%M_%S_%N')$2"
}
fi=$(get_file_with_tstamp "REPLACE_FILENAME" "REPLACE_EXT")
echo "$fi"
"""
ADB_SHELL_SYSTEM_MEMORY_DUMP = R"""hexdump -e '90/1 "%_p" "\n"' /dev/mem"""

ADB_SHELL_GET_CWD_OF_PROCS = """
#!/bin/bash
for proc_path in /proc/*/cwd; do
    pid=$(basename "$(dirname "$proc_path")")
    cwd=$(readlink "$proc_path")
    echo "$pid - $cwd"
done
"""
ADB_SHELL_JOBS = "jobs"
ADB_SHELL_JOBS_P = "jobs -p"

ADB_SHELL_REBOOT = "reboot"
ADB_SHELL_SHOW_USED_DISKSPACE = "df"
ADB_SHELL_SHOW_USED_MEMORY = "free"
ADB_SHELL_SORT_FILE_REVERSE = "sort -r %s"
ADB_SHELL_SORT_FILE = "sort %s"
ADB_SHELL_CHMOD_X = "chmod u+x,g+x,o+x %s"
ADB_SHELL_EXECUTE_SH_SCRIPT = "sh %s"
ADB_SHELL_WHICH_A = "which -a %s"
ADB_SHELL_TYPE = "type %s"
ADB_SHELL_CREATE_SYMBOLIC_LINK = "ln -s -f %s %s"
ADB_SHELL_LS_FULL_PATH = """REPLACE_PATH\nls | sed s#^#$(pwd)/#"""
ADB_SHELL_LS_SORT_BY_MOD_DATE = (
    """REPLACE_PATHfind -type f -print0 | xargs -r0 stat -c %y\\ %n | sort"""
)
ADB_SHELL_IPTABLES = "iptables -nL -v --line-numbers"
ADB_SHELL_REVERSE_FILE = """cat %s | sed '1!G;h;$!d'"""
ADB_SHELL_ECHO_BACKWARDS = "echo %s|rev"
ADB_SHELL_NETSTAT_IP_GROUP = """netstat -ntu | awk ' $5 ~ /^[0-9]/ {print $5}' | cut -d: -f1 | sort | uniq -c | sort -n"""
ADB_SHELL_PSTREE = "pstree -p"
ADB_SHELL_LIST_HDS = """awk '/d.[0-9]/{print $4}' /proc/partitions"""
ADB_SHELL_LIST_HDDS_REAL = "ls /sys/bus/scsi/devices"
ADB_SHELL_SORT_AND_UNIQUE = "sort %s | uniq"
ADB_SHELL_LSOF_FILEHANDLES = (
    """lsof | awk '{print $1}' | sort | uniq -c | sort -rn | head"""
)
ADB_SHELL_LIST_ALL_EXE_IN_PATH = """ls `echo $PATH | sed 's/:/ /g'`"""
ADB_SHELL_FREE_MEMORY = """grep '^MemFree:' /proc/meminfo | awk '{ mem=($2)/(1024) ; printf "%0.0f \\n", mem }'"""
ADB_LS_BY_FILESIZE = "REPLACE_PATH\nls -l | sort -nk5"
ADB_SHELL_GET_INSTALL_DATE = """ls -lct /etc/ | tail -1 | awk '{print $6, $7}'"""
ADB_SHELL_GET_AUDIO_PLAYING_PROCS = """lsof | grep pcm"""
ADB_SHELL_GET_KERNEL_INFOS = """awk '{print $1}' "/proc/modules" | xargs modinfo | awk '/^(filename|desc|depends)/'"""
ADB_SHELL_PROCS_WITH_OPEN_CONNECTIONS = """netstat -ntauple"""
ADB_SHELL_CHR = (
    """chr () { printf \\\\$(($1/64*100+$1%64/8*10+$1%8)); }\nchr REPLACE_CHAR"""
)
ADB_SHELL_LIST_ALL_EXTENSIONS_IN_FOLDER = """REPLACE_PATH\nfind . -type f | awk -F'.' '{print $NF}' | sort| uniq -c | sort -g"""
ADB_SHELL_COMMENT_OUT_LINE_IN_FILE = """sed -i '%s s/^/#/' %s"""
ADB_SHELL_MD5_HASHES_FROM_ALL_FILES = (
    """REPLACE_PATH\nfind . -type f -exec md5sum {} \;"""
)
ADB_SHELL_SIZE_OF_FOLDERS = "REPLACE_PATH\ndu -ks */"
ADB_SHELL_DELETE_ALL_FILES_IN_FOLDER_EXCEPT_NEWEST = (
    """REPLACE_PATH\nls -pt1 | sed '/.*\//d' | sed 1d | xargs rm"""
)
ADB_SHELL_APPS_USING_INTERNET = (
    """netstat -lantp | grep -i stab | awk -F/ '{print $2}' | sort | uniq"""
)
ADB_SHELL_GOTO_NEXT_SIBLING_FOLDER = (
    '''cd ../"$(ls -F ..|grep '/'|grep -B1 `basename $PWD`|head -n 1)"\necho "$PWD"'''
)
ADB_SHELL_GOTO_DIR_AND_SEARCH_FOR_STRING = (
    """%s\nfind . -type f -print | xargs grep -n %s"""
)

ADB_SHELL_GETPROPS = "getprop"
ADB_SHELL_GET_ALL_SERVICES_FOR_DUMPSYS = R"""for i in $(dumpsys 2>/dev/null | grep "DUMP OF SERVICE" | cut -d' ' -f4 | cut -d':' -f1); do
  echo "$i"
done
"""

ADB_SHELL_CHECK_FILESIZE = """
check_if_finished_writing(){
     while true; do
            initial_size=$(stat -c %s "$1")
            sleep $2
            current_size=$(stat -c %s "$1")
            if [ "$current_size" -eq "$initial_size" ]; then
                break
            fi
        done
        }
        """

ADB_SHELL_CREATE_DATE_SORTED_FILE_LIST = (
    R"cd %s && find %s -type f -print0 | xargs -0 stat -c %%Y\&%%n | sort >%s && cat %s"
)
ADB_SHELL_GET_ALL_ACTIVITY_ELEMENTS = (
    f"{sconfig.mycfg_system_folder}dumpsys activity top -a -c --checkin"
)
ADB_UIAUTOMATOR_NICE20 = """nice -n %s %s"""
ADB_SHELL_FORCE_IDLE = """
dumpsys deviceidle enable all
dumpsys deviceidle step
dumpsys deviceidle force-idle
"""
ADB_SHELL_UNFORCE_IDLE = """dumpsys deviceidle unforce"""
ADB_SHELL_CURRENT_FOCUS = (
    f"{sconfig.mycfg_system_folder}dumpsys window windows | grep mCurrentFocus"
)
ADB_SHELL_TOP_ALL_PIDS_FROM_PROC_GREP = """
pids=$(top -n 1 | grep 'REPLACEGREP' | grep -v 'grep' | awk '{print $1, $NF}')
        for pid in "$pids"
        do
            echo "$pid"
        done
"""
ADB_SHELL_GET_ALL_POSSIBLE_ACTIVITIES = """dumpsys package -f r activity"""
ADB_SHELL_AM_I_SU = """
which su -- &> /dev/null
    if [[ $? = "0" ]]; then
        echo "True"
    else
        echo "False"
    fi"""
ADB_SHELL_DELETE_FILES_IN_FOLDER_OLDER_THAN = R"""
delete_files_in_folder_older_than(){
  find "$1" -name "$2" -type f -mmin "$3" -exec rm -f {} \;
}

delete_files_in_folder_older_than REPLACEFOLDER "REPLACEFILEFILTER" "REPLACEDISTANCE"

"""
ADB_SHELL_GET_NEWEST_FILE_IN_FOLDER_AS_TAR = R"""
#!/bin/bash

get_newest_file_in_folder_as_tar() {
    cd "$1"
    firstpart=$(find -type f -name "$2" -print0 | xargs -0 stat -c %Y\ %n | sort | tail -n 1)
    secondpart=$(echo "$firstpart" | cut -b 12-1000)
    tar -zcvf "$3" "$secondpart"
}

get_newest_file_in_folder_as_tar REPLACEFOLDER "REPLACEFILEFILTER" "REPLACETARPATH"
"""

ADB_SHELL_TEST_DIRECTORY = """
    if test -d %s; then
        echo 1
    else
        echo 0
    fi"""
ADB_SHELL_TEST_EXISTS_IN_ANY_FORM = """
    if test -e %s; then
        echo 1
    else
        echo 0
    fi"""
ADB_SHELL_TEST_EXECUTABLE = """
    if test -x %s; then
        echo 1
    else
        echo 0
    fi"""
ADB_SHELL_TEST_REGULAR_FILE = """
    if test -f %s; then
        echo 1
    else
        echo 0
    fi"""
ADB_SHELL_TEST_READABLE = """
    if test -r %s; then
        echo 1
    else
        echo 0
    fi"""
ADB_SHELL_TEST_NAMED_PIPE = """
    if test -p %s; then
        echo 1
    else
        echo 0
    fi"""
ADB_SHELL_TEST_BLOCK_DEVICE = """
    if test -b %s; then
        echo 1
    else
        echo 0
    fi"""
ADB_SHELL_TEST_CHARACTER_DEVICE = """
    if test -c %s; then
        echo 1
    else
        echo 0
    fi"""
ADB_SHELL_TEST_CHARACTER_LINK = """
    if test -h %s; then
        echo 1
    else
        echo 0
    fi"""

ADB_SHELL_FILE_LISTING_HUMAN_READABLE = R"""
#!/bin/sh
cd REPLACEDIR
# https://github.com/epety/100-shell-script-examples/blob/master/018-formatdir.sh
gmk()
{
  echo "${1} Kb"
}

if [ $# -gt 1 ] ; then
  echo "Usage: $0 [dirname]" >&2; exit 1
elif [ $# -eq 1 ] ; then
  cd "$@"
fi

for file in *
do
  if [ -d "$file" ] ; then
    size=$(ls "$file" | wc -l | sed 's/[^[:digit:]]//g')
    if [ $size -eq 1 ] ; then
      echo "$file ($size entry)|"
    else
      echo "$file ($size entries)|"
    fi
  else
    size="$(ls -sk "$file" | awk '{print $1}')"
    echo "$file ($(gmk $size))|"
  fi
done | \
  sed 's/ /^^^/g'  | \
  xargs -n 2     | \
  sed 's/\^\^\^/ /g' | \
  awk -F\| '{ printf "%-39s\n%-39s\n", $1, $2 }'


"""

ADB_SHELL_FIND_FULL_FILEPATH = "find %s -print"

ADB_SHELL_CHECK_ENVIRONMENT_VARS = R"""
# https://github.com/epety/100-shell-script-examples/blob/master/047-validator.sh
errors=0

in_path() {
    # given a command and the PATH, try to find the command. Returns
    # 1 if found, 0 if not.  Note that this temporarily modifies the
    # the IFS input field seperator, but restores it upon completion.
    cmd=$1 path=$2 retval=0

    oldIFS=$IFS
    IFS=":"

    for directory in $path; do
        if [ -x $directory/$cmd ]; then
            retval=1 # if we're here, we found $cmd in $directory
        fi
    done
    IFS=$oldIFS
    return $retval
}

validate() {
    varname=$1 varvalue=$2

    if [ ! -z $varvalue ]; then
        if [ "${varvalue%${varvalue#?}}" = "/" ]; then
            if [ ! -x $varvalue ]; then
                echo "** $varname set to $varvalue, but I cannot find executable."
                errors=$(($errors + 1))
            fi
        else
            if in_path $varvalue $PATH; then
                echo "** $varname set to $varvalue, but I cannot find it in PATH."
                errors=$(($errors + 1))
            fi
        fi
    fi
}

####### Beginning of actual shell script #######

if [ ! -x ${SHELL:?"Cannot proceed without SHELL being defined."} ]; then
    echo "** SHELL set to $SHELL, but I cannot find that executable."
    errors=$(($errors + 1))
fi

if [ ! -d ${HOME:?"You need to have your HOME set to your home directory"} ]; then
    echo "** HOME set to $HOME, but it's not a directory."
    errors=$(($errors + 1))
fi

# Our first interesting test: are all the paths in PATH valid?

oldIFS=$IFS
IFS=":" # IFS is the field separator. We'll change to ':'

for directory in $PATH; do
    if [ ! -d $directory ]; then
        echo "** PATH contains invalid directory $directory"
        errors=$(($errors + 1))
    fi
done

IFS=$oldIFS # restore value for rest of script

# The following can be undefined, and they can also be a progname, rather
# than a fully qualified path.  Add additional variables as necessary for
# your site and user community.

validate "EDITOR" $EDITOR
validate "MAILER" $MAILER
validate "PAGER" $PAGER

# and, finally, a different ending depending on whether errors > 0

echo "ERRORS:$errors"


"""

ADB_SHELL_PRINTENV = "printenv"
ADB_SHELL_FREEZE_PROC = "kill -19 %s"
ADB_SHELL_UNFREEZE_PROC = "kill -18 %s"
ADB_SHELL_SHOW_FRAGMENTS_ON_SCREEN = """setprop debug.layout true
service call activity 1599295570"""
ADB_SHELL_PURE_ABS_PATH_OF_FILES = "find %s -type f -print"
ANDROID_PERMISSION_LIST = """'android.permission.ACCEPT_HANDOVER
android.permission.ACCESS_ALL_DOWNLOADS
android.permission.ACCESS_BACKGROUND_LOCATION
android.permission.ACCESS_BLOBS_ACROSS_USERS
android.permission.ACCESS_BLUETOOTH_SHARE
android.permission.ACCESS_CACHE_FILESYSTEM
android.permission.ACCESS_CHECKIN_PROPERTIES
android.permission.ACCESS_COARSE_LOCATION
android.permission.ACCESS_CONTENT_PROVIDERS_EXTERNALLY
android.permission.ACCESS_DOWNLOAD_MANAGER
android.permission.ACCESS_DOWNLOAD_MANAGER_ADVANCED
android.permission.ACCESS_DRM_CERTIFICATES
android.permission.ACCESS_EPHEMERAL_APPS
android.permission.ACCESS_FINE_LOCATION
android.permission.ACCESS_FM_RADIO
android.permission.ACCESS_HIDDEN_PROFILES
android.permission.ACCESS_INPUT_FLINGER
android.permission.ACCESS_KEYGUARD_SECURE_STORAGE
android.permission.ACCESS_LOCATION_EXTRA_COMMANDS
android.permission.ACCESS_MEDIA_LOCATION
android.permission.ACCESS_MOCK_LOCATION
android.permission.ACCESS_MTP
android.permission.ACCESS_NETWORK_CONDITIONS
android.permission.ACCESS_NETWORK_STATE
android.permission.ACCESS_NOTIFICATIONS
android.permission.ACCESS_NOTIFICATION_POLICY
android.permission.ACCESS_PDB_STATE
android.permission.ACCESS_SURFACE_FLINGER
android.permission.ACCESS_VOICE_INTERACTION_SERVICE
android.permission.ACCESS_VR_MANAGER
android.permission.ACCESS_WIFI_STATE
android.permission.ACCESS_WIMAX_STATE
android.permission.ACCOUNT_MANAGER
android.permission.ACTIVITY_RECOGNITION
android.permission.ADD_VOICEMAIL
android.permission.ALLOW_ANY_CODEC_FOR_PLAYBACK
android.permission.ANSWER_PHONE_CALLS
android.permission.ASEC_ACCESS
android.permission.ASEC_CREATE
android.permission.ASEC_DESTROY
android.permission.ASEC_MOUNT_UNMOUNT
android.permission.ASEC_RENAME
android.permission.AUTHENTICATE_ACCOUNTS
android.permission.BACKUP
android.permission.BATTERY_STATS
android.permission.BIND_ACCESSIBILITY_SERVICE
android.permission.BIND_APPWIDGET
android.permission.BIND_APP_FUNCTION_SERVICE
android.permission.BIND_AUTOFILL_SERVICE
android.permission.BIND_CALL_REDIRECTION_SERVICE
android.permission.BIND_CARRIER_MESSAGING_CLIENT_SERVICE
android.permission.BIND_CARRIER_MESSAGING_SERVICE
android.permission.BIND_CARRIER_SERVICES
android.permission.BIND_CHOOSER_TARGET_SERVICE
android.permission.BIND_COMPANION_DEVICE_SERVICE
android.permission.BIND_CONDITION_PROVIDER_SERVICE
android.permission.BIND_CONNECTION_SERVICE
android.permission.BIND_CONTROLS
android.permission.BIND_CREDENTIAL_PROVIDER_SERVICE
android.permission.BIND_DEVICE_ADMIN
android.permission.BIND_DIRECTORY_SEARCH
android.permission.BIND_DREAM_SERVICE
android.permission.BIND_INCALL_SERVICE
android.permission.BIND_INPUT_METHOD
android.permission.BIND_INTENT_FILTER_VERIFIER
android.permission.BIND_JOB_SERVICE
android.permission.BIND_KEYGUARD_APPWIDGET
android.permission.BIND_MIDI_DEVICE_SERVICE
android.permission.BIND_NFC_SERVICE
android.permission.BIND_NOTIFICATION_LISTENER_SERVICE
android.permission.BIND_NOTIFICATION_RANKER_SERVICE
android.permission.BIND_PACKAGE_VERIFIER
android.permission.BIND_PRINT_RECOMMENDATION_SERVICE
android.permission.BIND_PRINT_SERVICE
android.permission.BIND_PRINT_SPOOLER_SERVICE
android.permission.BIND_QUICK_ACCESS_WALLET_SERVICE
android.permission.BIND_QUICK_SETTINGS_TILE
android.permission.BIND_REMOTEVIEWS
android.permission.BIND_REMOTE_DISPLAY
android.permission.BIND_ROUTE_PROVIDER
android.permission.BIND_RUNTIME_PERMISSION_PRESENTER_SERVICE
android.permission.BIND_SCREENING_SERVICE
android.permission.BIND_TELECOM_CONNECTION_SERVICE
android.permission.BIND_TEXT_SERVICE
android.permission.BIND_TRUST_AGENT
android.permission.BIND_TV_AD_SERVICE
android.permission.BIND_TV_INPUT
android.permission.BIND_TV_INTERACTIVE_APP
android.permission.BIND_TV_REMOTE_SERVICE
android.permission.BIND_VISUAL_VOICEMAIL_SERVICE
android.permission.BIND_VOICE_INTERACTION
android.permission.BIND_VPN_SERVICE
android.permission.BIND_VR_LISTENER_SERVICE
android.permission.BIND_WALLPAPER
android.permission.BLUETOOTH
android.permission.BLUETOOTH_ADMIN
android.permission.BLUETOOTH_ADVERTISE
android.permission.BLUETOOTH_CONNECT
android.permission.BLUETOOTH_MAP
android.permission.BLUETOOTH_PRIVILEGED
android.permission.BLUETOOTH_SCAN
android.permission.BLUETOOTH_STACK
android.permission.BODY_SENSORS
android.permission.BODY_SENSORS_BACKGROUND
android.permission.BRICK
android.permission.BROADCAST_CALLLOG_INFO
android.permission.BROADCAST_NETWORK_PRIVILEGED
android.permission.BROADCAST_PACKAGE_REMOVED
android.permission.BROADCAST_PHONE_ACCOUNT_REGISTRATION
android.permission.BROADCAST_SMS
android.permission.BROADCAST_STICKY
android.permission.BROADCAST_WAP_PUSH
android.permission.CACHE_CONTENT
android.permission.CALL_COMPANION_APP
android.permission.CALL_PHONE
android.permission.CALL_PRIVILEGED
android.permission.CAMERA
android.permission.CAMERA_DISABLE_TRANSMIT_LED
android.permission.CAMERA_SEND_SYSTEM_EVENTS
android.permission.CAPTURE_AUDIO_HOTWORD
android.permission.CAPTURE_AUDIO_OUTPUT
android.permission.CAPTURE_SECURE_VIDEO_OUTPUT
android.permission.CAPTURE_TV_INPUT
android.permission.CAPTURE_VIDEO_OUTPUT
android.permission.CARRIER_FILTER_SMS
android.permission.CHANGE_APP_IDLE_STATE
android.permission.CHANGE_BACKGROUND_DATA_SETTING
android.permission.CHANGE_COMPONENT_ENABLED_STATE
android.permission.CHANGE_CONFIGURATION
android.permission.CHANGE_DEVICE_IDLE_TEMP_WHITELIST
android.permission.CHANGE_NETWORK_STATE
android.permission.CHANGE_WIFI_MULTICAST_STATE
android.permission.CHANGE_WIFI_STATE
android.permission.CHANGE_WIMAX_STATE
android.permission.CLEAR_APP_CACHE
android.permission.CLEAR_APP_GRANTED_URI_PERMISSIONS
android.permission.CLEAR_APP_USER_DATA
android.permission.CONFIGURE_DISPLAY_COLOR_TRANSFORM
android.permission.CONFIGURE_WIFI_DISPLAY
android.permission.CONFIRM_FULL_BACKUP
android.permission.CONNECTIVITY_INTERNAL
android.permission.CONTROL_INCALL_EXPERIENCE
android.permission.CONTROL_KEYGUARD
android.permission.CONTROL_LOCATION_UPDATES
android.permission.CONTROL_VPN
android.permission.CONTROL_WIFI_DISPLAY
android.permission.COPY_PROTECTED_DATA
android.permission.CREATE_USERS
android.permission.CREDENTIAL_MANAGER_QUERY_CANDIDATE_CREDENTIALS
android.permission.CREDENTIAL_MANAGER_SET_ALLOWED_PROVIDERS
android.permission.CREDENTIAL_MANAGER_SET_ORIGIN
android.permission.CRYPT_KEEPER
android.permission.DELETE_CACHE_FILES
android.permission.DELETE_PACKAGES
android.permission.DELIVER_COMPANION_MESSAGES
android.permission.DETECT_SCREEN_CAPTURE
android.permission.DETECT_SCREEN_RECORDING
android.permission.DEVICE_POWER
android.permission.DIAGNOSTIC
android.permission.DISABLE_KEYGUARD
android.permission.DISPATCH_NFC_MESSAGE
android.permission.DISPATCH_PROVISIONING_MESSAGE
android.permission.DOWNLOAD_CACHE_NON_PURGEABLE
android.permission.DUMP
android.permission.DVB_DEVICE
android.permission.ENFORCE_UPDATE_OWNERSHIP
android.permission.EXECUTE_APP_ACTION
android.permission.EXPAND_STATUS_BAR
android.permission.FACTORY_TEST
android.permission.FILTER_EVENTS
android.permission.FLASHLIGHT
android.permission.FORCE_BACK
android.permission.FORCE_STOP_PACKAGES
android.permission.FOREGROUND_SERVICE
android.permission.FOREGROUND_SERVICE_CAMERA
android.permission.FOREGROUND_SERVICE_CONNECTED_DEVICE
android.permission.FOREGROUND_SERVICE_DATA_SYNC
android.permission.FOREGROUND_SERVICE_HEALTH
android.permission.FOREGROUND_SERVICE_LOCATION
android.permission.FOREGROUND_SERVICE_MEDIA_PLAYBACK
android.permission.FOREGROUND_SERVICE_MEDIA_PROCESSING
android.permission.FOREGROUND_SERVICE_MEDIA_PROJECTION
android.permission.FOREGROUND_SERVICE_MICROPHONE
android.permission.FOREGROUND_SERVICE_PHONE_CALL
android.permission.FOREGROUND_SERVICE_REMOTE_MESSAGING
android.permission.FOREGROUND_SERVICE_SPECIAL_USE
android.permission.FOREGROUND_SERVICE_SYSTEM_EXEMPTED
android.permission.FRAME_STATS
android.permission.FREEZE_SCREEN
android.permission.GET_ACCOUNTS
android.permission.GET_ACCOUNTS_PRIVILEGED
android.permission.GET_APP_GRANTED_URI_PERMISSIONS
android.permission.GET_APP_OPS_STATS
android.permission.GET_DETAILED_TASKS
android.permission.GET_INTENT_SENDER_INTENT
android.permission.GET_PACKAGE_IMPORTANCE
android.permission.GET_PACKAGE_SIZE
android.permission.GET_PASSWORD
android.permission.GET_PROCESS_STATE_AND_OOM_SCORE
android.permission.GET_TASKS
android.permission.GET_TOP_ACTIVITY_INFO
android.permission.GLOBAL_SEARCH
android.permission.GLOBAL_SEARCH_CONTROL
android.permission.GRANT_RUNTIME_PERMISSIONS
android.permission.HARDWARE_TEST
android.permission.HDMI_CEC
android.permission.HIDE_OVERLAY_WINDOWS
android.permission.HIGH_SAMPLING_RATE_SENSORS
android.permission.INJECT_EVENTS
android.permission.INSTALL_GRANT_RUNTIME_PERMISSIONS
android.permission.INSTALL_LOCATION_PROVIDER
android.permission.INSTALL_PACKAGES
android.permission.INSTALL_SHORTCUT
android.permission.INSTANT_APP_FOREGROUND_SERVICE
android.permission.INTENT_FILTER_VERIFICATION_AGENT
android.permission.INTERACT_ACROSS_PROFILES
android.permission.INTERACT_ACROSS_USERS
android.permission.INTERACT_ACROSS_USERS_FULL
android.permission.INTERNAL_SYSTEM_WINDOW
android.permission.INTERNET
android.permission.INVOKE_CARRIER_SETUP
android.permission.KILL_BACKGROUND_PROCESSES
android.permission.KILL_UID
android.permission.LAUNCH_CAPTURE_CONTENT_ACTIVITY_FOR_NOTE
android.permission.LAUNCH_MULTI_PANE_SETTINGS_DEEP_LINK
android.permission.LAUNCH_TRUST_AGENT_SETTINGS
android.permission.LOADER_USAGE_STATS
android.permission.LOCAL_MAC_ADDRESS
android.permission.LOCATION_HARDWARE
android.permission.LOOP_RADIO
android.permission.MANAGE_ACCOUNTS
android.permission.MANAGE_ACTIVITY_STACKS
android.permission.MANAGE_APP_OPS_RESTRICTIONS
android.permission.MANAGE_APP_TOKENS
android.permission.MANAGE_CA_CERTIFICATES
android.permission.MANAGE_DEVICE_ADMINS
android.permission.MANAGE_DEVICE_LOCK_STATE
android.permission.MANAGE_DEVICE_POLICY_ACCESSIBILITY
android.permission.MANAGE_DEVICE_POLICY_ACCOUNT_MANAGEMENT
android.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS
android.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL
android.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_SECURITY_CRITICAL
android.permission.MANAGE_DEVICE_POLICY_AIRPLANE_MODE
android.permission.MANAGE_DEVICE_POLICY_APPS_CONTROL
android.permission.MANAGE_DEVICE_POLICY_APP_RESTRICTIONS
android.permission.MANAGE_DEVICE_POLICY_APP_USER_DATA
android.permission.MANAGE_DEVICE_POLICY_ASSIST_CONTENT
android.permission.MANAGE_DEVICE_POLICY_AUDIO_OUTPUT
android.permission.MANAGE_DEVICE_POLICY_AUTOFILL
android.permission.MANAGE_DEVICE_POLICY_BACKUP_SERVICE
android.permission.MANAGE_DEVICE_POLICY_BLOCK_UNINSTALL
android.permission.MANAGE_DEVICE_POLICY_BLUETOOTH
android.permission.MANAGE_DEVICE_POLICY_BUGREPORT
android.permission.MANAGE_DEVICE_POLICY_CALLS
android.permission.MANAGE_DEVICE_POLICY_CAMERA
android.permission.MANAGE_DEVICE_POLICY_CAMERA_TOGGLE
android.permission.MANAGE_DEVICE_POLICY_CERTIFICATES
android.permission.MANAGE_DEVICE_POLICY_COMMON_CRITERIA_MODE
android.permission.MANAGE_DEVICE_POLICY_CONTENT_PROTECTION
android.permission.MANAGE_DEVICE_POLICY_DEBUGGING_FEATURES
android.permission.MANAGE_DEVICE_POLICY_DEFAULT_SMS
android.permission.MANAGE_DEVICE_POLICY_DEVICE_IDENTIFIERS
android.permission.MANAGE_DEVICE_POLICY_DISPLAY
android.permission.MANAGE_DEVICE_POLICY_FACTORY_RESET
android.permission.MANAGE_DEVICE_POLICY_FUN
android.permission.MANAGE_DEVICE_POLICY_INPUT_METHODS
android.permission.MANAGE_DEVICE_POLICY_INSTALL_UNKNOWN_SOURCES
android.permission.MANAGE_DEVICE_POLICY_KEEP_UNINSTALLED_PACKAGES
android.permission.MANAGE_DEVICE_POLICY_KEYGUARD
android.permission.MANAGE_DEVICE_POLICY_LOCALE
android.permission.MANAGE_DEVICE_POLICY_LOCATION
android.permission.MANAGE_DEVICE_POLICY_LOCK
android.permission.MANAGE_DEVICE_POLICY_LOCK_CREDENTIALS
android.permission.MANAGE_DEVICE_POLICY_LOCK_TASK
android.permission.MANAGE_DEVICE_POLICY_MANAGED_SUBSCRIPTIONS
android.permission.MANAGE_DEVICE_POLICY_METERED_DATA
android.permission.MANAGE_DEVICE_POLICY_MICROPHONE
android.permission.MANAGE_DEVICE_POLICY_MICROPHONE_TOGGLE
android.permission.MANAGE_DEVICE_POLICY_MOBILE_NETWORK
android.permission.MANAGE_DEVICE_POLICY_MODIFY_USERS
android.permission.MANAGE_DEVICE_POLICY_MTE
android.permission.MANAGE_DEVICE_POLICY_NEARBY_COMMUNICATION
android.permission.MANAGE_DEVICE_POLICY_NETWORK_LOGGING
android.permission.MANAGE_DEVICE_POLICY_ORGANIZATION_IDENTITY
android.permission.MANAGE_DEVICE_POLICY_OVERRIDE_APN
android.permission.MANAGE_DEVICE_POLICY_PACKAGE_STATE
android.permission.MANAGE_DEVICE_POLICY_PHYSICAL_MEDIA
android.permission.MANAGE_DEVICE_POLICY_PRINTING
android.permission.MANAGE_DEVICE_POLICY_PRIVATE_DNS
android.permission.MANAGE_DEVICE_POLICY_PROFILES
android.permission.MANAGE_DEVICE_POLICY_PROFILE_INTERACTION
android.permission.MANAGE_DEVICE_POLICY_PROXY
android.permission.MANAGE_DEVICE_POLICY_QUERY_SYSTEM_UPDATES
android.permission.MANAGE_DEVICE_POLICY_RESET_PASSWORD
android.permission.MANAGE_DEVICE_POLICY_RESTRICT_PRIVATE_DNS
android.permission.MANAGE_DEVICE_POLICY_RUNTIME_PERMISSIONS
android.permission.MANAGE_DEVICE_POLICY_RUN_IN_BACKGROUND
android.permission.MANAGE_DEVICE_POLICY_SAFE_BOOT
android.permission.MANAGE_DEVICE_POLICY_SCREEN_CAPTURE
android.permission.MANAGE_DEVICE_POLICY_SCREEN_CONTENT
android.permission.MANAGE_DEVICE_POLICY_SECURITY_LOGGING
android.permission.MANAGE_DEVICE_POLICY_SETTINGS
android.permission.MANAGE_DEVICE_POLICY_SMS
android.permission.MANAGE_DEVICE_POLICY_STATUS_BAR
android.permission.MANAGE_DEVICE_POLICY_SUPPORT_MESSAGE
android.permission.MANAGE_DEVICE_POLICY_SUSPEND_PERSONAL_APPS
android.permission.MANAGE_DEVICE_POLICY_SYSTEM_APPS
android.permission.MANAGE_DEVICE_POLICY_SYSTEM_DIALOGS
android.permission.MANAGE_DEVICE_POLICY_SYSTEM_UPDATES
android.permission.MANAGE_DEVICE_POLICY_THREAD_NETWORK
android.permission.MANAGE_DEVICE_POLICY_TIME
android.permission.MANAGE_DEVICE_POLICY_USB_DATA_SIGNALLING
android.permission.MANAGE_DEVICE_POLICY_USB_FILE_TRANSFER
android.permission.MANAGE_DEVICE_POLICY_USERS
android.permission.MANAGE_DEVICE_POLICY_VPN
android.permission.MANAGE_DEVICE_POLICY_WALLPAPER
android.permission.MANAGE_DEVICE_POLICY_WIFI
android.permission.MANAGE_DEVICE_POLICY_WINDOWS
android.permission.MANAGE_DEVICE_POLICY_WIPE_DATA
android.permission.MANAGE_DOCUMENTS
android.permission.MANAGE_EXTERNAL_STORAGE
android.permission.MANAGE_FINGERPRINT
android.permission.MANAGE_MEDIA
android.permission.MANAGE_MEDIA_PROJECTION
android.permission.MANAGE_NETWORK_POLICY
android.permission.MANAGE_NOTIFICATIONS
android.permission.MANAGE_ONGOING_CALLS
android.permission.MANAGE_OWN_CALLS
android.permission.MANAGE_PROFILE_AND_DEVICE_OWNERS
android.permission.MANAGE_SOUND_TRIGGER
android.permission.MANAGE_USB
android.permission.MANAGE_USERS
android.permission.MANAGE_VOICE_KEYPHRASES
android.permission.MANAGE_WIFI_INTERFACES
android.permission.MANAGE_WIFI_NETWORK_SELECTION
android.permission.MASTER_CLEAR
android.permission.MEDIA_CONTENT_CONTROL
android.permission.MEDIA_ROUTING_CONTROL
android.permission.MODIFY_APPWIDGET_BIND_PERMISSIONS
android.permission.MODIFY_AUDIO_ROUTING
android.permission.MODIFY_AUDIO_SETTINGS
android.permission.MODIFY_CELL_BROADCASTS
android.permission.MODIFY_DAY_NIGHT_MODE
android.permission.MODIFY_NETWORK_ACCOUNTING
android.permission.MODIFY_PARENTAL_CONTROLS
android.permission.MODIFY_PHONE_STATE
android.permission.MOUNT_FORMAT_FILESYSTEMS
android.permission.MOUNT_UNMOUNT_FILESYSTEMS
android.permission.MOVE_PACKAGE
android.permission.NEARBY_WIFI_DEVICES
android.permission.NET_ADMIN
android.permission.NET_TUNNELING
android.permission.NFC
android.permission.NFC_HANDOVER_STATUS
android.permission.NFC_PREFERRED_PAYMENT_INFO
android.permission.NFC_TRANSACTION_EVENT
android.permission.NOTIFY_PENDING_SYSTEM_UPDATE
android.permission.OBSERVE_GRANT_REVOKE_PERMISSIONS
android.permission.OEM_UNLOCK_STATE
android.permission.OVERRIDE_WIFI_CONFIG
android.permission.PACKAGE_USAGE_STATS
android.permission.PACKAGE_VERIFICATION_AGENT
android.permission.PACKET_KEEPALIVE_OFFLOAD
android.permission.PEERS_MAC_ADDRESS
android.permission.PERFORM_CDMA_PROVISIONING
android.permission.PERFORM_SIM_ACTIVATION
android.permission.PERSISTENT_ACTIVITY
android.permission.POST_NOTIFICATIONS
android.permission.PROCESS_CALLLOG_INFO
android.permission.PROCESS_OUTGOING_CALLS
android.permission.PROCESS_PHONE_ACCOUNT_REGISTRATION
android.permission.PROVIDE_OWN_AUTOFILL_SUGGESTIONS
android.permission.PROVIDE_REMOTE_CREDENTIALS
android.permission.PROVIDE_TRUST_AGENT
android.permission.QUERY_ALL_PACKAGES
android.permission.QUERY_DO_NOT_ASK_CREDENTIALS_ON_BOOT
android.permission.RANGING
android.permission.READ_ASSISTANT_APP_SEARCH_DATA
android.permission.READ_BASIC_PHONE_STATE
android.permission.READ_BLOCKED_NUMBERS
android.permission.READ_CALENDAR
android.permission.READ_CALL_LOG
android.permission.READ_CONTACTS
android.permission.READ_DREAM_STATE
android.permission.READ_DROPBOX_DATA
android.permission.READ_EXTERNAL_STORAGE
android.permission.READ_FRAME_BUFFER
android.permission.READ_HOME_APP_SEARCH_DATA
android.permission.READ_INPUT_STATE
android.permission.READ_INSTALL_SESSIONS
android.permission.READ_LOGS
android.permission.READ_MEDIA_AUDIO
android.permission.READ_MEDIA_IMAGES
android.permission.READ_MEDIA_VIDEO
android.permission.READ_MEDIA_VISUAL_USER_SELECTED
android.permission.READ_NEARBY_STREAMING_POLICY
android.permission.READ_NETWORK_USAGE_HISTORY
android.permission.READ_OEM_UNLOCK_STATE
android.permission.READ_PHONE_NUMBERS
android.permission.READ_PHONE_STATE
android.permission.READ_PRECISE_PHONE_STATE
android.permission.READ_PRIVILEGED_PHONE_STATE
android.permission.READ_PROFILE
android.permission.READ_SEARCH_INDEXABLES
android.permission.READ_SMS
android.permission.READ_SOCIAL_STREAM
android.permission.READ_SYNC_SETTINGS
android.permission.READ_SYNC_STATS
android.permission.READ_USER_DICTIONARY
android.permission.READ_VOICEMAIL
android.permission.READ_WIFI_CREDENTIAL
android.permission.REAL_GET_TASKS
android.permission.REBOOT
android.permission.RECEIVE_BLUETOOTH_MAP
android.permission.RECEIVE_BOOT_COMPLETED
android.permission.RECEIVE_DATA_ACTIVITY_CHANGE
android.permission.RECEIVE_EMERGENCY_BROADCAST
android.permission.RECEIVE_MEDIA_RESOURCE_USAGE
android.permission.RECEIVE_MMS
android.permission.RECEIVE_SMS
android.permission.RECEIVE_STK_COMMANDS
android.permission.RECEIVE_WAP_PUSH
android.permission.RECEIVE_WIFI_CREDENTIAL_CHANGE
android.permission.RECORD_AUDIO
android.permission.RECOVERY
android.permission.REGISTER_CALL_PROVIDER
android.permission.REGISTER_CONNECTION_MANAGER
android.permission.REGISTER_SIM_SUBSCRIPTION
android.permission.REGISTER_WINDOW_MANAGER_LISTENERS
android.permission.REMOTE_AUDIO_PLAYBACK
android.permission.REMOVE_DRM_CERTIFICATES
android.permission.REMOVE_TASKS
android.permission.REORDER_TASKS
android.permission.REQUEST_COMPANION_PROFILE_APP_STREAMING
android.permission.REQUEST_COMPANION_PROFILE_AUTOMOTIVE_PROJECTION
android.permission.REQUEST_COMPANION_PROFILE_COMPUTER
android.permission.REQUEST_COMPANION_PROFILE_GLASSES
android.permission.REQUEST_COMPANION_PROFILE_NEARBY_DEVICE_STREAMING
android.permission.REQUEST_COMPANION_PROFILE_WATCH
android.permission.REQUEST_COMPANION_RUN_IN_BACKGROUND
android.permission.REQUEST_COMPANION_SELF_MANAGED
android.permission.REQUEST_COMPANION_START_FOREGROUND_SERVICES_FROM_BACKGROUND
android.permission.REQUEST_COMPANION_USE_DATA_IN_BACKGROUND
android.permission.REQUEST_DELETE_PACKAGES
android.permission.REQUEST_IGNORE_BATTERY_OPTIMIZATIONS
android.permission.REQUEST_INSTALL_PACKAGES
android.permission.REQUEST_OBSERVE_COMPANION_DEVICE_PRESENCE
android.permission.REQUEST_OBSERVE_DEVICE_UUID_PRESENCE
android.permission.REQUEST_PASSWORD_COMPLEXITY
android.permission.RESET_FINGERPRINT_LOCKOUT
android.permission.RESET_SHORTCUT_MANAGER_THROTTLING
android.permission.RESTART_PACKAGES
android.permission.RETRIEVE_WINDOW_CONTENT
android.permission.RETRIEVE_WINDOW_TOKEN
android.permission.REVOKE_RUNTIME_PERMISSIONS
android.permission.RUN_USER_INITIATED_JOBS
android.permission.RUN_IN_BACKGROUND
android.permission.SCHEDULE_EXACT_ALARM
android.permission.SCORE_NETWORKS
android.permission.SEND_CALL_LOG_CHANGE
android.permission.SEND_DOWNLOAD_COMPLETED_INTENTS
android.permission.SEND_RESPOND_VIA_MESSAGE
android.permission.SEND_SMS
android.permission.SEND_SMS_NO_CONFIRMATION
android.permission.SERIAL_PORT
android.permission.SET_ACTIVITY_WATCHER
android.permission.SET_ALARM
android.permission.SET_ALWAYS_FINISH
android.permission.SET_ANIMATION_SCALE
android.permission.SET_BIOMETRIC_DIALOG_ADVANCED
android.permission.SET_DEBUG_APP
android.permission.SET_INPUT_CALIBRATION
android.permission.SET_KEYBOARD_LAYOUT
android.permission.SET_ORIENTATION
android.permission.SET_POINTER_SPEED
android.permission.SET_PREFERRED_APPLICATIONS
android.permission.SET_PROCESS_LIMIT
android.permission.SET_SCREEN_COMPATIBILITY
android.permission.SET_TIME
android.permission.SET_TIME_ZONE
android.permission.SET_WALLPAPER
android.permission.SET_WALLPAPER_COMPONENT
android.permission.SET_WALLPAPER_HINTS
android.permission.SHUTDOWN
android.permission.SIGNAL_PERSISTENT_PROCESSES
android.permission.SMS_FINANCIAL_TRANSACTIONS
android.permission.START_ANY_ACTIVITY
android.permission.START_FOREGROUND_SERVICES_FROM_BACKGROUND
android.permission.START_PRINT_SERVICE_CONFIG_ACTIVITY
android.permission.START_TASKS_FROM_RECENTS
android.permission.START_VIEW_APP_FEATURES
android.permission.START_VIEW_PERMISSION_USAGE
android.permission.STATUS_BAR
android.permission.STATUS_BAR_SERVICE
android.permission.STOP_APP_SWITCHES
android.permission.STORAGE_INTERNAL
android.permission.SUBSCRIBED_FEEDS_READ
android.permission.SUBSCRIBED_FEEDS_WRITE
android.permission.SUBSCRIBE_TO_KEYGUARD_LOCKED_STATE
android.permission.SUBSTITUTE_NOTIFICATION_APP_NAME
android.permission.SYSTEM_ALERT_WINDOW
android.permission.TABLET_MODE
android.permission.TEMPORARY_ENABLE_ACCESSIBILITY
android.permission.TETHER_PRIVILEGED
android.permission.TRANSMIT_IR
android.permission.TRUST_LISTENER
android.permission.TURN_SCREEN_ON
android.permission.TV_INPUT_HARDWARE
android.permission.TV_VIRTUAL_REMOTE_CONTROLLER
android.permission.UNINSTALL_SHORTCUT
android.permission.UPDATE_APP_OPS_STATS
android.permission.UPDATE_CONFIG
android.permission.UPDATE_DEVICE_STATS
android.permission.UPDATE_LOCK
android.permission.UPDATE_LOCK_TASK_PACKAGES
android.permission.UPDATE_PACKAGES_WITHOUT_USER_ACTION
android.permission.USER_ACTIVITY
android.permission.USE_BIOMETRIC
android.permission.USE_CREDENTIALS
android.permission.USE_EXACT_ALARM
android.permission.USE_FINGERPRINT
android.permission.USE_FULL_SCREEN_INTENT
android.permission.USE_ICC_AUTH_WITH_DEVICE_IDENTIFIER
android.permission.USE_SIP
android.permission.UWB_RANGING
android.permission.VIBRATE
android.permission.WAKE_LOCK
android.permission.WRITE_APN_SETTINGS
android.permission.WRITE_BLOCKED_NUMBERS
android.permission.WRITE_CALENDAR
android.permission.WRITE_CALL_LOG
android.permission.WRITE_CONTACTS
android.permission.WRITE_DREAM_STATE
android.permission.WRITE_EXTERNAL_STORAGE
android.permission.WRITE_GSERVICES
android.permission.WRITE_MEDIA_STORAGE
android.permission.WRITE_PROFILE
android.permission.WRITE_SECURE_SETTINGS
android.permission.WRITE_SETTINGS
android.permission.WRITE_SMS
android.permission.WRITE_SOCIAL_STREAM
android.permission.WRITE_SYNC_SETTINGS
android.permission.WRITE_SYSTEM_PREFERENCES
android.permission.WRITE_USER_DICTIONARY
android.permission.WRITE_VOICEMAIL'"""

ADB_SHELL_GRAND_ALL_ANDROID_RIGHTS_TO_PACKAGE = f"""grant_all_android_permissions() {{
    /system/bin/cmd role set-bypassing-role-qualification true
    allcmds={ANDROID_PERMISSION_LIST}
    for line in $(seq 1 $(printf "%s\n" "$allcmds\n" | wc -l)); do
        script2execute="$(printf "%s\n" "$allcmds" | sed -n "${{line}}p")"
        {sconfig.mycfg_system_folder}pm grant $1 $script2execute 2>/dev/null
        withoutprefix=$(echo "$script2execute" | sed -E 's/^android.permission.//g')
        {sconfig.mycfg_system_folder}cmd appops set "$1" "$withoutprefix" allow 2>/dev/null
    done
{sconfig.mycfg_system_folder}cmd overlay enable "$1"
{sconfig.mycfg_system_folder}am set-standby-bucket "$1" "active"
{sconfig.mycfg_system_folder}pm set-app-links-allowed --package "$1" true

}}

grant_all_android_permissions REPLACE_WITH_PACKAGE
"""

ADB_SHELL_REVOKE_ALL_ANDROID_RIGHTS_FROM_PACKAGE = f"""revoke_all_android_permissions() {{
    /system/bin/cmd role set-bypassing-role-qualification true
    allcmds={ANDROID_PERMISSION_LIST}
    for line in $(seq 1 $(printf "%s\n" "$allcmds\n" | wc -l)); do
        script2execute="$(printf "%s\n" "$allcmds" | sed -n "${{line}}p")"
        {sconfig.mycfg_system_folder}pm revoke $1 $script2execute 2>/dev/null
        withoutprefix=$(echo "$script2execute" | sed -E 's/^android.permission.//g')
        {sconfig.mycfg_system_folder}cmd appops set "$1" "$withoutprefix" ignore 2>/dev/null
    done
{sconfig.mycfg_system_folder}cmd overlay disable "$1"
{sconfig.mycfg_system_folder}am set-standby-bucket "$1" "restricted"
{sconfig.mycfg_system_folder}pm set-app-links-allowed --package "$1" false

}}

revoke_all_android_permissions REPLACE_WITH_PACKAGE
"""


def remove_accents_from_text(text):
    textlist = []
    for t in text.splitlines():
        t = t.replace("ß", "ss").replace("ẞ", "SS")
        t = "".join(
            [
                lookup(k, case_sens=True, replace="", add_to_printable="")["suggested"]
                for k in t
            ]
        )
        textlist.append(t)
    text = "\n".join(textlist)
    return text


def _write_data_using_dd(
    path_on_device,
    lendata,
    numberofloops,
    inputdev="/dev/input/event3",
    blocksize=72,
    sleepbetweencommand=0,
    exec_or_eval="exec",
):
    if sleepbetweencommand > 0:
        sleepbetweencommand = f"sleep {sleepbetweencommand}"
    else:
        sleepbetweencommand = ""
    if exec_or_eval == "eval":
        quotes = '"'
        commandline = f"eval {quotes}dd status=none conv=sync count=1 skip=$skiphowmany bs=$blocksize if=$inputfile of=$outdevice{quotes}"
    else:
        commandline = 'dd status=none conv=sync count=1 skip="$skiphowmany" bs="$blocksize" if="$inputfile" of="$outdevice"'
    return rf"""#!/bin/sh
inputfile={path_on_device}
outdevice={inputdev}
totalchars={lendata}
blocksize={blocksize}
howmanyloops={numberofloops}
skiphowmany=0
for line in $(seq 1 $howmanyloops); do
        skiphowmany=$((line-1))
        {commandline}
        {sleepbetweencommand}
        skiphowmany=$((skiphowmany+1))
done
        """


def create_struct_mouse_move_commands(
    allcoords,
    y_max,
    x_max,
    screen_height,
    screen_width,
    inputdev="/dev/input/event3",
    FORMAT="llHHI" * 3,
    path_on_device="/sdcard/neu.bin",
    path_on_device_sh="/sdcard/neu.sh",
    qty_blocks=6,
    exec_or_eval="exec",
    sleepbetweencommand=0,
):
    structcmds = []

    chunk_size = struct.calcsize(FORMAT)
    pack_fu = struct.Struct(FORMAT).pack
    for x, y in allcoords:
        try:
            tstamp = ceil(time.time())
            ycoord = int(y * y_max / screen_height)
            xcoord = int(x * x_max / screen_width)
            p1 = (tstamp, 363320, 3, 0, xcoord)
            p2 = (tstamp, 363321, 3, 1, ycoord)
            p3 = (tstamp, 363322, 0, 0, 0)
            f = pack_fu(*p1, *p2, *p3)
            structcmds.append(f)
        except Exception:
            errwrite()

    binary_data = b"\n".join(structcmds)
    with open(path_on_device, mode="wb") as f:
        f.write(binary_data)
    lendata = len(binary_data)
    blocksize = (chunk_size) * qty_blocks
    numberofloops = (lendata // blocksize) + 1

    ddscript = _write_data_using_dd(
        path_on_device,
        lendata,
        numberofloops,
        inputdev=inputdev,
        blocksize=blocksize,
        sleepbetweencommand=sleepbetweencommand,
        exec_or_eval=exec_or_eval,
    )
    with open(path_on_device_sh, mode="w", encoding="utf-8") as f:
        f.write(ddscript)


def create_mouse_downswipe(
    inputdev,
    start_y=0.1,
    end_y=0.9,
    x_coord=0.5,
    qty_blocks=8,
    screen_width=416,
    screen_height=693,
    x_max=65535,
    y_max=65535,
    bin_path="/sdcard/upswipe_middle.bin",
    sh_path="/sdcard/upswipe_middle.sh",
):
    downswipe_coords = [
        [int(screen_width * x_coord), x]
        for x in range(int(screen_height * start_y), int(screen_height * end_y))
    ]
    create_struct_mouse_move_commands(
        allcoords=downswipe_coords,
        y_max=y_max,
        x_max=x_max,
        screen_height=screen_height,
        screen_width=screen_width,
        inputdev=inputdev,
        FORMAT="llHHI" * 3,
        path_on_device=bin_path,
        path_on_device_sh=sh_path,
        qty_blocks=6 * qty_blocks,
        exec_or_eval="exec",
        sleepbetweencommand=0,
    )
    mycmd = f"su -c '/system/bin/sh {sh_path}'"
    return lambda: os.system(mycmd)


def create_mouse_upswipe(
    inputdev,
    start_y=0.1,
    end_y=0.9,
    x_coord=0.5,
    qty_blocks=8,
    screen_width=416,
    screen_height=693,
    x_max=65535,
    y_max=65535,
    bin_path="/sdcard/upswipe_middle.bin",
    sh_path="/sdcard/upswipe_middle.sh",
):
    downswipe_coords = [
        [int(screen_width * x_coord), x]
        for x in range(int(screen_height * start_y), int(screen_height * end_y))
    ]
    upswipe_coords = list(reversed(downswipe_coords))
    create_struct_mouse_move_commands(
        allcoords=upswipe_coords,
        y_max=y_max,
        x_max=x_max,
        screen_height=screen_height,
        screen_width=screen_width,
        inputdev=inputdev,
        FORMAT="llHHI" * 3,
        path_on_device=bin_path,
        path_on_device_sh=sh_path,
        qty_blocks=6 * qty_blocks,
        exec_or_eval="exec",
        sleepbetweencommand=0,
    )
    mycmd = f"su -c '/system/bin/sh {sh_path}'"
    return lambda: os.system(mycmd)


def get_step_set_dict(how_many=10):
    step = {}

    for z in range(how_many):
        x = z + 1
        step[x] = set()

        try:
            for y in range(1, x):
                if y > 0:
                    step[x].add(y)
        except Exception:
            errwrite()
    return step


def iskeyboardshown():
    try:
        pr = subprocess.run(
            """/system/bin/dumpsys input_method | grep -E "mInputShown|mVisibleBound" """,
            shell=True,
            env=os.environ,
            timeout=10,
            capture_output=True,
        )
        stdout, stderr, returncode = pr.stdout, pr.stderr, pr.returncode
        print(stdout, stderr, returncode)
        if b"mVisibleBound=true" in stdout and b"mInputShown=true" in stdout:
            return True
        return False
    except Exception:
        errwrite()
    return False


def get_clickcommand(
    inputdev=None,
    path_on_device_click="/sdcard/cmd_click.bin",
):
    FORMAT = "llHHI" * 8
    tstamp = int(time.time())
    pack_fu = struct.Struct(FORMAT).pack
    p1 = (tstamp, 864860, 1, 272, 0)
    p2 = (tstamp, 864860, 0, 0, 0)
    p3 = (tstamp, 910010, 1, 272, 1)
    p4 = (tstamp, 910010, 0, 0, 0)
    clickcommand = pack_fu(*p1, *p2, *p3, *p4, *p1, *p2, *p3, *p4)
    with open(path_on_device_click, mode="wb") as f:
        f.write(clickcommand)
    dst = inputdev
    mycmd = f"su -c 'cp {path_on_device_click} {dst}'"
    return lambda: os.system(mycmd)


def touch(path: str) -> bool:
    # touch('f:\\dada\\baba\\caca\\myfile.html')
    # original: https://github.com/andrewp-as-is/touch.py (not working anymore)
    def _fullpath(path):
        return os.path.abspath(os.path.expanduser(path))

    def _mkdir(path):
        path = path.replace("\\", "/")
        if path.find("/") > 0 and not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))

    def _utime(path):
        try:
            os.utime(path, None)
        except Exception:
            open(path, "a").close()

    def touch_(path):
        if path:
            path = _fullpath(path)
            _mkdir(path)
            _utime(path)

    try:
        touch_(path)
        return True
    except Exception as Fe:
        print(Fe)
        return False


def split_text_at_quotes(text):
    return [
        f"'{x}'" if x not in '''\'""''' else repr(x)
        for x in re_split_quotes.split(text)
    ]


def split_text_in_letters(text):
    return [f"'{x}'" if x not in '''\'""''' else repr(x) for x in text]


def sleep_random_time(sleep_after_letter):
    if sum(sleep_after_letter) > 0:
        sleep(random.uniform(*sleep_after_letter))


def split_text_in_chars_or_parts(text, sleep_after_letter):
    if sum(sleep_after_letter) == 0:
        return split_text_at_quotes(text)
    else:
        return split_text_in_letters(text)


def format_input_command(input_device, action, command):
    if input_device:
        cmd2send = (
            f"{sconfig.mycfg_system_folder}input {input_device} {action} {command}"
        )
    else:
        cmd2send = f"{sconfig.mycfg_system_folder}input {action} {command}"
    return cmd2send


def format_url(url):
    if not url.lower().startswith("http://") and not url.lower().startswith("https://"):
        if "://" not in url:
            url = "http://" + url
    return url


def strip_quotes_and_escape(s):
    if isinstance(s, bytes):
        return s
    s = s.strip("'\"")
    s = s.replace("\\", "\\\\")
    s = s.replace("%", "\\%")
    s = s.replace(" ", "\\ ")
    s = s.replace('"', '\\"')
    s = s.replace("'", "\\'")
    s = s.replace("(", "\\(")
    s = s.replace(")", "\\)")
    s = s.replace("&", "\\&")
    s = s.replace("<", "\\<")
    s = s.replace(">", "\\>")
    s = s.replace(";", "\\;")
    s = s.replace("*", "\\*")
    s = s.replace("|", "\\|")
    s = s.replace("~", "\\~")
    s = s.replace("¬", "\\¬")
    s = s.replace("`", "\\`")
    s = s.replace("¦", "\\¦")
    return s


@lru_cache
def lookup(
    l: str, case_sens: bool = True, replace: str = "", add_to_printable: str = ""
):
    v = sorted(unicodedata.name(l).split(), key=len)
    sug = replace
    stri_pri = string.printable + add_to_printable.upper()
    is_printable_letter = v[0] in stri_pri
    is_printable = l in stri_pri
    is_capital = "CAPITAL" in v
    if is_printable_letter:
        sug = v[0]

        if case_sens:
            if not is_capital:
                sug = v[0].lower()
    elif is_printable:
        sug = l
    return {
        "all_data": v,
        "is_printable_letter": is_printable_letter,
        "is_printable": is_printable,
        "is_capital": is_capital,
        "suggested": sug,
    }


def get_tmpfile(suffix=".txt"):
    tfp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    filename = tfp.name
    filename = os.path.normpath(filename)
    tfp.close()
    purefile = filename.split(os.sep)[-1]
    return purefile, filename, partial(os.remove, tfp.name)


ADB_SHELL_SVC_POWER_REBOOT = f"{sconfig.mycfg_system_folder}svc power reboot"
ADB_SHELL_SVC_POWER_SHUTDOWN = f"{sconfig.mycfg_system_folder}svc power shutdown"
ADB_SHELL_DISABLE_PACKAGE_FOR_USER = (
    f"{sconfig.mycfg_system_folder}pm disable-user --user %s %s"
)
ADB_SHELL_TRY_RW_VARIATIONS = """
check_if_mounted() {
    mountcheckervalue=0
    mountchecker="$(mount -v | grep -v 'rw' | grep 'ro' | awk 'BEGIN{FS="[\\(]+";}{print $2}' | awk 'BEGIN{FS="[\\),]+";}{if ($1 ~ /^ro$/){ print 1;exit}}')"
    printf "%s\n" "$mountchecker"
    mountcheckervalue=$((mountcheckervalue + mountchecker))
    return "$mountcheckervalue"
}

modr() {

    if ! check_if_mounted; then
        mount -o remount,rw /
    else
        return 0
    fi
    if ! check_if_mounted; then
        su -c "mount -o remount,rw /"
    else
        return 0
    fi

    if ! check_if_mounted; then
        su -c "mount --all -o remount,rw -t vfat1"
    else
        return 0
    fi

    if ! check_if_mounted; then
        su -c 'mount --all -o remount,rw -t ext4'
    else
        return 0
    fi

    if ! check_if_mounted; then
        su -c 'mount -o remount,rw'
    else
        return 0
    fi

    if ! check_if_mounted; then
        su -c "mount -o remount,rw /;"
    else
        return 0
    fi

    if ! check_if_mounted; then
        mount -o remount,rw /
    else
        return 0
    fi
    if ! check_if_mounted; then
        su -c "mount -o remount,rw /"
    else
        return 0
    fi

    if ! check_if_mounted; then
        su -c 'mount -o rw&&remount /'
    else
        return 0
    fi

    if ! check_if_mounted; then
        su -c 'mount -o rw;remount /'
    else
        return 0
    fi

    if ! check_if_mounted; then
        mount --all -o remount,rw -t vfat
    else
        return 0
    fi
    if ! check_if_mounted; then
        su -c "mount --all -o remount,rw -t vfat"
    else
        return 0
    fi

    if ! check_if_mounted; then
        mount -o remount,rw /
    else
        return 0
    fi
    if ! check_if_mounted; then
        su -c "mount -o remount,rw /"
    else
        return 0
    fi
    if ! check_if_mounted; then
        mount --all -o remount,rw -t vfat
    else
        return 0
    fi
    if ! check_if_mounted; then
        su -c "mount --all -o remount,rw -t vfat"
    else
        return 0
    fi
    if ! check_if_mounted; then
        getprop --help >/dev/null
        su -c 'mount -o remount,rw /;'
    else
        return 0
    fi
    if ! check_if_mounted; then
        su -c 'mount -o remount,rw /;'
    else
        return 0
    fi

    if ! check_if_mounted; then
        mount -v | grep "^/" | grep -v '\\(rw,' | grep '\\(ro' | awk '{print "mount -o rw,remount " $1 " " $3}' | tr '\n' '\0' | xargs -0 -n1 su -c
    else
        return 0
    fi

    if ! check_if_mounted; then
        mount -v | grep "^/" | grep -v '\\(rw,' | grep '\\(ro' | awk '{print "mount -o rw,remount " $1 " " $3}' | su -c sh
    else
        return 0
    fi

    if ! check_if_mounted; then
        mount -v | grep "^/" | grep -v '\\(rw,' | grep '\\(ro' | awk '{system("mount -o rw,remount " $1 " " $3)}'
    else
        return 0
    fi

    if ! check_if_mounted; then
        su -c 'mount -v | grep -E "^/" | awk '\''{print "mount -o rw,remount " $1 " " $3}'\''' | tr '\n' '\0' | xargs -0 -n1 su -c
    else
        return 0
    fi

    if ! check_if_mounted; then
        mount -Ev | grep -Ev 'nodev' | grep -Ev '/proc' | grep -v '\\(rw,' | awk 'BEGIN{FS="([[:space:]]+(on|type)[[:space:]]+)|([[:space:]]+\\()"}{print "mount -o rw,remount " $1 " " $2}' | xargs -n5 | su -c
    else
        return 0
    fi

    if ! check_if_mounted; then
        su -c 'mount -v | grep -E "^/" | awk '\''{print "mount -o rw,remount " $1 " " $3}'\''' | sh su -c
    else
        return 0
    fi

    if ! check_if_mounted; then
        getprop --help >/dev/null
        su -c 'mount -v | grep -E "^/" | awk '\''{print "mount -o rw,remount " $1 " " $3}'\''' | tr '\n' '\0' | xargs -0 -n1 | su -c sh
    else
        return 0
    fi
    return 1
}
modr 2>/dev/null"""


ADB_SHELL_CLOSE_SYSTEM_DIALOGS = f"{sconfig.mycfg_system_folder}am broadcast -a android.intent.action.CLOSE_SYSTEM_DIALOGS"
ADB_SHELL_SET_STANDBY_BUCKET_ACTIVE = (
    f'{sconfig.mycfg_system_folder}am set-standby-bucket "%s" "Active"'
)

ADB_SHELL_DISABLE_BLUR = f"{sconfig.mycfg_system_folder}cmd window disable-blur 1"
ADB_SHELL_RUN_IN_BACKGROUND_ALLOW = (
    f"{sconfig.mycfg_system_folder}cmd appops set %s RUN_IN_BACKGROUND allow"
)
ADB_SHELL_RUN_IN_BACKGROUND_DENY = (
    f"{sconfig.mycfg_system_folder}cmd appops set %s RUN_IN_BACKGROUND ignore"
)
ADB_SHELL_SET_HIGH_PERFORMANCE_MODE = (
    f"{sconfig.mycfg_system_folder}cmd settings put global high_performance 1"
)
ADB_SHELL_SET_LOW_PERFORMANCE_MODE = (
    f"{sconfig.mycfg_system_folder}cmd settings put global high_performance 0"
)
ADB_SHELL_SET_DEFAULT_BROWSER = f"""{sconfig.mycfg_system_folder}cmd role set-bypassing-role-qualification true;{sconfig.mycfg_system_folder}cmd role add-role-holder android.app.role.BROWSER %s"""

ADB_SHELL_INSTALL_EXISTING_PACKAGE_FOR_USER = (
    f"{sconfig.mycfg_system_folder}pm install-existing --user %s %s"
)
ADB_SHELL_SWITCH_USER = f"{sconfig.mycfg_system_folder}am switch-user %s"
ADB_SHELL_STOP_USER = f"{sconfig.mycfg_system_folder}am stop-user %s"
ADB_SET_DENSITY = f"{sconfig.mycfg_system_folder}wm density %s"
ADB_AM_START_PACKAGE = f'''{sconfig.mycfg_system_folder}am start "$({sconfig.mycfg_system_folder}cmd package resolve-activity --brief %s | tail -n 1)"'''

ADB_AM_START_PACKAGE_WITH_RIGHTS_NO_ANIMATION = f"""{sconfig.mycfg_system_folder}am start %s --grant-read-uri-permission --grant-persistable-uri-permission --grant-prefix-uri-permission --grant-write-uri-permission --activity-no-animation"""

ADB_SHELL_ACTIVATE_ACCESSIBILITY_SERVICE = f"""
qx="$({sconfig.mycfg_system_folder}settings get secure enabled_accessibility_services)"
rr=%s
if [ "$qx" != "$rr" ]; then
    {sconfig.mycfg_system_folder}settings put secure enabled_accessibility_services %s
fi
"""


class ExecuteShellCmds:
    def __init__(self, print_cmds=True):
        self.stand_kwargs = {
            "capture_output": True,
            "shell": True,
            "env": os.environ,
            "cwd": os.getcwd(),
        }
        self.print_cmds = print_cmds

    def sh_activate_accessibility_service(self, service, service_activity, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_ACTIVATE_ACCESSIBILITY_SERVICE % (service, service_activity),
            **kwargs,
        )

    def sh_am_start_package_with_rights_no_animation(self, package, **kwargs):
        return self.execute_sh_command(
            ADB_AM_START_PACKAGE_WITH_RIGHTS_NO_ANIMATION % package,
            **kwargs,
        )

    def sh_am_start_package(self, package, **kwargs):
        return self.execute_sh_command(ADB_AM_START_PACKAGE % package, **kwargs)

    def sh_set_density(self, density, **kwargs):
        return self.execute_sh_command(ADB_SET_DENSITY % str(density), **kwargs)

    def sh_switch_user(self, user, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_SWITCH_USER % str(user),
            **kwargs,
        )

    def sh_stop_user(self, user, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_STOP_USER % str(user),
            **kwargs,
        )

    def sh_install_existing_package_for_user(self, user, package, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_INSTALL_EXISTING_PACKAGE_FOR_USER % (str(user), package),
            **kwargs,
        )

    def sh_set_default_browser(self, package, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_SET_DEFAULT_BROWSER % package,
            **kwargs,
        )

    def sh_set_high_performance_mode(self, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_SET_HIGH_PERFORMANCE_MODE,
            **kwargs,
        )

    def sh_set_low_performance_mode(self, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_SET_LOW_PERFORMANCE_MODE,
            **kwargs,
        )

    def sh_set_run_in_background_allow(self, package, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_RUN_IN_BACKGROUND_ALLOW % package,
            **kwargs,
        )

    def sh_set_run_in_background_deny(self, package, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_RUN_IN_BACKGROUND_DENY % package,
            **kwargs,
        )

    def sh_disable_blug(self, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_DISABLE_BLUR,
            **kwargs,
        )

    def sh_set_standby_bucket_active(self, package, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_SET_STANDBY_BUCKET_ACTIVE % package,
            **kwargs,
        )

    def sh_close_system_dialogs(self, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_CLOSE_SYSTEM_DIALOGS,
            **kwargs,
        )

    def sh_try_rw_variations(self, **kwargs):
        return self.execute_sh_command_as_input(
            ADB_SHELL_TRY_RW_VARIATIONS,
            **kwargs,
        )

    ########################################################################################################
    def sh_disable_package_for_user(self, package, user=0, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_DISABLE_PACKAGE_FOR_USER % (str(user), package),
            **kwargs,
        )

    ########################################################################################################

    def sh_set_some_speed_up_configs(self, **kwargs):
        return self.execute_sh_command_as_input(
            ADB_SHELL_SOME_SPEED_UP_CONFIG,
            **kwargs,
        )

    ########################################################################################################

    def sh_svc_power_shutdown(self, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_SVC_POWER_SHUTDOWN,
            **kwargs,
        )

    ########################################################################################################
    def sh_svc_power_reboot(self, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_SVC_POWER_REBOOT,
            **kwargs,
        )

    def execute_sh_command(self, cmd, **kwargs):
        if self.print_cmds:
            print(cmd)
            pprint(kwargs)
        try:
            p = subprocess.run(cmd, **{**self.stand_kwargs, **kwargs})
            return [
                p.stdout.splitlines(keepends=True),
                p.stderr.splitlines(keepends=True),
            ]
        except Exception:
            errwrite()
            return [[], []]

    def execute_sh_command_as_input(self, cmd, **kwargs):
        if self.print_cmds:
            print(cmd)
            pprint(kwargs)
        try:
            p = subprocess.run(
                sconfig.mycfg_shell,
                input=cmd.encode("utf-8") if isinstance(cmd, str) else cmd,
                **{**self.stand_kwargs, **kwargs},
            )
            return [
                p.stdout.splitlines(keepends=True),
                p.stderr.splitlines(keepends=True),
            ]
        except Exception:
            errwrite()
            return [[], []]

    def sh_grant_all_android_rights_to_package(self, package, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_GRAND_ALL_ANDROID_RIGHTS_TO_PACKAGE.replace(
                "REPLACE_WITH_PACKAGE", package
            ),
            **kwargs,
        )

    def sh_input_tap(self, x, y, **kwargs):
        return self.execute_sh_command(ADB_SHELL_INPUT_TAP % (int(x), int(y)), **kwargs)

    def sh_get_android_version(self, **kwargs):
        so, se = self.execute_sh_command(ADB_SHELL_GET_ANDROID_VERSION, **kwargs)
        if so:
            return so[0].strip().decode()

    def sh_copy_dir_recursive(self, src, dst, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_COPY_DIR_RECURSIVE % (src, dst), **kwargs
        )

    def sh_paste(self, file, delimiter=" ", **kwargs):
        return self.execute_sh_command(ADB_SHELL_PASTE_DS % (delimiter, file), **kwargs)

    def sh_tail_bytes(self, n, file, **kwargs):
        return self.execute_sh_command(ADB_SHELL_TAIL_BYTES % (int(n), file), **kwargs)

    def sh_tail_lines(self, n, file, **kwargs):
        return self.execute_sh_command(ADB_SHELL_TAIL_LINES % (int(n), file), **kwargs)

    def sh_head_bytes(self, n, file, **kwargs):
        return self.execute_sh_command(ADB_SHELL_HEAD_BYTES % (int(n), file), **kwargs)

    def sh_head_lines(self, n, file, **kwargs):
        return self.execute_sh_command(ADB_SHELL_HEAD_LINES % (int(n), file), **kwargs)

    def sh_remove_folder(self, folder, **kwargs):
        return self.execute_sh_command(ADB_SHELL_REMOVE_FOLDER % (folder,), **kwargs)

    def sh_number_of_lines_words_chars_in_file(self, file, **kwargs):
        try:
            return list(
                map(
                    int,
                    self.execute_sh_command(
                        ADB_SHELL_COUNT_LINES_WORDS_CHARS % file, **kwargs
                    )[0][0]
                    .strip()
                    .split(maxsplit=3)[:3],
                )
            )
        except Exception as e:
            sys.stderr.write(f"{e}")
            sys.stderr.flush()
        return []

    def sh_create_bak_of_file(self, file, **kwargs):
        return self.execute_sh_command(ADB_SHELL_CRATE_BACKUP % file, **kwargs)

    def sh_ls(self, **kwargs):
        so, se = self.execute_sh_command(ADB_SHELL_LS, **kwargs)
        if not so and se:
            kwargs.update(su=True)
            so, se = self.execute_sh_command(ADB_SHELL_LS, **kwargs)
        return so, se

    def sh_empty_file(self, path, **kwargs):
        return self.execute_sh_command(ADB_SHELL_EMPTY_FILE % path, **kwargs)

    def format_output(self, stdout):
        return b"".join(stdout)

    def sh_cat_file(self, path, **kwargs):
        path2 = strip_quotes_and_escape(path)
        da = self.execute_sh_command(ADB_SHELL_CAT_FILE % path2, **kwargs)[0]
        if not da:
            da = self.execute_sh_command(ADB_SHELL_CAT_FILE % f'"{path}"', **kwargs)[0]

        return self.format_output(da)

    def sh_cat_file_without_newlines(self, path, **kwargs):
        path2 = strip_quotes_and_escape(path)
        da = self.execute_sh_command(
            ADB_SHELL_REMOVE_NEWLINES_FROM_FILE_AND_CAT % path2, **kwargs
        )[0]
        if not da:
            da = self.execute_sh_command(
                ADB_SHELL_REMOVE_NEWLINES_FROM_FILE_AND_CAT % f'"{path}"', **kwargs
            )[0]
        return self.format_output(da)

    def sh_ping_one_time(self, url, **kwargs):
        return self.execute_sh_command(ADB_SHELL_ONE_TIME_PING % url, **kwargs)

    def sh_cat_file_without_leading_whitespaces(self, path, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_CAT_FILE_WITHOUT_LEADING_WHITESPACES % path, **kwargs
        )

    def sh_variable_exists(self, variable, **kwargs):
        so, se = self.execute_sh_command(ADB_SHELL_VARIABLE_EXISTS % variable, **kwargs)
        if so:
            return bool(int(so[0].strip().decode()))
        return False

    def sh_create_file_with_content(self, filedata, path, append=False, **kwargs):
        if not isinstance(filedata, bytes):
            filedata = filedata.encode()
        eni = base64.standard_b64encode(filedata).decode("utf-8", "strict")
        if not append:
            enicmd = f"base64 -d <<< $(echo -n {eni}) > {path}".encode()
        else:
            enicmd = f"base64 -d <<< $(echo -n {eni}) >> {path}".encode()

        return self.execute_sh_command(enicmd, **kwargs)

    def sh_append_to_file(self, filedata, path, **kwargs):
        return self.sh_create_file_with_content(filedata, path, append=True, **kwargs)

    def sh_echo_rev(self, string, **kwargs):
        return self.execute_sh_command(ADB_SHELL_ECHO_BACKWARDS % string, **kwargs)

    def sh_netstat_ip_group(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_NETSTAT_IP_GROUP, **kwargs)

    def sh_process_tree(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_PSTREE, **kwargs)

    def sh_list_hdds(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_LIST_HDS, **kwargs)

    def sh_list_hdds_real(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_LIST_HDDS_REAL, **kwargs)

    def sh_lsof_filehandles(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_LSOF_FILEHANDLES, **kwargs)

    def sh_list_exe_in_path(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_LIST_ALL_EXE_IN_PATH, **kwargs)

    def sh_free_memory(self, **kwargs):
        so, se = self.execute_sh_command(ADB_SHELL_FREE_MEMORY, **kwargs)
        if so:
            return int(so[0].strip().decode())

    def sh_cat_file_without_leading_whitespaces(self, path, **kwargs):
        return self.execute_sh_command(ADB_SHELL_SORT_AND_UNIQUE % path, **kwargs)

    def _all_outputlist_to_one(self, *args):
        allout = []
        for arg in args:
            allout.extend(arg)
        return allout

    def list_all_listening_ports_and_pid(self, **kwargs):
        return [
            g
            for x in self.execute_sh_command(
                ADB_SHELL_LIST_ALL_LISTENING_PORT_AND_PIDS, **kwargs
            )[0]
            if len(g := (x.strip().split(maxsplit=6))) == 7
            and re.search(rb"^\d+", g[1])
        ]

    def sh_screencap(self, correct_newlines=True, **kwargs):
        if "wait_to_complete" not in kwargs:
            kwargs.update({"wait_to_complete": 0.01})

        stdout, stderr = self.execute_sh_command(ADB_SHELL_SCREENCAPRAW, **kwargs)
        if not correct_newlines:
            return b"".join(stdout)
        # else:
        return self.format_output(stdout)

    def sh_screencap_png(self, correct_newlines=True, **kwargs):
        if "wait_to_complete" not in kwargs:
            kwargs.update({"wait_to_complete": 0.01})

        stdout, stderr = self.execute_sh_command(ADB_SHELL_SCREENCAP, **kwargs)
        if not correct_newlines:
            return b"".join(stdout)
        return self.format_output(stdout)

    def pull(self, path):
        stdout, stderr = self.execute_sh_command(f'cat "{path}"')
        if stderr:
            stdout, stderr = self.execute_sh_command(
                f"cat {strip_quotes_and_escape(path)}"
            )
        return self.format_output(stdout)

    def push_folder(self, folder, dstfolder):
        olddir = os.getcwd()
        os.chdir(folder)
        purefile, filename, deletefu = get_tmpfile(suffix=".tar")
        try:
            tar = tarfile.open(filename, "w")
            tar.add(".", recursive=True)
        finally:
            tar.close()
            os.chdir(olddir)
        stdout1, stderr1 = self.push(filename, dstfolder)
        stdout2, stderr2 = self.execute_sh_command(
            f"cd {dstfolder};" + ADB_SHELL_UNPACK_TAR % purefile
        )
        stdout3, stderr3 = self.execute_sh_command(ADB_SHELL_REMOVE_FILE % purefile)
        deletefu()
        allout = self._all_outputlist_to_one(stdout1, stdout2, stdout3)
        allerrs = self._all_outputlist_to_one(stderr1, stderr2, stderr3)

        return allout, allerrs

    def get_memdump_from_process(self, pid, **kwargs):
        memdumpfunction = ADB_SHELL_MEMDUMP + str(pid)
        return self.execute_sh_command(memdumpfunction, **kwargs)

    def sh_pkill(self, package, **kwargs):
        return self.execute_sh_command(ADB_SHELL_PKILL % package, **kwargs)

    def sh_am_kill(self, package, **kwargs):
        return self.execute_sh_command(ADB_SHELL_AM_KILL % package, **kwargs)

    def sh_killall9(self, package, **kwargs):
        return self.execute_sh_command(ADB_SHELL_KILLALL_9 % package, **kwargs)

    def get_imeis_multidevices(self):
        a = (
            b"".join(self.execute_sh_command(ADB_IMEI_MULTI1)[0])
            .strip()
            .decode("utf-8")
        )
        b = (
            b"".join(self.execute_sh_command(ADB_IMEI_MULTI2)[0])
            .strip()
            .decode("utf-8")
        )
        return a, b

    def sh_kill(self, package, **kwargs):
        return self.execute_sh_command(f"kill {self.sh_get_pid_of(package)}", **kwargs)

    def sh_force_stop(self, package, **kwargs):
        return self.execute_sh_command(ADB_SHELL_AM_FORCE_STOP % package, **kwargs)

    def sh_get_pid_of(self, package, **kwargs):
        stdout, stderr = self.execute_sh_command(
            ADB_SHELL_GET_PIDOF % package, **kwargs
        )
        try:
            if stdout:
                return int(stdout[0].strip())
        except Exception:
            sys.stderr.write(f"{package} not found\n")
            return -1

    def kill_package(self, package, **kwargs):
        stdoutlist = []
        stderrlist = []
        stdout, stderr = self.sh_force_stop(package, **kwargs)
        stdoutlist.extend(stdout)
        stderrlist.extend(stderr)
        stdout, stderr = self.sh_kill(package, **kwargs)
        stdoutlist.extend(stdout)
        stderrlist.extend(stderr)
        stdout, stderr = self.sh_killall9(package, **kwargs)
        stdoutlist.extend(stdout)
        stderrlist.extend(stderr)
        stdout, stderr = self.sh_am_kill(package, **kwargs)
        stdoutlist.extend(stdout)
        stderrlist.extend(stderr)
        stdout, stderr = self.sh_pkill(package, **kwargs)
        stdoutlist.extend(stdout)
        stderrlist.extend(stderr)
        return [stdoutlist, stderrlist]

    def sh_grep(
        self,
        reg,
        path,
        escape=True,
        quote=False,
        extended_regexp=True,
        ignore_case=True,
        recursively=False,
        line_number=True,
        invert_match=False,
        files_with_matches=False,
        count=False,
        **kwargs,
    ):
        if isinstance(path, str):
            path = [path]
        if escape:
            path = [strip_quotes_and_escape(p) for p in path]
        allpath = []
        if quote:
            for p in path:
                if '"' in p:
                    p = f"'{p}'"
                else:
                    p = f'"{p}"'
            allpath.append(p)
        else:
            allpath.extend(path)
        whole_command = ["grep", f'"{reg}"', "--text"]
        if extended_regexp:
            whole_command.append("--extended-regexp")
        if ignore_case:
            whole_command.append("--ignore-case")
        if recursively:
            whole_command.append("-R")
        if line_number:
            whole_command.append("--line-number")
        if invert_match:
            whole_command.append("--invert-match")
        if files_with_matches:
            whole_command.append("--files-with-matches")
        if count:
            whole_command.append("--count")

        wholecommandstr = " ".join(whole_command) + " " + " ".join(allpath)
        return self.execute_sh_command(
            wholecommandstr,
            **kwargs,
        )

    def sh_input_dpad_longtap(self, x, y, t=1.0, **kwargs):
        return self.sh_input_dpad_drag_and_drop(x, y, x, y, t, **kwargs)

    def sh_input_keyboard_longtap(self, x, y, t=1.0, **kwargs):
        return self.sh_input_keyboard_drag_and_drop(x, y, x, y, t, **kwargs)

    def sh_input_mouse_longtap(self, x, y, t=1.0, **kwargs):
        return self.sh_input_mouse_drag_and_drop(x, y, x, y, t, **kwargs)

    def sh_input_touchpad_longtap(self, x, y, t=1.0, **kwargs):
        return self.sh_input_touchpad_drag_and_drop(x, y, x, y, t, **kwargs)

    def sh_input_gamepad_longtap(self, x, y, t=1.0, **kwargs):
        return self.sh_input_gamepad_drag_and_drop(x, y, x, y, t, **kwargs)

    def sh_input_touchnavigation_longtap(self, x, y, t=1.0, **kwargs):
        return self.sh_input_touchnavigation_drag_and_drop(x, y, x, y, t, **kwargs)

    def sh_input_joystick_longtap(self, x, y, t=1.0, **kwargs):
        return self.sh_input_joystick_drag_and_drop(x, y, x, y, t, **kwargs)

    def sh_input_touchscreen_longtap(self, x, y, t=1.0, **kwargs):
        return self.sh_input_touchscreen_drag_and_drop(x, y, x, y, t, **kwargs)

    def sh_input_stylus_longtap(self, x, y, t=1.0, **kwargs):
        return self.sh_input_stylus_drag_and_drop(x, y, x, y, t, **kwargs)

    def sh_input_trackball_longtap(self, x, y, t=1.0, **kwargs):
        return self.sh_input_trackball_drag_and_drop(x, y, x, y, t, **kwargs)

    def sh_input_dpad_swipe(self, x0, y0, x1, y1, t=1.0, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_INPUT_DPAD_SWIPE
            % (int(x0), int(y0), int(x1), int(y1), int(t * 1000)),
            **kwargs,
        )

    def sh_input_dpad_drag_and_drop(self, x0, y0, x1, y1, t=1.0, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_INPUT_DPAD_DRAGANDDROP
            % (int(x0), int(y0), int(x1), int(y1), int(t * 1000)),
            **kwargs,
        )

    def sh_input_dpad_roll(self, x, y, **kwargs):
        return (
            self.execute_sh_command(
                ADB_SHELL_INPUT_DPAD_ROLL % (int(x), int(y)), **kwargs
            ),
        )

    def sh_input_keyboard_swipe(self, x0, y0, x1, y1, t=1.0, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_INPUT_KEYBOARD_SWIPE
            % (int(x0), int(y0), int(x1), int(y1), int(t * 1000)),
            **kwargs,
        )

    def sh_input_keyboard_drag_and_drop(self, x0, y0, x1, y1, t=1.0, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_INPUT_KEYBOARD_DRAGANDDROP
            % (int(x0), int(y0), int(x1), int(y1), int(t * 1000)),
            **kwargs,
        )

    def sh_input_keyboard_roll(self, x, y, **kwargs):
        return (
            self.execute_sh_command(
                ADB_SHELL_INPUT_KEYBOARD_ROLL % (int(x), int(y)), **kwargs
            ),
        )

    def sh_input_mouse_swipe(self, x0, y0, x1, y1, t=1.0, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_INPUT_MOUSE_SWIPE
            % (int(x0), int(y0), int(x1), int(y1), int(t * 1000)),
            **kwargs,
        )

    def sh_input_mouse_drag_and_drop(self, x0, y0, x1, y1, t=1.0, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_INPUT_MOUSE_DRAGANDDROP
            % (int(x0), int(y0), int(x1), int(y1), int(t * 1000)),
            **kwargs,
        )

    def sh_input_mouse_roll(self, x, y, **kwargs):
        return (
            self.execute_sh_command(
                ADB_SHELL_INPUT_MOUSE_ROLL % (int(x), int(y)), **kwargs
            ),
        )

    def sh_input_touchpad_swipe(self, x0, y0, x1, y1, t=1.0, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_INPUT_TOUCHPAD_SWIPE
            % (int(x0), int(y0), int(x1), int(y1), int(t * 1000)),
            **kwargs,
        )

    def sh_revoke_all_package_permissions(self, package, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_REVOKE_OR_GRAND_RIGHTS.replace("ANDROIDPACKAGE", package).replace(
                "REVOKEORGRANT", "0"
            ),
            **kwargs,
        )

    def sh_grant_all_package_permissions(self, package, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_REVOKE_OR_GRAND_RIGHTS.replace("ANDROIDPACKAGE", package).replace(
                "REVOKEORGRANT", "1"
            ),
            **kwargs,
        )

    def sh_get_my_android_id(self, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_GET_ANDROID_ID,
            **kwargs,
        )

    def sh_disable_ipv6(self, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_DISABLE_IPV6,
            **kwargs,
        )

    def sh_show_mounted_devices(self, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_GET_MOUNTED_DEVICES,
            **kwargs,
        )

    def sh_input_touchpad_drag_and_drop(self, x0, y0, x1, y1, t=1.0, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_INPUT_TOUCHPAD_DRAGANDDROP
            % (int(x0), int(y0), int(x1), int(y1), int(t * 1000)),
            **kwargs,
        )

    def sh_input_touchpad_roll(self, x, y, **kwargs):
        return (
            self.execute_sh_command(
                ADB_SHELL_INPUT_TOUCHPAD_ROLL % (int(x), int(y)), **kwargs
            ),
        )

    def sh_input_gamepad_swipe(self, x0, y0, x1, y1, t=1.0, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_INPUT_GAMEPAD_SWIPE
            % (int(x0), int(y0), int(x1), int(y1), int(t * 1000)),
            **kwargs,
        )

    def sh_input_gamepad_drag_and_drop(self, x0, y0, x1, y1, t=1.0, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_INPUT_GAMEPAD_DRAGANDDROP
            % (int(x0), int(y0), int(x1), int(y1), int(t * 1000)),
            **kwargs,
        )

    def sh_input_gamepad_roll(self, x, y, **kwargs):
        return (
            self.execute_sh_command(
                ADB_SHELL_INPUT_GAMEPAD_ROLL % (int(x), int(y)), **kwargs
            ),
        )

    def sh_input_touchnavigation_swipe(self, x0, y0, x1, y1, t=1.0, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_INPUT_TOUCHNAVIGATION_SWIPE
            % (int(x0), int(y0), int(x1), int(y1), int(t * 1000)),
            **kwargs,
        )

    def sh_input_touchnavigation_drag_and_drop(self, x0, y0, x1, y1, t=1.0, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_INPUT_TOUCHNAVIGATION_DRAGANDDROP
            % (int(x0), int(y0), int(x1), int(y1), int(t * 1000)),
            **kwargs,
        )

    def sh_input_touchnavigation_roll(self, x, y, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_INPUT_TOUCHNAVIGATION_ROLL % (int(x), int(y)), **kwargs
        )

    def sh_input_joystick_swipe(self, x0, y0, x1, y1, t=1.0, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_INPUT_JOYSTICK_SWIPE
            % (int(x0), int(y0), int(x1), int(y1), int(t * 1000)),
            **kwargs,
        )

    def sh_input_joystick_drag_and_drop(self, x0, y0, x1, y1, t=1.0, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_INPUT_JOYSTICK_DRAGANDDROP
            % (int(x0), int(y0), int(x1), int(y1), int(t * 1000)),
            **kwargs,
        )

    def sh_input_joystick_roll(self, x, y, **kwargs):
        return (
            self.execute_sh_command(
                ADB_SHELL_INPUT_JOYSTICK_ROLL % (int(x), int(y)), **kwargs
            ),
        )

    def sh_input_touchscreen_swipe(self, x0, y0, x1, y1, t=1.0, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_INPUT_TOUCHSCREEN_SWIPE
            % (int(x0), int(y0), int(x1), int(y1), int(t * 1000)),
            **kwargs,
        )

    def sh_input_touchscreen_drag_and_drop(self, x0, y0, x1, y1, t=1.0, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_INPUT_TOUCHSCREEN_DRAGANDDROP
            % (int(x0), int(y0), int(x1), int(y1), int(t * 1000)),
            **kwargs,
        )

    def sh_input_touchscreen_roll(self, x, y, **kwargs):
        return (
            self.execute_sh_command(
                ADB_SHELL_INPUT_TOUCHSCREEN_ROLL % (int(x), int(y)), **kwargs
            ),
        )

    def sh_input_stylus_swipe(self, x0, y0, x1, y1, t=1.0, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_INPUT_STYLUS_SWIPE
            % (int(x0), int(y0), int(x1), int(y1), int(t * 1000)),
            **kwargs,
        )

    def sh_input_stylus_drag_and_drop(self, x0, y0, x1, y1, t=1.0, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_INPUT_STYLUS_DRAGANDDROP
            % (int(x0), int(y0), int(x1), int(y1), int(t * 1000)),
            **kwargs,
        )

    def sh_input_stylus_roll(self, x, y, **kwargs):
        return (
            self.execute_sh_command(
                ADB_SHELL_INPUT_STYLUS_ROLL % (int(x), int(y)), **kwargs
            ),
        )

    def sh_input_trackball_swipe(self, x0, y0, x1, y1, t=1.0, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_INPUT_TRACKBALL_SWIPE
            % (int(x0), int(y0), int(x1), int(y1), int(t * 1000)),
            **kwargs,
        )

    def sh_input_trackball_drag_and_drop(self, x0, y0, x1, y1, t=1.0, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_INPUT_TRACKBALL_DRAGANDDROP
            % (int(x0), int(y0), int(x1), int(y1), int(t * 1000)),
            **kwargs,
        )

    def sh_input_trackball_roll(self, x, y, **kwargs):
        return (
            self.execute_sh_command(
                ADB_SHELL_INPUT_TRACKBALL_ROLL % (int(x), int(y)), **kwargs
            ),
        )

    def sh_dumpsys_window(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_DUMPSYS_WINDOW, **kwargs)

    def sh_input_dpad_tap(self, x, y, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_INPUT_DPAD_TAP % (int(x), int(y)), **kwargs
        )

    def sh_input_keyboard_tap(self, x, y, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_INPUT_KEYBOARD_TAP % (int(x), int(y)), **kwargs
        )

    def sh_input_mouse_tap(self, x, y, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_INPUT_MOUSE_TAP % (int(x), int(y)), **kwargs
        )

    def sh_input_touchpad_tap(self, x, y, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_INPUT_TOUCHPAD_TAP % (int(x), int(y)), **kwargs
        )

    def sh_input_gamepad_tap(self, x, y, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_INPUT_GAMEPAD_TAP % (int(x), int(y)), **kwargs
        )

    def sh_input_touchnavigation_tap(self, x, y, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_INPUT_TOUCHNAVIGATION_TAP % (int(x), int(y)), **kwargs
        )

    def sh_input_joystick_tap(self, x, y, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_INPUT_JOYSTICK_TAP % (int(x), int(y)), **kwargs
        )

    def sh_input_touchscreen_tap(self, x, y, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_INPUT_TOUCHSCREEN_TAP % (int(x), int(y)), **kwargs
        )

    def sh_input_stylus_tap(self, x, y, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_INPUT_STYLUS_TAP % (int(x), int(y)), **kwargs
        )

    def sh_input_trackball_tap(self, x, y, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_INPUT_TRACKBALL_TAP % (int(x), int(y)), **kwargs
        )

    def sh_is_screen_locked(self, **kwargs):
        stdo, stde = self.sh_dumpsys_window(**kwargs)
        return b"mDreamingLockscreen=true" in b"".join(stdo)

    def sh_list_permission_groups(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_LIST_PERMISSION_GROUPS, **kwargs)

    def sh_resolve_activity(self, package, **kwargs):
        return self.execute_sh_command(ADB_SHELL_RESOLVE_ACTIVITY % package, **kwargs)

    def sh_resolve_activity_brief(self, package, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_RESOLVE_ACTIVITY_BRIEF % package, **kwargs
        )

    def sh_expand_notifications(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_EXPAND_NOTIFICATIONS, **kwargs)

    def sh_expand_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_EXPAND_SETTINGS, **kwargs)

    def sh_start_package(self, package, **kwargs):
        return self.execute_sh_command(ADB_SHELL_START_PACKAGE % package, **kwargs)

    def sh_get_resolution(self, **kwargs):
        try:
            width, height = [
                [int(g[0][0]), int(g[0][1])]
                for x in self.execute_sh_command(ADB_SHELL_DUMPSYS_WINDOW, **kwargs)[0]
                if (g := screenres_reg_cur.findall(x))
            ][0]
        except Exception:
            width, height = [
                [int(g[0][0]), int(g[0][1])]
                for x in self.sh_get_wm_size(**kwargs)[0]
                if (g := screenres_reg.findall(x))
            ][0]
        return width, height

    def sh_change_display_orientation(self, new_orientation=1, timeout=5, **kwargs):
        orientierung = self.sh_get_display_orientation(**kwargs)

        if new_orientation == "horizontal_upside_down" or new_orientation == 2:
            format_einfuegen = 2

        elif new_orientation == "vertical" or new_orientation == 1:
            format_einfuegen = 1

        elif new_orientation == "horizontal" or new_orientation == 0:
            format_einfuegen = 0

        elif new_orientation == "vertical_upside_down" or new_orientation == 3:
            format_einfuegen = 3
        else:
            format_einfuegen = 0
        timeoutfinal = timeout + time.time()
        while orientierung != format_einfuegen:
            if time.time() > timeoutfinal:
                break
            cmds = f"""content insert --uri content://settings/system --bind name:s:accelerometer_rotation --bind value:i:0 && settings put system accelerometer_rotation 0 && content insert --uri content://settings/system --bind name:s:user_rotation --bind value:i:{format_einfuegen}"""
            stdo, stde = self.execute_sh_command(cmds, **kwargs)
            orientierung = self.sh_get_display_orientation(**kwargs)
        return orientierung

    def sh_do_random_actions(
        self,
        p=(),
        c=(),
        v=10,
        ignore_crashes=False,
        ignore_timeouts=False,
        ignore_security_exceptions=False,
        monitor_native_crashes=False,
        ignore_native_crashes=False,
        kill_process_after_error=False,
        hprof=False,
        match_description="",
        pct_touch=-1,
        pct_motion=-1,
        pct_trackball=-1,
        pct_syskeys=-1,
        pct_nav=-1,
        pct_majornav=-1,
        pct_appswitch=-1,
        pct_flip=-1,
        pct_anyevent=-1,
        pct_pinchzoom=-1,
        pct_permission=-1,
        pkg_blacklist_file="",
        pkg_whitelist_file="",
        wait_dbg=False,
        dbg_no_events=False,
        setup="",
        port=-1,
        s=-1,
        throttle_start=-1,
        throttle_end=-1,
        randomize_throttle=False,
        profile_wait=-1,
        device_sleep_time=-1,
        randomize_script=False,
        script_log=False,
        bugreport=False,
        periodic_bugreport=False,
        permission_target_system=False,
        **kwargs,
    ):
        command = ["monkey"]
        if p:
            if isinstance(p, str):
                p = [p]
            for pp in p:
                command.append(f"-p {pp}")
        if c:
            if isinstance(c, str):
                c = [c]
            for cc in c:
                command.append(f"-c {cc}")

        if ignore_crashes:
            command.append("--ignore-crashes")
        if ignore_timeouts:
            command.append("--ignore-timeouts")
        if ignore_security_exceptions:
            command.append("--ignore-security-exceptions")
        if monitor_native_crashes:
            command.append("--monitor-native-crashes")
        if ignore_native_crashes:
            command.append("--ignore-native-crashes")
        if kill_process_after_error:
            command.append("--kill-process-after-error")
        if hprof:
            command.append("--hprof")
        if match_description:
            command.append(f"--match-description {match_description}")
        if pct_touch > -1:
            command.append(f"--pct-touch {pct_touch}")
        if pct_motion > -1:
            command.append(f"--pct-motion {pct_motion}")
        if pct_trackball > -1:
            command.append(f"--pct-trackball {pct_trackball}")
        if pct_syskeys > -1:
            command.append(f"--pct-syskeys {pct_syskeys}")
        if pct_nav > -1:
            command.append(f"--pct-nav {pct_nav}")
        if pct_majornav > -1:
            command.append(f"--pct-majornav {pct_majornav}")
        if pct_appswitch > -1:
            command.append(f"--pct-appswitch {pct_appswitch}")
        if pct_flip > -1:
            command.append(f"--pct-flip {pct_flip}")
        if pct_anyevent > -1:
            command.append(f"--pct-anyevent {pct_anyevent}")
        if pct_pinchzoom > -1:
            command.append(f"--pct-pinchzoom {pct_pinchzoom}")
        if pct_permission > -1:
            command.append(f"--pct-permission {pct_permission}")

        if pkg_blacklist_file:
            command.append(f"--pkg-blacklist-file {pkg_blacklist_file}")
        if pkg_whitelist_file:
            command.append(f"--pkg-whitelist-file {pkg_whitelist_file}")
        if wait_dbg:
            command.append("--wait-dbg")
        if dbg_no_events:
            command.append("--dbg-no-events")
        if setup:
            command.append(f"--setup {setup}")
        if port > -1:
            command.append(f"--port {port}")
        if s > -1:
            command.append(f"-s {s}")
        command.append(f"-v {v}")
        if throttle_start > -1 or throttle_end > -1:
            command.append("--throttle")
            if throttle_start > -1:
                command.append(f"{throttle_start}")
            if throttle_end > -1:
                command.append(f"{throttle_end}")
        if randomize_throttle:
            command.append("--randomize-throttle")
        if profile_wait > -1:
            command.append(f"--profile-wait {profile_wait}")
        if device_sleep_time > -1:
            command.append(f"--device-sleep-time {device_sleep_time}")
        if randomize_script:
            command.append("--randomize-script")
        if script_log:
            command.append("--script-log")
        if bugreport:
            command.append("--bugreport")
        if periodic_bugreport:
            command.append("--periodic-bugreport")
        if permission_target_system:
            command.append("--permission-target-system")
        wholecommand = " ".join(command).strip()
        return self.execute_sh_command(wholecommand, **kwargs)

    def sh_netstat(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_NETSTAT, **kwargs)

    def sh_remove_user_cache(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_REMOVE_USER_CACHE, **kwargs)

    def sh_remove_dalvik_cache(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_REMOVE_DALVIK_CACHE, **kwargs)

    def sh_remove_data_cache(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_REMOVE_DATA_CACHE, **kwargs)

    def get_imei_android_14(self, **kwargs):
        r = self.execute_sh_command(ADB_IMEI_ANDROID14, **kwargs)[0]
        if r:
            return r[0]

    def sh_remount_all_rw(self, **kwargs):
        self.execute_sh_command(ADB_SHELL_REMOUNT_ALL_RW, **kwargs)
        cmd2 = ADB_SHELL_REMOUNT_ALL_RW.rstrip(" /")
        return [
            self.execute_sh_command(f"{cmd2} {y[0]} {y[2]}", **kwargs)
            for y in [
                x.decode("utf-8").split(maxsplit=3)
                for x in self.execute_sh_command(ADB_SHELL_MOUNT, **kwargs)[0]
            ]
        ]

    def sh_remount_all_ro(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_REMOUNT_ALL_RO, **kwargs)

    def sh_pm_dump(self, package, **kwargs):
        return self.execute_sh_command(ADB_SHELL_PM_DUMP % package, **kwargs)

    def sh_get_wm_size(self, **kwargs):
        so, se = self.execute_sh_command(ADB_SHELL_GET_WM_SIZE, **kwargs)

        return [int(y) for y in so[0].strip().split()[-1].decode("utf-8").split("x")]

    def sh_change_wm_size(self, width, height, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_CHANGE_WM_SIZE % (width, height), **kwargs
        )

    def sh_wm_reset_size(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_WM_RESET_SIZE, **kwargs)

    def sh_get_wm_density(self, **kwargs):
        so, se = self.execute_sh_command(ADB_SHELL_GET_WM_DENSITY, **kwargs)

        return int(so[0].strip().split()[-1].decode("utf-8"))

    def sh_change_wm_density(self, density, **kwargs):
        return self.execute_sh_command(ADB_SHELL_CHANGE_WM_DENSITY % density, **kwargs)

    def sh_wm_reset_density(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_WM_RESET_DENSITY, **kwargs)

    def sh_list_features(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_LIST_FEATURES, **kwargs)

    def sh_pwd(self, **kwargs):
        return (
            self.execute_sh_command(ADB_SHELL_PWD, **kwargs)[0][0]
            .strip()
            .decode("utf-8")
        )

    def sh_list_services(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_LIST_SERVICES, **kwargs)

    def sh_ps_a_t_l_z(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_PS_A_T_L_Z, **kwargs)

    def sh_open_url(self, url, **kwargs):
        return self.execute_sh_command(ADB_SHELL_OPEN_URL % format_url(url), **kwargs)

    def sh_get_ntp_server(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_GET_NTP_SERVER, **kwargs)

    def sh_set_ntp_server(self, server, **kwargs):
        return self.execute_sh_command(ADB_SHELL_SET_NTP_SERVER % server, **kwargs)

    def sh_pm_list_packages_f_i_u(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_PM_LIST_PACKAGES_F_I_U, **kwargs)

    def sh_pm_list_packages_3(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_PM_LIST_PACKAGES_3, **kwargs)

    def sh_pm_list_packages_s(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_PM_LIST_PACKAGES_S, **kwargs)

    def sh_mount(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_MOUNT, **kwargs)

    def sh_dumpsys_activity_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_DUMPSYS_ACTIVITY_SETTINGS, **kwargs)

    def sh_dumpsys_activity_allowed_associations(self, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_DUMPSYS_ACTIVITY_ALLOWED_ASSOCIATIONS, **kwargs
        )

    def sh_dumpsys_activity_intents(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_DUMPSYS_ACTIVITY_INTENTS, **kwargs)

    def sh_dumpsys_activity_broadcasts(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_DUMPSYS_ACTIVITY_BROADCASTS, **kwargs)

    def sh_dumpsys_activity_broadcast_stats(self, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_DUMPSYS_ACTIVITY_BROADCAST_STATS, **kwargs
        )

    def sh_dumpsys_activity_providers(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_DUMPSYS_ACTIVITY_PROVIDERS, **kwargs)

    def sh_dumpsys_activity_permissions(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_DUMPSYS_ACTIVITY_PERMISSIONS, **kwargs)

    def sh_dumpsys_activity_services(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_DUMPSYS_ACTIVITY_SERVICES, **kwargs)

    def sh_dumpsys_activity_recents(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_DUMPSYS_ACTIVITY_RECENTS, **kwargs)

    def sh_dumpsys_activity_lastanr(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_DUMPSYS_ACTIVITY_LASTANR, **kwargs)

    def sh_dumpsys_activity_starter(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_DUMPSYS_ACTIVITY_STARTER, **kwargs)

    def sh_dumpsys_activity_activities(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_DUMPSYS_ACTIVITY_ACTIVITIES, **kwargs)

    def sh_dumpsys_activity_exit_info(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_DUMPSYS_ACTIVITY_EXIT_INFO, **kwargs)

    def sh_dumpsys_activity_processes(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_DUMPSYS_ACTIVITY_PROCESSES, **kwargs)

    def sh_dumpsys_activity_lru(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_DUMPSYS_ACTIVITY_LRU, **kwargs)

    def sh_make_call(self, number, **kwargs):
        return self.execute_sh_command(ADB_SHELL_MAKE_CALL % number, **kwargs)

    def sh_still_image_camera(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_STILL_IMAGE_CAMERA, **kwargs)

    def sh_clear_package(self, package, **kwargs):
        return self.execute_sh_command(ADB_SHELL_CLEAR_PACKAGE % package, **kwargs)

    def sh_create_date_sorted_filelist(
        self, folder, outputfile, filefilter="*", **kwargs
    ):
        return self.execute_sh_command(
            ADB_SHELL_CREATE_DATE_SORTED_FILE_LIST
            % (folder, filefilter, outputfile, outputfile),
            **kwargs,
        )

    def sh_remove_file(self, path, **kwargs):
        return self.execute_sh_command(ADB_SHELL_REMOVE_FILE % path, **kwargs)

    def sh_disable_heads_up_notifications(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_DISABLE_NOTIFICATIONS, **kwargs)

    def sh_enable_heads_up_notifications(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_ENABLE_NOTIFICATIONS, **kwargs)

    def sh_screen_compat_on(self, package, **kwargs):
        return self.execute_sh_command(ADB_SHELL_SCREEN_COMPAT_ON % package, **kwargs)

    def sh_screen_compat_off(self, package, **kwargs):
        return self.execute_sh_command(ADB_SHELL_SCREEN_COMPAT_OFF % package, **kwargs)

    def sh_list_users(self, **kwargs):
        return [
            x.decode("utf-8", "ignore").strip()
            for x in self.execute_sh_command(ADB_SHELL_LIST_USERS, **kwargs)[0]
            if b"{" in x
        ]

    def sh_rescan_one_media(self, path, **kwargs):
        return self.execute_sh_command(ADB_SHELL_RESCAN_ONE_MEDIA % path, **kwargs)

    def _press_keyevent(self, k, **kwargs):
        longpress = kwargs.get("longpress", False)

        if "longpress" in kwargs:
            del kwargs["longpress"]
        if longpress:
            self.execute_sh_command(f"input keyevent {k} --longpress", **kwargs)
        else:
            self.execute_sh_command(f"input keyevent {k}", **kwargs)

    def k_hide_keyboard(self, **kwargs):
        return self._press_keyevent("4", **kwargs)

    def k_app_switch(self, **kwargs):
        return self._press_keyevent("KEYCODE_APP_SWITCH", **kwargs)

    def k_brightness_down(self, **kwargs):
        return self._press_keyevent("KEYCODE_BRIGHTNESS_DOWN", **kwargs)

    def k_brightness_up(self, **kwargs):
        return self._press_keyevent("KEYCODE_BRIGHTNESS_UP", **kwargs)

    def k_contacts(self, **kwargs):
        return self._press_keyevent("KEYCODE_CONTACTS", **kwargs)

    def k_copy(self, **kwargs):
        return self._press_keyevent("KEYCODE_COPY", **kwargs)

    def k_cut(self, **kwargs):
        return self._press_keyevent("KEYCODE_CUT", **kwargs)

    def k_home(self, **kwargs):
        return self._press_keyevent("KEYCODE_HOME", **kwargs)

    def k_page_down(self, **kwargs):
        return self._press_keyevent("KEYCODE_PAGE_DOWN", **kwargs)

    def k_page_up(self, **kwargs):
        return self._press_keyevent("KEYCODE_PAGE_UP", **kwargs)

    def k_paste(self, **kwargs):
        return self._press_keyevent("KEYCODE_PASTE", **kwargs)

    def k_power(self, **kwargs):
        return self._press_keyevent("KEYCODE_POWER", **kwargs)

    def k_search(self, **kwargs):
        return self._press_keyevent("KEYCODE_SEARCH", **kwargs)

    def k_sleep(self, **kwargs):
        return self._press_keyevent("KEYCODE_SLEEP", **kwargs)

    def k_tab(self, **kwargs):
        return self._press_keyevent("KEYCODE_TAB", **kwargs)

    def k_volume_down(self, **kwargs):
        return self._press_keyevent("KEYCODE_VOLUME_DOWN", **kwargs)

    def k_volume_up(self, **kwargs):
        return self._press_keyevent("KEYCODE_VOLUME_UP", **kwargs)

    def k_volume_mute(self, **kwargs):
        return self._press_keyevent("KEYCODE_VOLUME_MUTE", **kwargs)

    def k_wakeup(self, **kwargs):
        return self._press_keyevent("KEYCODE_WAKEUP", **kwargs)

    #
    def sh_get_display_orientation(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_GET_USER_ROTATION, **kwargs)[0][
            0
        ].strip()

    def sh_open_date_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_DATE_SETTINGS, **kwargs)

    def sh_open_application_development_settings(self, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_APPLICATION_DEVELOPMENT_SETTINGS, **kwargs
        )

    def sh_open_location_source_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_LOCATION_SOURCE_SETTINGS, **kwargs)

    def sh_open_memory_card_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_MEMORY_CARD_SETTINGS, **kwargs)

    def sh_open_locale_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_LOCALE_SETTINGS, **kwargs)

    def sh_open_search_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_SEARCH_SETTINGS, **kwargs)

    def sh_open_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_SETTINGS, **kwargs)

    def sh_open_account_sync_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_ACCOUNT_SYNC_SETTINGS, **kwargs)

    def sh_open_display_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_DISPLAY_SETTINGS, **kwargs)

    def sh_open_input_method_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_INPUT_METHOD_SETTINGS, **kwargs)

    def sh_open_sound_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_SOUND_SETTINGS, **kwargs)

    def sh_open_wifi_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_WIFI_SETTINGS, **kwargs)

    def sh_open_application_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_APPLICATION_SETTINGS, **kwargs)

    def sh_open_account_sync_settings_add_account(self, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_ACCOUNT_SYNC_SETTINGS_ADD_ACCOUNT, **kwargs
        )

    def sh_open_manage_applications_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_MANAGE_APPLICATIONS_SETTINGS, **kwargs)

    def sh_open_sync_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_SYNC_SETTINGS, **kwargs)

    def sh_open_dock_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_DOCK_SETTINGS, **kwargs)

    def sh_open_add_account_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_ADD_ACCOUNT_SETTINGS, **kwargs)

    def sh_open_security_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_SECURITY_SETTINGS, **kwargs)

    def sh_open_device_info_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_DEVICE_INFO_SETTINGS, **kwargs)

    def sh_open_wireless_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_WIRELESS_SETTINGS, **kwargs)

    def sh_open_system_update_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_SYSTEM_UPDATE_SETTINGS, **kwargs)

    def sh_open_manage_all_applications_settings(self, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_MANAGE_ALL_APPLICATIONS_SETTINGS, **kwargs
        )

    def sh_open_data_roaming_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_DATA_ROAMING_SETTINGS, **kwargs)

    def sh_open_apn_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_APN_SETTINGS, **kwargs)

    def sh_open_user_dictionary_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_USER_DICTIONARY_SETTINGS, **kwargs)

    def sh_open_voice_input_output_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_VOICE_INPUT_OUTPUT_SETTINGS, **kwargs)

    def sh_open_tts_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_TTS_SETTINGS, **kwargs)

    def sh_open_wifi_ip_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_WIFI_IP_SETTINGS, **kwargs)

    def sh_open_web_search_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_WEB_SEARCH_SETTINGS, **kwargs)

    def sh_open_bluetooth_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_BLUETOOTH_SETTINGS, **kwargs)

    def sh_open_airplane_mode_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_AIRPLANE_MODE_SETTINGS, **kwargs)

    def sh_open_internal_storage_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_INTERNAL_STORAGE_SETTINGS, **kwargs)

    def sh_open_accessibility_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_ACCESSIBILITY_SETTINGS, **kwargs)

    def sh_open_quick_launch_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_QUICK_LAUNCH_SETTINGS, **kwargs)

    def sh_open_privacy_settings(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_PRIVACY_SETTINGS, **kwargs)

    def sh_touch(self, path, **kwargs):
        folderpath = "/".join(path.split("/")[:-1])
        self.sh_mkdir(folderpath, **kwargs)
        return self.execute_sh_command(
            ADB_SHELL_TOUCH % strip_quotes_and_escape(path), **kwargs
        )

    def sh_rename(self, src, dst, **kwargs):
        return self.execute_sh_command(ADB_SHELL_RENAME_FILE % (src, dst), **kwargs)

    def sh_mkdir(self, path, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_MKDIR % strip_quotes_and_escape(path), **kwargs
        )

    def sh_is_folder(self, path, **kwargs):
        result, stde = self.execute_sh_command(ADB_SHELL_IS_FOLDER % path, **kwargs)
        isfolder = False
        try:
            if re.findall(rb"^\d+\s+\d+\s+d", result[0])[0]:
                isfolder = True
        except Exception:
            pass
        return isfolder

    def sh_is_file(self, path, **kwargs):
        return bool(
            int(
                self.execute_sh_command(ADB_SHELL_IS_FILE % path, **kwargs)[0][
                    0
                ].strip()
            )
        )

    def sh_swipe(self, x0, y0, x1, y1, t, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_SWIPE % (int(x0), int(y0), int(x1), int(y1), int(t * 1000)),
            **kwargs,
        )

    def sh_sort_file_reverse(self, file, **kwargs):
        return self.execute_sh_command(ADB_SHELL_SORT_FILE_REVERSE % (file,), **kwargs)

    def sh_sort_file(self, file, **kwargs):
        return self.execute_sh_command(ADB_SHELL_SORT_FILE % (file,), **kwargs)

    def sh_file_exists(self, path, **kwargs):
        stdout, stderr = self.execute_sh_command(ADB_SHELL_PATH_EXISTS % path, **kwargs)
        return bool(int(stdout[0].strip().decode("utf-8")))

    def copy_folder_to_other_location(self, src, dst):
        src = "/" + src.strip("/") + "/"
        dst = "/" + dst.strip("/") + "/"
        stdout1, stderr1 = self.execute_sh_command(f"mkdir -p {dst}")
        stdout2, stderr2 = self.execute_sh_command(
            f"(cd {src}; tar cf - .) | (cd {dst}; tar xvf -)"
        )
        stdoutall = self._all_outputlist_to_one(stdout1, stdout2)
        stderrall = self._all_outputlist_to_one(stderr1, stderr2)
        return [stdoutall, stderrall]

    def get_all_keyboards(self):
        return [
            x.strip().decode("utf-8")
            for x in self.execute_sh_command(ADB_SHELL_ALL_KEYBOARDS)[0]
        ]

    def install_adb_keyboard(
        self,
        url=r"https://github.com/senzhk/ADBKeyBoard/raw/master/ADBKeyboard.apk",
        **kwargs,
    ):
        purefile, filename, removefu = get_tmpfile(".apk")

        with requests.get(url) as r:
            keyb = r.content
            if r.status_code != 200:
                raise Exception(f"Could not download ADBKeyboard.apk from {url}")
            with open(filename, mode="wb") as f:
                f.write(keyb)
        kwargs = kwargs.copy()
        kwargs.update(invisibledict)
        subprocess.run(
            f"{self.adb_path} -s {self.device_serial} install {filename}",
            **kwargs,
        )

        while True:
            try:
                removefu()
                break
            except Exception:
                sleep(1)
                continue

    def get_active_keyboard(self, **kwargs):
        return (
            self.execute_sh_command(ADB_GET_DEFAULT_KEYBOARD, **kwargs)[0][0]
            .strip()
            .decode("utf-8")
        )

    def disable_keyboard(self, **kwargs):
        activekeyboard = self.get_active_keyboard(**kwargs)
        return self.execute_sh_command(
            ADB_DISABLE_KEYBOARD % activekeyboard,
            **kwargs,
        )

    def enable_keyboard(
        self, keyboard="com.android.inputmethod.latin/.LatinIME", **kwargs
    ):
        stdout1, stderr1 = self.execute_sh_command(
            ADB_ENABLE_KEYBOARD % keyboard, **kwargs
        )
        stdout2, stderr2 = self.execute_sh_command(
            ADB_SET_KEYBOARD % keyboard, **kwargs
        )
        allstdout = self._all_outputlist_to_one(
            stdout1,
            stdout2,
        )
        allstderr = self._all_outputlist_to_one(
            stderr1,
            stderr2,
        )
        return allstdout, allstderr

    def enable_adbkeyboard(self, **kwargs):
        return self.enable_keyboard(ADB_KEYBOARD_NAME, **kwargs)

    def is_keyboard_shown(self, **kwargs):
        q = b"".join(self.execute_sh_command(ADB_IS_KEYBOARD_SHOWN, **kwargs)[0])
        if b"mInputShown=true" in q:
            return True
        return False

    def input_text_adbkeyboard(self, text, **kwargs):
        charsb64 = base64.b64encode(text.encode("utf-8")).decode()
        return self.execute_sh_command(ADB_KEYBOARD_COMMAND % charsb64, **kwargs)

    def input_text(
        self,
        text,
        remove_accents=False,
        sleep_after_letter=(0, 0),
        input_device: valid_input_devices = "",
        **kwargs,
    ):
        if remove_accents:
            text = remove_accents_from_text(text)
        stdoutlist = []
        stderrlist = []
        splitext = split_text_in_chars_or_parts(text, sleep_after_letter)
        for c in splitext:
            cmd2send = format_input_command(input_device, action="text", command=c)

            stdout, stderr = self.execute_sh_command(
                cmd2send,
                **kwargs,
            )
            stdoutlist.extend(stdout)
            stderrlist.extend(stderr)
            sleep_random_time(sleep_after_letter)
        return [stdoutlist, stderrlist]

    def sh_input_dpad_text(self, text, sleeptime=(0.0, 0.0), remove_accents=False):
        return (
            self.input_text(
                text,
                sleeptime=sleeptime,
                remove_accents=remove_accents,
                input_device="dpad",
            ),
        )

    def sh_input_keyboard_text(self, text, sleeptime=(0.0, 0.0), remove_accents=False):
        return (
            self.input_text(
                text,
                sleeptime=sleeptime,
                remove_accents=remove_accents,
                input_device="keyboard",
            ),
        )

    def sh_input_mouse_text(self, text, sleeptime=(0.0, 0.0), remove_accents=False):
        return (
            self.input_text(
                text,
                sleeptime=sleeptime,
                remove_accents=remove_accents,
                input_device="mouse",
            ),
        )

    def sh_input_touchpad_text(self, text, sleeptime=(0.0, 0.0), remove_accents=False):
        return (
            self.input_text(
                text,
                sleeptime=sleeptime,
                remove_accents=remove_accents,
                input_device="touchpad",
            ),
        )

    def sh_input_gamepad_text(self, text, sleeptime=(0.0, 0.0), remove_accents=False):
        return (
            self.input_text(
                text,
                sleeptime=sleeptime,
                remove_accents=remove_accents,
                input_device="gamepad",
            ),
        )

    def sh_input_touchnavigation_text(
        self, text, sleeptime=(0.0, 0.0), remove_accents=False
    ):
        return self.input_text(
            text,
            sleeptime=sleeptime,
            remove_accents=remove_accents,
            input_device="touchnavigation",
        )

    def sh_input_joystick_text(self, text, sleeptime=(0.0, 0.0), remove_accents=False):
        return (
            self.input_text(
                text,
                sleeptime=sleeptime,
                remove_accents=remove_accents,
                input_device="joystick",
            ),
        )

    def sh_input_touchscreen_text(
        self, text, sleeptime=(0.0, 0.0), remove_accents=False
    ):
        return (
            self.input_text(
                text,
                sleeptime=sleeptime,
                remove_accents=remove_accents,
                input_device="touchscreen",
            ),
        )

    def sh_input_stylus_text(self, text, sleeptime=(0.0, 0.0), remove_accents=False):
        return (
            self.input_text(
                text,
                sleeptime=sleeptime,
                remove_accents=remove_accents,
                input_device="stylus",
            ),
        )

    def sh_input_trackball_text(self, text, sleeptime=(0.0, 0.0), remove_accents=False):
        return (
            self.input_text(
                text,
                sleeptime=sleeptime,
                remove_accents=remove_accents,
                input_device="trackball",
            ),
        )

    def pull_folder(self, src, dst, **kwargs):
        kwargs.update({"disable_print_stdout": True, "wait_to_complete": 2})
        su = kwargs.get("su", False)
        if "su" in kwargs:
            del kwargs["su"]
        if not su:
            s1, s2 = self.execute_sh_command(f"(cd {src}; tar cf - .)", **kwargs)
        else:
            s1, s2 = self.execute_sh_command(
                f"(su -- cd {src}; su -- tar cf - .)", **kwargs
            )

        repla = self.format_output(s1)
        tar_data_bytes_io = io.BytesIO(repla)
        os.makedirs(dst, exist_ok=True)
        with tarfile.open(fileobj=tar_data_bytes_io, mode="r:") as tar:
            tar.extractall(path=dst)

    def sh_awk_calculator(self, expr, **kwargs):
        return float(
            self.execute_sh_command(ADB_SHELL_AWK_CALCULATOR % expr, **kwargs)[0][
                0
            ].strip()
        )

    import re

    def sh_all_full_file_path_from_dir(self, folder, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_PURE_ABS_PATH_OF_FILES % folder, **kwargs
        )

    def sh_pull_folder_with_cat(self, src, dst, **kwargs):
        folder2copy = "/" + src.strip("/ ") + "/"
        outfolder = dst.rstrip("/\\ ")

        so, se = self.sh_all_full_file_path_from_dir(folder2copy, **kwargs)
        for fi in so:
            try:
                file = fi.strip().decode("utf-8", "backslashreplace")
                shorterpath = file[len(folder2copy) :]
                outfol = os.path.normpath(
                    os.path.join(
                        outfolder, re.sub(r"[\\/]+", f"{os.sep}{os.sep}", shorterpath)
                    )
                )
                touch(outfol)
                catfi = self.sh_cat_file(file, **kwargs)
                with open(outfol, mode="wb") as fx:
                    fx.write(catfi)
            except Exception as fe:
                sys.stderr.write(f"\n{fe}\n")
                sys.stderr.flush()

    def sh_get_treeview_of_folder(self, folder, **kwargs):
        if "print_stdout" not in kwargs:
            kwargs["print_stdout"] = False
        if "print_stderr" not in kwargs:
            kwargs["print_stderr"] = False

        s1, s2 = self.execute_sh_command(ADB_SHELL_GET_TREEVIEW % folder, **kwargs)
        s1 = [x.decode("utf-8", "backslashreplace").strip() for x in s1]
        return s1

    def sh_get_lines_from_to_in_file(self, start, end, path, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_GET_LINES_IN_FILE % (int(start), int(end), path), **kwargs
        )

    def sh_get_specific_line_from_a_file(self, no, path, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_SPECIFIC_LINE_IN_FILE % (int(no), path), **kwargs
        )

    def sh_remove_specific_line_from_a_file(self, no, path, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_REMOVE_SPECIFIC_LINE_IN_FILE % (int(no), path), **kwargs
        )

    def chmod_all_files_in_folder(self, path, chmod, **kwargs):
        # newpath = strip_quotes_and_escape(path)
        return self.execute_sh_command(
            ADB_SHELL_CHMOD_ALL_FILES_IN_FOLDER % (path, int(chmod)), **kwargs
        )

    def sh_count_network_connections(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_COUNT_NETWORK_CONNECTIONS, **kwargs)

    def sh_mkdir_and_cd(self, path, **kwargs):
        return self.execute_sh_command(ADB_SHELL_CREATE_DICT_AND_CD % (path,), **kwargs)

    def sh_get_all_chmod_from_files_in_folder(self, folder, **kwargs):
        foldernew = folder.strip("/")
        return self.execute_sh_command(
            ADB_SHELL_GET_ALL_CHMOD_IN_FOLDER.replace("REPLACE_FOLDER", foldernew),
            **kwargs,
        )

    def sh_list_all_connected_ips(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_ALL_CONNECTED_IPS, **kwargs)

    def sh_get_bios_info(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_GET_BIOS_INFORMATION, **kwargs)

    def sh_wait_until_file_written_to_disk(self, file, interval, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_CHECK_FILESIZE
            + f"\ncheck_if_finished_writing {file} {interval}\n",
            **kwargs,
        )

    def sh_ls_human_readable(self, folder, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_FILE_LISTING_HUMAN_READABLE.replace("REPLACEDIR", folder),
            **kwargs,
        )

    def sh_find_all_folder_full_path(self, folder, **kwargs):
        return self.execute_sh_command(ADB_SHELL_FIND_FULL_FILEPATH % folder, **kwargs)

    def sh_check_environment_vars(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_CHECK_ENVIRONMENT_VARS, **kwargs)

    def sh_printenv(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_PRINTENV, **kwargs)

    def sh_freeze_proc(self, pid, **kwargs):
        return self.execute_sh_command(ADB_SHELL_FREEZE_PROC % str(int(pid)), **kwargs)

    def sh_unfreeze_proc(self, pid, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_UNFREEZE_PROC % str(int(pid)), **kwargs
        )

    def sh_hexdump(self, file, **kwargs):
        return self.execute_sh_command(ADB_SHELL_HEXDUMP % file, **kwargs)

    def sh_count_lines_in_file(self, file, **kwargs):
        stdo, stde = self.execute_sh_command(
            ADB_SHELL_COUNT_LINES_IN_FILE % file, **kwargs
        )
        fire = []
        for std in stdo:
            q, v = std.split(maxsplit=1)
            q = int(q)
            v = v.strip()
            fire.extend([q, v])
        return fire

    def sh_reverse_file(self, file, **kwargs):
        return self.execute_sh_command(ADB_SHELL_REVERSE_FILE % file, **kwargs)

    def sh_comment_out_line_in_file(self, n, file, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_COMMENT_OUT_LINE_IN_FILE % (n, file), **kwargs
        )

    def sh_tar_backup_of_folder_to_sdcard(
        self, foldertobackup, outputfolder="/sdcard/", **kwargs
    ):
        foldertobackup2 = strip_quotes_and_escape(foldertobackup)
        foldertobackupn = re.sub(r"\W+", "_", foldertobackup).strip("_")
        return self.execute_sh_command(
            f"""filename={outputfolder}{foldertobackupn}$(date "+%Y%m%d_%H%M%S").tar.gz\necho "$filename"\ntar -czvvf "$filename" {foldertobackup2}""",
            **kwargs,
        )

    def sh_ls_folder(self, folder="", **kwargs):
        return self.execute_sh_command(ADB_SHELL_LS_FOLDER % folder, **kwargs)

    def sh_ls_fp(self, folder="", **kwargs):
        if folder:
            folder = "cd " + folder
        return self.execute_sh_command(
            ADB_SHELL_LS_FULL_PATH.replace("REPLACE_PATH", folder), **kwargs
        )

    def sh_get_md5_for_all_files(self, folder="", **kwargs):
        if folder:
            folder = "cd " + folder
        return self.execute_sh_command(
            ADB_SHELL_MD5_HASHES_FROM_ALL_FILES.replace("REPLACE_PATH", folder),
            **kwargs,
        )

    def sh_delete_all_files_in_folder_except_newest(self, folder="", **kwargs):
        if folder:
            folder = "cd " + folder
        return self.execute_sh_command(
            ADB_SHELL_DELETE_ALL_FILES_IN_FOLDER_EXCEPT_NEWEST.replace(
                "REPLACE_PATH", folder
            ),
            **kwargs,
        )

    def sh_list_extensions_in_folder(self, folder="", **kwargs):
        if folder:
            folder = "cd " + folder
        return self.execute_sh_command(
            ADB_SHELL_LIST_ALL_EXTENSIONS_IN_FOLDER.replace("REPLACE_PATH", folder),
            **kwargs,
        )

    def sh_ls_size(self, folder="", **kwargs):
        if folder:
            folder = "cd " + folder
        return self.execute_sh_command(
            ADB_LS_BY_FILESIZE.replace("REPLACE_PATH", folder), **kwargs
        )

    def sh_ls_by_mod_date(self, folder="", **kwargs):
        # path = strip_quotes_and_escape(folder)
        if folder:
            folder = "cd " + folder + "\n"
        return self.execute_sh_command(
            ADB_SHELL_LS_SORT_BY_MOD_DATE.replace("REPLACE_PATH", folder), **kwargs
        )

    def sh_iptables(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_IPTABLES, **kwargs)

    def sh_get_kernel_infos(self, **kwargs):
        return re.split(
            r"^\s*$",
            b"".join(
                self.execute_sh_command(
                    ADB_SHELL_KERNEL_INFOS,
                    **kwargs,
                )[0]
            )
            .strip()
            .decode("utf-8", "backslashreplace"),
        )

    def sh_get_ip_from_host(self, url, **kwargs):
        stdo, stde = self.execute_sh_command(ADB_SHELL_GET_IP_FROM_HOST % url, **kwargs)
        if stdo:
            return stdo[0].strip().decode("utf-8", "backslashreplace")

    def sh_newest_file_in_folder(self, folder, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_NEWEST_FILE_IN_FOLDER % folder, **kwargs
        )

    def sh_show_ips(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_GET_IPS, **kwargs)

    def sh_print_file_with_linenumbers(self, file, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_PRINT_FILE_WITH_LINENUMBERS % file, **kwargs
        )

    def sh_abs_value_of_number(self, number, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_ABS_VALUE_OF_NUMBER % (int(number),), **kwargs
        )

    def sh_get_details_from_pid(self, pid, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_GET_DETAILS_FROM_PROCESS % (int(pid),), **kwargs
        )

    def sh_netstat_tlnp(self):
        return [
            g
            for x in self.execute_sh_command(ADB_SHELL_NETSTAT_TLNP)[0]
            if len(g := (x.strip().split(maxsplit=6))) == 7
            and re.search(rb"^\d+", g[1])
        ]

    def sh_get_details_with_lsof(self, **kwargs):
        return self.execute_sh_command(ADB_GET_DETAILS_FROM_ALL_PROCS, **kwargs)

    def sh_kill_process_that_is_locking_a_file(self, file, **kwargs):
        return self.execute_sh_command(
            ADB_KILL_A_PROCESS_THAT_IS_LOCKING_A_FILE % file, **kwargs
        )

    def sh_print_lines_of_file_with_at_least_length_n(self, file, n, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_PRINT_LINES_LONGER_THAN % (int(n), file), **kwargs
        )

    def sh_show_folders_in_PATH(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_FOLDER_IN_PATH_VAR, **kwargs)

    def sh_compare_2_files(self, file1, file2, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_COMPARE_2_FILES % (file1, file2), **kwargs
        )

    def sh_substring_from_string(self, string, start, end, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_SUBSTRING_FROM_STRING % (string, start, end - start), **kwargs
        )

    def sh_rm_dry_run(self, args, **kwargs):
        return self.execute_sh_command(ADB_SHELL_RM_DRY_RUN % (args,), **kwargs)

    def sh_ipv4_interfaces(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_IPV4_INTERFACES, **kwargs)

    def sh_list_procs_cpu_usage(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_LIST_PROCS_CPU_USAGE, **kwargs)

    def sh_list_current_running_procs(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_CURRENT_RUNNING_PROCESSES, **kwargs)

    def sh_get_interfaces_and_mac(self, **kwargs):
        so, se = self.execute_sh_command(ADB_SHELL_INTERFACES_AND_MAC, **kwargs)
        out = [
            g.decode("utf-8", "backslashreplace").split(maxsplit=1)
            for x in so
            if (g := x.strip())
        ]
        return out

    def sh_list_files_newest_first(self, folder, **kwargs):
        so, se = self.execute_sh_command(
            ADB_SHELL_FILES_IN_FOLDER_NEWEST_FIRST % folder, **kwargs
        )
        return [
            y
            for y in [
                x.decode("utf-8", "backslashreplace").strip().split(maxsplit=6)
                for x in so
            ]
            if len(y) == 7
        ]

        v = (
            ("capture_stdout_stderr_first", True),
            ("global_cmd", False),
            ("wait_to_complete", 0.1),
        )

    def sh_upperstring_to_lowerstring(self, s, **kwargs):
        return self.execute_sh_command(ADB_SHELL_UPPER_TO_LOWER % (s,), **kwargs)

    def sh_calculate_size_of_folders(self, folder, **kwargs):
        if folder:
            folder = "cd " + folder
        size = self.execute_sh_command(
            ADB_SHELL_SIZE_OF_FOLDERS.replace("REPLACE_PATH", folder), **kwargs
        )
        return [
            (int(g[0]), g[1])
            for x in size[0]
            if len(g := x.strip().split(maxsplit=1)) == 2
        ]

    def sh_number_of_cpus(self, **kwargs):
        return int(
            self.execute_sh_command(ADB_SHELL_NUMBER_OF_CPUS, **kwargs)[0][0].strip()
        )

    def sh_get_internal_ip_addr(self, **kwargs):
        so, se = self.execute_sh_command(ADB_SHELL_GET_INTERNAL_IPS, **kwargs)
        return [g.decode("utf-8", "backslashreplace") for x in so if (g := x.strip())]

    def sh_get_external_ip(self, **kwargs):
        so, se = self.execute_sh_command(ADB_SHELL_GET_EXTERNAL_IP, **kwargs)
        if so:
            return so[0].strip().decode("utf-8", "backslashreplace")
        else:
            so, se = self.execute_sh_command(ADB_SHELL_GET_EXTERNAL_IP2, **kwargs)
            if so:
                return so[0].strip().decode("utf-8", "backslashreplace")

    def sh_get_all_mac_addresses(self, **kwargs):
        so, se = self.execute_sh_command(ADB_SHELL_GET_ALL_MAC_ADDRESSES, **kwargs)
        return [g.decode("utf-8", "backslashreplace") for x in so if (g := x.strip())]

    def sh_number_of_tcp_connections(self, **kwargs):
        return int(
            self.execute_sh_command(ADB_SHELL_NUMBER_OF_TCP_CONNECTIONS, **kwargs)[0][
                0
            ].strip()
        )

    def sh_append_line_to_file(self, line, file, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_APPEND_LINE_TO_FILE % (line, file), **kwargs
        )

    def sh_dump_all_db_files(self, as_pandas=False, **kwargs):
        return self._sh_dump_db_files(
            ADB_SHELL_DUMP_ALL_DB_FILES, as_pandas=as_pandas, **kwargs
        )

    def sh_dump_all_databases_in_data_data(self, as_pandas=False, **kwargs):
        return self._sh_dump_db_files(
            ADB_SHELL_DUMP_ALL_DATABASES_IN_DATA_DATA, as_pandas=as_pandas, **kwargs
        )

    def sh_delete_files_in_folder_older_than(
        self, folder, file_filter="*", date_distance="+1", **kwargs
    ):
        return self.execute_sh_command(
            ADB_SHELL_DELETE_FILES_IN_FOLDER_OLDER_THAN.replace("REPLACEFOLDER", folder)
            .replace("REPLACEFILEFILTER", file_filter)
            .replace("REPLACEDISTANCE", date_distance),
            **kwargs,
        )

    def sh_get_newest_file_in_folder_as_tar(
        self, folder, file_filter="*", tarpath="/ssdcard/newestar.tar.gz", **kwargs
    ):
        return self.execute_sh_command(
            ADB_SHELL_GET_NEWEST_FILE_IN_FOLDER_AS_TAR.replace("REPLACEFOLDER", folder)
            .replace("REPLACEFILEFILTER", file_filter)
            .replace("REPLACETARPATH", tarpath),
            **kwargs,
        )

    def sh_disable_network_adapter(self, network, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_DISABLE_NETWORK_INTERFACE % network, **kwargs
        )

    def sh_get_linux_version(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_LINUX_VERSION, **kwargs)

    def sh_get_cpu_info(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_CPU_INFO, **kwargs)

    def sh_get_mem_info(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_MEM_INFO, **kwargs)

    def sh_whoami(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_WHOAMI, **kwargs)

    def sh_id(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_ID, **kwargs)

    def sh_get_user_groups(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_USER_GROUPS, **kwargs)

    def sh_get_filetype(self, file, **kwargs):
        return (
            self.execute_sh_command(ADB_SHELL_GET_FILETYPE % file, **kwargs)[0][0]
            .rsplit(b":", 1)[-1]
            .strip()
            .decode()
        )

        v = (
            ("su", True),
            ("global_cmd", False),
            ("wait_to_complete", 0),
            ("capture_stdout_stderr_first", False),
        )

    def sh_enable_network_adapter(self, network, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_ENABLE_NETWORK_INTERFACE % network, **kwargs
        )

    def _sh_dump_db_files(self, command, as_pandas=False, **kwargs):
        dbfiles = self.execute_sh_command(command, **kwargs)
        sleep(10)
        oldlen = -1
        while oldlen < len(dbfiles[0]):
            oldlen = len(dbfiles[0])
            print(dbfiles)
            sleep(10)

        dumpdata = [
            b"path,table," + g.split(b",", maxsplit=2)[-1]
            for q in re.split(
                rb"^\s*Dumping\s*data\s*from.*:\s*$",
                b"".join(dbfiles[0]).replace(self.exitcommand.encode("utf-8"), b""),
                flags=re.M,
            )
            if (g := q.strip())
        ]
        if as_pandas:
            try:
                pddfs = [
                    pd.read_csv(
                        io.StringIO(xx.decode("utf-8", "backslashreplace")),
                        header=0,
                        encoding="utf-8",
                        sep=",",
                        index_col=False,
                        encoding_errors="backslashreplace",
                        on_bad_lines="warn",
                        engine="python",
                    )
                    for xx in dumpdata
                ]
                return pddfs
            except Exception as e:
                sys.stderr.write(f"{e}\n")
        return dumpdata

    def sh_cat_file_join_newlines(self, file, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_CAT_FILE_JOIN_NEWLINES % file, **kwargs
        )

    def sh_check_open_ports(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_CHECK_OPEN_PORTS, **kwargs)

    def sh_show_touches(self, **kwargs):
        return self.execute_sh_command(ADB_SHOW_TOUCHES, **kwargs)

    def sh_show_touches_not(self, **kwargs):
        return self.execute_sh_command(ADB_SHOW_TOUCHES_NOT, **kwargs)

    def sh_count_files_in_folder(self, folder, **kwargs):
        folder = folder.rstrip("/") + "/"
        return int(
            self.execute_sh_command(ADB_SHELL_COUNT_FILES_IN_FOLDER % folder, **kwargs)[
                0
            ][0].strip()
        )

    def sh_list_input_devices(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_LIST_INPUT_DEVICES, **kwargs)

    def sh_get_sendevent_input_devices(self, **kwargs):
        so, se = self.execute_sh_command(
            ADB_SHELL_GET_SENDEVENT_INPUT_DEVICES, **kwargs
        )
        return [
            x.strip().decode("utf-8", "backslashreplace").split(maxsplit=1) for x in so
        ]

    def sh_list_dev_input(self, **kwargs):
        return [
            f"/dev/input/{x.decode().strip()}"
            for x in self.sh_ls_folder("/dev/input", **kwargs)[0]
        ]

    def sh_get_all_props(self, **kwargs):
        return [
            [y[0].strip(b"[] ").decode(), y[1].strip(b"[]\n ").decode()]
            for y in [
                x.split(b": ", maxsplit=1)
                for x in self.execute_sh_command(ADB_SHELL_GETPROPS, **kwargs)[0]
            ]
        ]

    def sh_get_all_dumpsys_services(self, **kwargs):
        return [
            q.decode().strip()
            for q in self.execute_sh_command(
                ADB_SHELL_GET_ALL_SERVICES_FOR_DUMPSYS, **kwargs
            )[0]
        ]

    def sh_dumpsys_everything(self, **kwargs):
        alli = []
        alls = self.sh_get_all_dumpsys_services(**kwargs)
        for a in alls:
            sleep(0.1)
            alli.append([a, self.execute_sh_command(f"dumpsys {a} 2>/dev/null")[0]])
        return alli

    def sh_get_all_extra_options_from_dumpsys(self, **kwargs):
        extraoptions = []

        alli = []
        alls = self.sh_get_all_dumpsys_services(**kwargs)
        allcommands = []
        for a in alls:
            sleep(0.1)
            alli.append([self.execute_sh_command(f"dumpsys {a} 2>/dev/null")], **kwargs)
            sleep(0.1)
            alli[-1].append(self.execute_sh_command(f"dumpsys {a} -h"), **kwargs)
            allcommands.append(a)
        i = -1
        for p1, p2 in alli:
            i += 1
            if p1 != p2:
                if b" options:" in b"".join(p2[0]):
                    extraoptions.append([allcommands[i], p2])
        return extraoptions

        v = (
            ("su", True),
            ("wait_to_complete", 0),
            ("capture_stdout_stderr_first", False),
        )

    def sh_get_file_extension(self, path, **kwargs):
        so, se = self.execute_sh_command(
            ADB_SHELL_GET_FILE_EXTENSION.replace("FILEPATH", path), **kwargs
        )
        if so:
            return so[0].strip().decode()

    def sh_test_directory(self, path, **kwargs):
        return bool(
            int(
                self.execute_sh_command(ADB_SHELL_TEST_DIRECTORY % path, **kwargs)[0][
                    0
                ].strip()
            )
        )

    def sh_test_exists_in_any_form(self, path, **kwargs):
        return bool(
            int(
                self.execute_sh_command(
                    ADB_SHELL_TEST_EXISTS_IN_ANY_FORM % path, **kwargs
                )[0][0].strip()
            )
        )

    def sh_test_executable(self, path, **kwargs):
        return bool(
            int(
                self.execute_sh_command(ADB_SHELL_TEST_EXECUTABLE % path, **kwargs)[0][
                    0
                ].strip()
            )
        )

    def sh_test_regular_file(self, path, **kwargs):
        return bool(
            int(
                self.execute_sh_command(ADB_SHELL_TEST_REGULAR_FILE % path, **kwargs)[
                    0
                ][0].strip()
            )
        )

    def sh_test_readable(self, path, **kwargs):
        return bool(
            int(
                self.execute_sh_command(ADB_SHELL_TEST_READABLE % path, **kwargs)[0][
                    0
                ].strip()
            )
        )

    def sh_test_named_pipe(self, path, **kwargs):
        return bool(
            int(
                self.execute_sh_command(ADB_SHELL_TEST_NAMED_PIPE % path, **kwargs)[0][
                    0
                ].strip()
            )
        )

    def sh_test_block_device(self, path, **kwargs):
        return bool(
            int(
                self.execute_sh_command(ADB_SHELL_TEST_BLOCK_DEVICE % path, **kwargs)[
                    0
                ][0].strip()
            )
        )

    def sh_test_character_device(self, path, **kwargs):
        return bool(
            int(
                self.execute_sh_command(
                    ADB_SHELL_TEST_CHARACTER_DEVICE % path, **kwargs
                )[0][0].strip()
            )
        )

    def sh_test_link(self, path, **kwargs):
        return bool(
            int(
                self.execute_sh_command(ADB_SHELL_TEST_CHARACTER_LINK % path, **kwargs)[
                    0
                ][0].strip()
            )
        )

    def sh_cd_and_search_string_in_files(self, path, query, **kwargs):
        path = strip_quotes_and_escape(path)

        so, se = self.execute_sh_command(
            ADB_SHELL_GOTO_DIR_AND_SEARCH_FOR_STRING % (f"cd {path}", query), **kwargs
        )
        if so:
            return [g for x in so if len(g := x.strip().split(b":", maxsplit=2)) == 3]

    def sh_get_md5sum(self, path, **kwargs):
        so, se = self.execute_sh_command(ADB_SHELL_MD5SUM % path, **kwargs)
        if so:
            return so[0].strip().decode()

    def sh_realpath(self, path, **kwargs):
        so, se = self.execute_sh_command(ADB_SHELL_REALPATH % path, **kwargs)
        if so:
            return so[0].strip().decode()

    def sh_dirname(self, path, **kwargs):
        so, se = self.execute_sh_command(ADB_SHELL_DIRNAME % path, **kwargs)
        if so:
            return so[0].strip().decode()

    def sh_rename_file_to_md5(self, path, **kwargs):
        so, se = self.execute_sh_command(
            ADB_SHELL_RENAME_FILE_TO_MD5.replace("FINOPATH", path), **kwargs
        )
        if so:
            return so[0].strip().decode()

    def sh_get_size_of_terminal(self, **kwargs):
        so, se = self.execute_sh_command(ADB_SHELL_GET_SIZE_OF_TERMINAL, **kwargs)
        if so:
            return list(map(int, so[0].strip().split(b" x ")))

    def sh_get_file_with_tstamp(self, filename, ext, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_GET_FILE_WITH_TIMESTAMP.replace(
                "REPLACE_FILENAME", filename
            ).replace("REPLACE_EXT", ext),
            **kwargs,
        )

    def sh_disable_input_device(self, device, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_DISABLE_INPUT_DEVICE % device, **kwargs
        )

    def sh_memory_dump(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_SYSTEM_MEMORY_DUMP, **kwargs)

    def sh_get_cwd_of_procs(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_GET_CWD_OF_PROCS, **kwargs)

    def sh_get_install_date(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_GET_INSTALL_DATE, **kwargs)

    def sh_get_audio_playing_procs(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_GET_AUDIO_PLAYING_PROCS, **kwargs)

    def sh_get_procs_with_open_connections(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_PROCS_WITH_OPEN_CONNECTIONS, **kwargs)

    def sh_force_idle(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_FORCE_IDLE, **kwargs)

    def sh_unforce_idle(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_UNFORCE_IDLE, **kwargs)

    def sh_nice(self, cmd, value=-19, **kwargs):
        return self.execute_sh_command(ADB_UIAUTOMATOR_NICE20 % (value, cmd), **kwargs)

    def sh_get_current_focus(self, **kwargs):
        so, se = self.execute_sh_command(ADB_SHELL_CURRENT_FOCUS, **kwargs)
        try:
            return so[0].decode().strip()
        except Exception as e:
            sys.stderr.write(f"{e}")
            sys.stderr.flush()

    def sh_grep_proc_top(self, grep, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_TOP_ALL_PIDS_FROM_PROC_GREP.replace("REPLACEGREP", grep),
            **kwargs,
        )

    def sh_am_i_su(self, **kwargs):
        so, se = self.execute_sh_command(ADB_SHELL_AM_I_SU, **kwargs)
        if so:
            sostri = so[0].strip()
            return True if sostri == b"True" else False

    def sh_get_all_possible_activities(self, **kwargs):
        return b"".join(
            self.execute_sh_command(ADB_SHELL_GET_ALL_POSSIBLE_ACTIVITIES, **kwargs)[0][
                1:
            ]
        ).decode("utf-8")

    def sh_apps_using_internet(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_APPS_USING_INTERNET, **kwargs)

    def sh_chmod_x(self, file, **kwargs):
        return self.execute_sh_command(ADB_SHELL_CHMOD_X % file, **kwargs)

    def sh_execute_sh_script(self, file, **kwargs):
        return self.execute_sh_command(ADB_SHELL_EXECUTE_SH_SCRIPT % file, **kwargs)

    def sh_which_a(self, file, **kwargs):
        return self.execute_sh_command(ADB_SHELL_WHICH_A % file, **kwargs)

    def sh_type(self, file, **kwargs):
        return self.execute_sh_command(ADB_SHELL_TYPE % file, **kwargs)

    def sh_create_symbolic_link(self, src, dst, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_CREATE_SYMBOLIC_LINK % (src, dst), **kwargs
        )

    def sh_show_used_diskspace(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_SHOW_USED_DISKSPACE, **kwargs)

    def sh_show_used_memory(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_SHOW_USED_MEMORY, **kwargs)

    def sh_reboot(self, **kwargs):
        return self.execute_sh_command(ADB_SHELL_REBOOT, **kwargs)

    def sh_jobs(self, **kwargs):
        return [
            [int(u[0].strip()), (u[1].strip())]
            for u in (
                zip(
                    self.execute_sh_command(ADB_SHELL_JOBS_P, **kwargs)[0],
                    self.execute_sh_command(ADB_SHELL_JOBS, **kwargs)[0],
                )
            )
        ]

    def sh_goto_next_sibling_folder(self, **kwargs):
        so, se = self.execute_sh_command(ADB_SHELL_GOTO_NEXT_SIBLING_FOLDER, **kwargs)
        if so:
            return so[0].strip()

    def sh_chr(self, char, **kwargs):
        return self.execute_sh_command(
            ADB_SHELL_CHR.replace("REPLACE_CHAR", char), **kwargs
        )


add_printer(1)


this_folder = os.path.dirname(os.path.abspath(__file__))

add_printer(1)
link_uiautomator_dump_without_could_not_detect_idle_state = "https://github.com/hansalemaos/uiautomator_dump_without_could_not_detect_idle_state/raw/refs/heads/main/uiautomatorcpulimit.cpp"
link_uiautomator_dump_to_csv = "https://github.com/hansalemaos/uiautomator_dump_to_csv/raw/refs/heads/main/uiautomatornolimit.cpp"
link_sendevent_multicommands_type_text = "https://github.com/hansalemaos/sendevent_multicommands_type_text/raw/refs/heads/main/sendeventall.cpp"
link_mouse_sendevent_android = "https://github.com/hansalemaos/mouse_sendevent_android/raw/refs/heads/main/sendeventmouse.cpp"
link_getevent_keydumper_linux = "https://github.com/hansalemaos/getevent_keydumper_linux/raw/refs/heads/main/newgetevent.cpp"
link_getevent_pretty_print_linux = "https://github.com/hansalemaos/getevent_pretty_print_linux/raw/refs/heads/main/geteventall.cpp"
link_android_fragment_parser = "https://github.com/hansalemaos/android_fragment_parser/raw/refs/heads/main/fragmentdumper.cpp"
link_uiautomator_eventsparser_cpp = "https://github.com/hansalemaos/uiautomator_eventsparser_cpp/raw/refs/heads/main/eventparser.cpp"
link_lcp = "https://github.com/hansalemaos/lcp/raw/refs/heads/main/lcp.cpp"
# def download_cpp_files():
folder_uiautomator_dump_without_could_not_detect_idle_state = os.path.join(
    this_folder, "uiautomator_dump_without_could_not_detect_idle_state"
)
folder_uiautomator_dump_to_csv = os.path.join(this_folder, "uiautomator_dump_to_csv")
folder_sendevent_multicommands_type_text = os.path.join(
    this_folder, "sendevent_multicommands_type_text"
)
folder_mouse_sendevent_android = os.path.join(this_folder, "mouse_sendevent_android")
folder_getevent_keydumper_linux = os.path.join(this_folder, "getevent_keydumper_linux")
folder_getevent_pretty_print_linux = os.path.join(
    this_folder, "getevent_pretty_print_linux"
)
folder_android_fragment_parser = os.path.join(this_folder, "android_fragment_parser")
folder_uiautomator_eventsparser_cpp = os.path.join(
    this_folder, "uiautomator_eventsparser_cpp"
)
folder_lcp = os.path.join(this_folder, "lcp")
folder_getevent_keydumper_linux = os.path.join(this_folder, "getevent_keydumper_linux")
os.makedirs(folder_uiautomator_dump_without_could_not_detect_idle_state, exist_ok=True)
os.makedirs(folder_uiautomator_dump_to_csv, exist_ok=True)
os.makedirs(folder_sendevent_multicommands_type_text, exist_ok=True)
os.makedirs(folder_mouse_sendevent_android, exist_ok=True)
os.makedirs(folder_getevent_keydumper_linux, exist_ok=True)
os.makedirs(folder_getevent_pretty_print_linux, exist_ok=True)
os.makedirs(folder_android_fragment_parser, exist_ok=True)
os.makedirs(folder_uiautomator_eventsparser_cpp, exist_ok=True)
os.makedirs(folder_lcp, exist_ok=True)
os.makedirs(folder_getevent_keydumper_linux, exist_ok=True)
mappingdict = {
    " ": "KEY_SPACE:ud:%s",
    "!": "KEY_LEFTSHIFT:d:0#KEY_1:ud:%s#KEY_LEFTSHIFT:u:0",
    "'": "KEY_APOSTROPHE:ud:%s",
    '"': "KEY_LEFTSHIFT:d:0#KEY_APOSTROPHE:ud:%s#KEY_LEFTSHIFT:u:0",
    "#": "KEY_LEFTSHIFT:d:0#KEY_3:ud:%s#KEY_LEFTSHIFT:u:0",
    "$": "KEY_LEFTSHIFT:d:0#KEY_4:ud:%s#KEY_LEFTSHIFT:u:0",
    "%": "KEY_LEFTSHIFT:d:0#KEY_5:ud:%s#KEY_LEFTSHIFT:u:0",
    "&": "KEY_LEFTSHIFT:d:0#KEY_7:ud:%s#KEY_LEFTSHIFT:u:0",
    "(": "KEY_LEFTSHIFT:d:0#KEY_9:ud:%s#KEY_LEFTSHIFT:u:0",
    ")": "KEY_LEFTSHIFT:d:0#KEY_0:ud:%s#KEY_LEFTSHIFT:u:0",
    "*": "KEY_LEFTSHIFT:d:0#KEY_8:ud:%s#KEY_LEFTSHIFT:u:0",
    "+": "KEY_KPPLUS:ud:%s",
    ",": "KEY_COMMA:ud:%s",
    "-": "KEY_MINUS:ud:%s",
    ".": "KEY_DOT:ud:%s",
    "/": "KEY_SLASH:ud:%s",
    "0": "KEY_0:ud:%s",
    "1": "KEY_1:ud:%s",
    "2": "KEY_2:ud:%s",
    "3": "KEY_3:ud:%s",
    "4": "KEY_4:ud:%s",
    "5": "KEY_5:ud:%s",
    "6": "KEY_6:ud:%s",
    "7": "KEY_7:ud:%s",
    "8": "KEY_8:ud:%s",
    "9": "KEY_9:ud:%s",
    ":": "KEY_LEFTSHIFT:d:0#KEY_SEMICOLON:ud:%s#KEY_LEFTSHIFT:u:0",
    ";": "KEY_SEMICOLON:ud:%s",
    "<": "KEY_LEFTSHIFT:d:0#KEY_COMMA:ud:%s#KEY_LEFTSHIFT:u:0",
    "=": "KEY_EQUAL:ud:%s",
    ">": "KEY_LEFTSHIFT:d:0#KEY_DOT:ud:%s#KEY_LEFTSHIFT:u:0",
    "?": "KEY_QUESTION:ud:%s",
    "@": "KEY_LEFTSHIFT:d:0#KEY_2:ud:%s#KEY_LEFTSHIFT:u:0",
    "A": "KEY_LEFTSHIFT:d:0#KEY_A:ud:%s#KEY_LEFTSHIFT:u:0",
    "B": "KEY_LEFTSHIFT:d:0#KEY_B:ud:%s#KEY_LEFTSHIFT:u:0",
    "C": "KEY_LEFTSHIFT:d:0#KEY_C:ud:%s#KEY_LEFTSHIFT:u:0",
    "D": "KEY_LEFTSHIFT:d:0#KEY_D:ud:%s#KEY_LEFTSHIFT:u:0",
    "E": "KEY_LEFTSHIFT:d:0#KEY_E:ud:%s#KEY_LEFTSHIFT:u:0",
    "F": "KEY_LEFTSHIFT:d:0#KEY_F:ud:%s#KEY_LEFTSHIFT:u:0",
    "G": "KEY_LEFTSHIFT:d:0#KEY_G:ud:%s#KEY_LEFTSHIFT:u:0",
    "H": "KEY_LEFTSHIFT:d:0#KEY_H:ud:%s#KEY_LEFTSHIFT:u:0",
    "I": "KEY_LEFTSHIFT:d:0#KEY_I:ud:%s#KEY_LEFTSHIFT:u:0",
    "J": "KEY_LEFTSHIFT:d:0#KEY_J:ud:%s#KEY_LEFTSHIFT:u:0",
    "K": "KEY_LEFTSHIFT:d:0#KEY_K:ud:%s#KEY_LEFTSHIFT:u:0",
    "L": "KEY_LEFTSHIFT:d:0#KEY_L:ud:%s#KEY_LEFTSHIFT:u:0",
    "M": "KEY_LEFTSHIFT:d:0#KEY_M:ud:%s#KEY_LEFTSHIFT:u:0",
    "N": "KEY_LEFTSHIFT:d:0#KEY_N:ud:%s#KEY_LEFTSHIFT:u:0",
    "O": "KEY_LEFTSHIFT:d:0#KEY_O:ud:%s#KEY_LEFTSHIFT:u:0",
    "P": "KEY_LEFTSHIFT:d:0#KEY_P:ud:%s#KEY_LEFTSHIFT:u:0",
    "Q": "KEY_LEFTSHIFT:d:0#KEY_Q:ud:%s#KEY_LEFTSHIFT:u:0",
    "R": "KEY_LEFTSHIFT:d:0#KEY_R:ud:%s#KEY_LEFTSHIFT:u:0",
    "S": "KEY_LEFTSHIFT:d:0#KEY_S:ud:%s#KEY_LEFTSHIFT:u:0",
    "T": "KEY_LEFTSHIFT:d:0#KEY_T:ud:%s#KEY_LEFTSHIFT:u:0",
    "U": "KEY_LEFTSHIFT:d:0#KEY_U:ud:%s#KEY_LEFTSHIFT:u:0",
    "V": "KEY_LEFTSHIFT:d:0#KEY_V:ud:%s#KEY_LEFTSHIFT:u:0",
    "W": "KEY_LEFTSHIFT:d:0#KEY_W:ud:%s#KEY_LEFTSHIFT:u:0",
    "X": "KEY_LEFTSHIFT:d:0#KEY_X:ud:%s#KEY_LEFTSHIFT:u:0",
    "Y": "KEY_LEFTSHIFT:d:0#KEY_Y:ud:%s#KEY_LEFTSHIFT:u:0",
    "Z": "KEY_LEFTSHIFT:d:0#KEY_Z:ud:%s#KEY_LEFTSHIFT:u:0",
    "[": "KEY_LEFTBRACE:ud:%s",
    "\n": "KEY_ENTER:ud:%s",
    "\t": "KEY_TAB:ud:%s",
    "]": "KEY_RIGHTBRACE:ud:%s",
    "^": "KEY_LEFTSHIFT:d:0#KEY_6:ud:%s#KEY_LEFTSHIFT:u:0",
    "_": "KEY_LEFTSHIFT:d:0#KEY_MINUS:ud:%s#KEY_LEFTSHIFT:u:0",
    "`": "KEY_GRAVE:ud:%s",
    "a": "KEY_A:ud:%s",
    "b": "KEY_B:ud:%s",
    "c": "KEY_C:ud:%s",
    "d": "KEY_D:ud:%s",
    "e": "KEY_E:ud:%s",
    "f": "KEY_F:ud:%s",
    "g": "KEY_G:ud:%s",
    "h": "KEY_H:ud:%s",
    "i": "KEY_I:ud:%s",
    "j": "KEY_J:ud:%s",
    "k": "KEY_K:ud:%s",
    "l": "KEY_L:ud:%s",
    "m": "KEY_M:ud:%s",
    "n": "KEY_N:ud:%s",
    "o": "KEY_O:ud:%s",
    "p": "KEY_P:ud:%s",
    "q": "KEY_Q:ud:%s",
    "r": "KEY_R:ud:%s",
    "s": "KEY_S:ud:%s",
    "t": "KEY_T:ud:%s",
    "u": "KEY_U:ud:%s",
    "v": "KEY_V:ud:%s",
    "w": "KEY_W:ud:%s",
    "x": "KEY_X:ud:%s",
    "y": "KEY_Y:ud:%s",
    "z": "KEY_Z:ud:%s",
    "{": "KEY_LEFTSHIFT:d:0#KEY_LEFTBRACE:ud:%s#KEY_LEFTSHIFT:u:0",
    "}": "KEY_LEFTSHIFT:d:0#KEY_RIGHTBRACE:ud:%s#KEY_LEFTSHIFT:u:0",
    "|": "KEY_LEFTSHIFT:d:0#KEY_BACKSLASH:ud:%s#KEY_LEFTSHIFT:u:0",
    "~": "KEY_LEFTSHIFT:d:0#KEY_GRAVE:ud:%s#KEY_LEFTSHIFT:u:0",
    "ç": "KEY_LEFTALT:d:0#KEY_C:ud:%s#KEY_LEFTALT:u:0",
    "Ç": "KEY_LEFTSHIFT:d:0#KEY_LEFTALT:d:0#KEY_C:ud:%s#KEY_LEFTALT:u:0#KEY_LEFTSHIFT:u:0",
    "ß": "KEY_LEFTALT:d:0#KEY_S:ud:%s#KEY_LEFTALT:u:0",
    "ẞ": "KEY_LEFTSHIFT:d:0#KEY_LEFTALT:d:0#KEY_S:ud:%s#KEY_LEFTALT:u:0#KEY_LEFTSHIFT:u:0",
}


def killthread(threadobject):
    # based on https://pypi.org/project/kthread/
    if not threadobject.is_alive():
        return True
    tid = -1
    for tid1, tobj in threading._active.items():
        if tobj is threadobject:
            tid = tid1
            break
    if tid == -1:
        sys.stderr.write(f"{threadobject} not found")
        return False
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
        ctypes.c_long(tid), ctypes.py_object(SystemExit)
    )
    if res == 0:
        return False
    elif res != 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, 0)
        return False
    return True


columns_uiautomator = [
    "bounds",
    "text",
    "package",
    "resource_id",
    "clazz",
    "content_desc",
    "aa_center_x",
    "aa_center_y",
    "aa_area",
    "aa_width",
    "aa_height",
    "aa_start_x",
    "aa_start_y",
    "aa_end_x",
    "aa_end_y",
    "aa_is_square",
    "aa_w_h_relation",
    "checkable",
    "checked",
    "clickable",
    "enabled",
    "focusable",
    "focused",
    "index",
    "long_clickable",
    "password",
    "scrollable",
    "selected",
    "naf",
]
columns_uiautomator = ["aa_" + x for x in columns_uiautomator]

dtypes_uiautomator = {
    "bounds": np.dtype("object"),
    "text": np.dtype("object"),
    "package": np.dtype("object"),
    "resource_id": np.dtype("object"),
    "clazz": np.dtype("object"),
    "content_desc": np.dtype("object"),
    "aa_center_x": np.dtype("int64"),
    "aa_center_y": np.dtype("int64"),
    "aa_area": np.dtype("int64"),
    "aa_width": np.dtype("int64"),
    "aa_height": np.dtype("int64"),
    "aa_start_x": np.dtype("int64"),
    "aa_start_y": np.dtype("int64"),
    "aa_end_x": np.dtype("int64"),
    "aa_end_y": np.dtype("int64"),
    "aa_is_square": np.dtype("int64"),
    "aa_w_h_relation": np.dtype("float64"),
    "checkable": np.dtype("int64"),
    "checked": np.dtype("int64"),
    "clickable": np.dtype("int64"),
    "enabled": np.dtype("int64"),
    "focusable": np.dtype("int64"),
    "focused": np.dtype("int64"),
    "index": np.dtype("int64"),
    "long_clickable": np.dtype("int64"),
    "password": np.dtype("int64"),
    "scrollable": np.dtype("int64"),
    "selected": np.dtype("int64"),
    "naf": np.dtype("int64"),
}

columns_fragments = columns = [
    "MY_ID",
    "MY_GROUP_ID",
    "MY_ELEMENT_ID",
    "MY_DIRECT_PARENT_ID",
    "MY_PARENT_IDS",
    "ORIGINAL_STRING",
    "CENTER_X",
    "CENTER_Y",
    "AREA",
    "START_X",
    "START_Y",
    "END_X",
    "END_Y",
    "HEIGHT",
    "WIDTH",
    "IS_SQARE",
    "REL_WIDTH_HEIGHT",
    "HASHCODE_INT",
    "MID_INT",
    "SPACES",
    "CLASSNAME",
    "ELEMENT_ID",
    "HASHCODE",
    "MID",
    "START_X_RELATIVE",
    "END_X_RELATIVE",
    "START_Y_RELATIVE",
    "END_Y_RELATIVE",
    "CLICKABLE",
    "CONTEXT_CLICKABLE",
    "DRAWN",
    "ENABLED",
    "FOCUSABLE",
    "LONG_CLICKABLE",
    "PFLAG_ACTIVATED",
    "PFLAG_DIRTY_MASK",
    "PFLAG_FOCUSED",
    "PFLAG_HOVERED",
    "PFLAG_INVALIDATED",
    "PFLAG_IS_ROOT_NAMESPACE",
    "PFLAG_PREPRESSED",
    "PFLAG_SELECTED",
    "SCROLLBARS_HORIZONTAL",
    "SCROLLBARS_VERTICAL",
    "VISIBILITY",
]
columns_fragments = ["aa_" + x for x in columns_fragments]
dtypes_fragments = {
    "MY_ID": np.dtype("int64"),
    "MY_GROUP_ID": np.dtype("int64"),
    "MY_ELEMENT_ID": np.dtype("int64"),
    "MY_DIRECT_PARENT_ID": np.dtype("int64"),
    "MY_PARENT_IDS": np.dtype("object"),
    "ORIGINAL_STRING": np.dtype("object"),
    "CENTER_X": np.dtype("int64"),
    "CENTER_Y": np.dtype("int64"),
    "AREA": np.dtype("int64"),
    "START_X": np.dtype("int64"),
    "START_Y": np.dtype("int64"),
    "END_X": np.dtype("int64"),
    "END_Y": np.dtype("int64"),
    "HEIGHT": np.dtype("int64"),
    "WIDTH": np.dtype("int64"),
    "IS_SQARE": np.dtype("int64"),
    "REL_WIDTH_HEIGHT": np.dtype("float64"),
    "HASHCODE_INT": np.dtype("int64"),
    "MID_INT": np.dtype("int64"),
    "SPACES": np.dtype("int64"),
    "CLASSNAME": np.dtype("object"),
    "ELEMENT_ID": np.dtype("object"),
    "HASHCODE": np.dtype("object"),
    "MID": np.dtype("object"),
    "START_X_RELATIVE": np.dtype("int64"),
    "END_X_RELATIVE": np.dtype("int64"),
    "START_Y_RELATIVE": np.dtype("int64"),
    "END_Y_RELATIVE": np.dtype("int64"),
    "CLICKABLE": np.dtype("object"),
    "CONTEXT_CLICKABLE": np.dtype("object"),
    "DRAWN": np.dtype("object"),
    "ENABLED": np.dtype("object"),
    "FOCUSABLE": np.dtype("object"),
    "LONG_CLICKABLE": np.dtype("object"),
    "PFLAG_ACTIVATED": np.dtype("object"),
    "PFLAG_DIRTY_MASK": np.dtype("object"),
    "PFLAG_FOCUSED": np.dtype("object"),
    "PFLAG_HOVERED": np.dtype("object"),
    "PFLAG_INVALIDATED": np.dtype("object"),
    "PFLAG_IS_ROOT_NAMESPACE": np.dtype("object"),
    "PFLAG_PREPRESSED": np.dtype("object"),
    "PFLAG_SELECTED": np.dtype("object"),
    "SCROLLBARS_HORIZONTAL": np.dtype("object"),
    "SCROLLBARS_VERTICAL": np.dtype("object"),
    "VISIBILITY": np.dtype("object"),
}
dtypes_fragments = {"aa_" + k: v for k, v in dtypes_fragments.items()}
dtypes = {
    "aa_Text": np.dtype("object"),
    "aa_ContentDescription": np.dtype("object"),
    "aa_StateDescription": np.dtype("object"),
    "aa_ClassName": np.dtype("object"),
    "aa_PackageName": np.dtype("object"),
    "aa_Error": np.dtype("object"),
    "aa_AccessNodeInfo": np.dtype("object"),
    "aa_WindowId": np.dtype("object"),
    "aa_WindowChanges": np.dtype("object"),
    "aa_WindowChangeTypes": np.dtype("object"),
    "aa_VirtualDescendantId": np.dtype("object"),
    "aa_ViewIdResName": np.dtype("object"),
    "aa_UniqueId": np.dtype("object"),
    "aa_TraversalBefore": np.dtype("object"),
    "aa_TraversalAfter": np.dtype("object"),
    "aa_TooltipText": np.dtype("object"),
    "aa_TimeStamp": np.dtype("object"),
    "aa_TimeNow": np.dtype("object"),
    "aa_SpeechStateChangeTypes": np.dtype("object"),
    "aa_SourceWindowId": np.dtype("object"),
    "aa_SourceNodeId": np.dtype("object"),
    "aa_SourceDisplayId": np.dtype("object"),
    "aa_Source": np.dtype("object"),
    "aa_Sealed": np.dtype("object"),
    "aa_Records": np.dtype("object"),
    "aa_ParentNodeId": np.dtype("object"),
    "aa_ParcelableData": np.dtype("object"),
    "aa_MovementGranularities": np.dtype("object"),
    "aa_HashCode": np.dtype("object"),
    "aa_EventType": np.dtype("object"),
    "aa_Actions": np.dtype("object"),
    "aa_ContentChangeTypes": np.dtype("object"),
    "aa_ConnectionId": np.dtype("object"),
    "aa_ChildAccessibilityIds": np.dtype("object"),
    "aa_BooleanProperties": np.dtype("object"),
    "aa_BeforeText": np.dtype("object"),
    "aa_Active": np.dtype("object"),
    "aa_AccessibilityViewId": np.dtype("object"),
    "aa_AccessibilityTool": np.dtype("object"),
    "aa_BoundsInScreen": np.dtype("object"),
    "aa_BoundsInParent": np.dtype("object"),
    "aa_UnixTimeText": np.dtype("object"),
    "aa_start_x_real": np.dtype("int64"),
    "aa_start_y_real": np.dtype("int64"),
    "aa_end_x_real": np.dtype("int64"),
    "aa_end_y_real": np.dtype("int64"),
    "aa_start_x": np.dtype("int64"),
    "aa_start_y": np.dtype("int64"),
    "aa_end_x": np.dtype("int64"),
    "aa_end_y": np.dtype("int64"),
    "aa_center_x": np.dtype("int64"),
    "aa_center_y": np.dtype("int64"),
    "aa_width": np.dtype("int64"),
    "aa_height": np.dtype("int64"),
    "aa_w_h_relation": np.dtype("float64"),
    "aa_area": np.dtype("int64"),
    "aa_parent_start_x_real": np.dtype("int64"),
    "aa_parent_start_y_real": np.dtype("int64"),
    "aa_parent_end_x_real": np.dtype("int64"),
    "aa_parent_end_y_real": np.dtype("int64"),
    "aa_parent_start_x": np.dtype("int64"),
    "aa_parent_start_y": np.dtype("int64"),
    "aa_parent_end_x": np.dtype("int64"),
    "aa_parent_end_y": np.dtype("int64"),
    "aa_parent_center_x": np.dtype("int64"),
    "aa_parent_center_y": np.dtype("int64"),
    "aa_parent_width": np.dtype("int64"),
    "aa_parent_height": np.dtype("int64"),
    "aa_parent_w_h_relation": np.dtype("int64"),
    "aa_parent_area": np.dtype("int64"),
    "aa_UnixTime": np.dtype("int64"),
    "aa_distance_from_start": np.dtype("int64"),
    "aa_size": np.dtype("int64"),
    "aa_Visible": np.dtype("uint8"),
    "aa_Password": np.dtype("uint8"),
    "aa_Selected": np.dtype("uint8"),
    "aa_Scrollable": np.dtype("uint8"),
    "aa_LongClickable": np.dtype("uint8"),
    "aa_Loggable": np.dtype("uint8"),
    "aa_IsTextSelectable": np.dtype("uint8"),
    "aa_ImportantForAccessibility": np.dtype("uint8"),
    "aa_Enabled": np.dtype("uint8"),
    "aa_Empty": np.dtype("uint8"),
    "aa_ContextClickable": np.dtype("uint8"),
    "aa_ContentInvalid": np.dtype("uint8"),
    "aa_FullScreen": np.dtype("uint8"),
    "aa_Focused": np.dtype("uint8"),
    "aa_Focusable": np.dtype("uint8"),
    "aa_AccessibilityFocused": np.dtype("uint8"),
    "aa_AccessibilityDataSensitive": np.dtype("uint8"),
    "aa_Clickable": np.dtype("uint8"),
    "aa_Checked": np.dtype("uint8"),
    "aa_Checkable": np.dtype("uint8"),
}
columns = [
    "Text",
    "ContentDescription",
    "StateDescription",
    "ClassName",
    "PackageName",
    "Error",
    "AccessNodeInfo",
    "WindowId",
    "WindowChanges",
    "WindowChangeTypes",
    "VirtualDescendantId",
    "ViewIdResName",
    "UniqueId",
    "TraversalBefore",
    "TraversalAfter",
    "TooltipText",
    "TimeStamp",
    "TimeNow",
    "SpeechStateChangeTypes",
    "SourceWindowId",
    "SourceNodeId",
    "SourceDisplayId",
    "Source",
    "Sealed",
    "Records",
    "ParentNodeId",
    "ParcelableData",
    "MovementGranularities",
    "HashCode",
    "EventType",
    "Actions",
    "ContentChangeTypes",
    "ConnectionId",
    "ChildAccessibilityIds",
    "BooleanProperties",
    "BeforeText",
    "Active",
    "AccessibilityViewId",
    "AccessibilityTool",
    "BoundsInScreen",
    "BoundsInParent",
    "UnixTimeText",
    "aa_start_x_real",
    "aa_start_y_real",
    "aa_end_x_real",
    "aa_end_y_real",
    "aa_start_x",
    "aa_start_y",
    "aa_end_x",
    "aa_end_y",
    "aa_center_x",
    "aa_center_y",
    "aa_width",
    "aa_height",
    "aa_w_h_relation",
    "aa_area",
    "aa_parent_start_x_real",
    "aa_parent_start_y_real",
    "aa_parent_end_x_real",
    "aa_parent_end_y_real",
    "aa_parent_start_x",
    "aa_parent_start_y",
    "aa_parent_end_x",
    "aa_parent_end_y",
    "aa_parent_center_x",
    "aa_parent_center_y",
    "aa_parent_width",
    "aa_parent_height",
    "aa_parent_w_h_relation",
    "aa_parent_area",
    "UnixTime",
    "distance_from_start",
    "size",
    "Visible",
    "Password",
    "Selected",
    "Scrollable",
    "LongClickable",
    "Loggable",
    "IsTextSelectable",
    "ImportantForAccessibility",
    "Enabled",
    "Empty",
    "ContextClickable",
    "ContentInvalid",
    "FullScreen",
    "Focused",
    "Focusable",
    "AccessibilityFocused",
    "AccessibilityDataSensitive",
    "Clickable",
    "Checked",
    "Checkable",
]
columns = [f"aa_{x}" if not x.startswith("aa_") else x for x in columns]
iswindows = "win" in platform().lower()

columns_files = [
    "PermissionsSymbolic",
    "SELinuxContext",
    "FileSize",
    "OwnerUsername",
    "GroupName",
    "SymlinkTarget",
    "ModificationTimestampEpoch",
    "OwnerUID",
    "GroupGID",
    "PermissionsOctal",
    "FullPath",
    "FileName",
]
columns_files = [f"aa_{x}" if not x.startswith("aa_") else x for x in columns_files]

# for key, item in dddd.dtypes.to_frame().iterrows():
#     print(f"'{key}':" f"np.dtype('{item[0]}'),")
dtypes_files = {
    "aa_PermissionsSymbolic": np.dtype("object"),
    "aa_SELinuxContext": np.dtype("object"),
    "aa_FileSize": np.dtype("int64"),
    "aa_OwnerUsername": np.dtype("object"),
    "aa_GroupName": np.dtype("object"),
    "aa_SymlinkTarget": np.dtype("object"),
    "aa_ModificationTimestampEpoch": np.dtype("float64"),
    "aa_OwnerUID": np.dtype("int64"),
    "aa_GroupGID": np.dtype("int64"),
    "aa_PermissionsOctal": np.dtype("int64"),
    "aa_FullPath": np.dtype("object"),
    "aa_FileName": np.dtype("object"),
}

# windows neglegted for now
if iswindows:
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = subprocess.SW_HIDE
    creationflags = subprocess.CREATE_NO_WINDOW
    invisibledict = {
        "startupinfo": startupinfo,
        "creationflags": creationflags,
        "start_new_session": True,
    }
else:
    invisibledict = {}


fields_cor = "folder file path ext"
classname_cor = "files"

FilePathInfos = namedtuple(classname_cor, fields_cor)


class StatsWriter:
    def __init__(self, sourcef, statsdict):
        self.path = sourcef
        self.owner = statsdict["owner"]
        self.group = statsdict["group"]
        self.perm = statsdict["perm"]
        self.atime = statsdict["atime"]
        self.mtime = statsdict["mtime"]
        self.selinux_context = statsdict["selinux_context"]
        self.statscmd = rf"""chown {self.owner} '{sourcef}'
chgrp {self.group} '{sourcef}'
chmod {self.perm} '{sourcef}'
touch -m -d @{self.mtime} '{sourcef}'
touch -a -d @{self.atime} '{sourcef}'
chcon {self.selinux_context} '{sourcef}'"""

    def __str__(self):
        return self.statscmd

    def __repr__(self):
        return self.__str__()

    def __call__(self):
        return subprocess.run(
            sconfig.mycfg_shell, input=str(self).encode(), shell=True, env=os.environ
        )


def get_folder_file_complete_path(folders, maxsubfolders=-1):
    if isinstance(folders, str):
        folders = [folders]
    folders = list(set([os.path.normpath(x) for x in folders]))
    folders = [x for x in folders if os.path.exists(x)]
    folders = [x for x in folders if os.path.isdir(x)]

    listOfFiles2 = []
    limit = 1000000000000
    checkdepth = False
    for dirName in folders:
        if maxsubfolders > -1:
            sepa = dirName.count("\\") + dirName.count("/")
            limit = sepa + maxsubfolders
        if limit < 1000000000000:
            checkdepth = True
        for dirpath, dirnames, filenames in os.walk(dirName):
            if checkdepth:
                depthok = dirpath.count("\\") + dirpath.count("/") <= limit
            else:
                depthok = True
            ra = [
                FilePathInfos(
                    dirpath,
                    file,
                    os.path.normpath(os.path.join(dirpath, file)),
                    pathlib.Path(file).suffix,
                )
                for file in filenames
                if depthok
            ]
            if ra:
                listOfFiles2.extend(ra)

    allmyfiles_list = []
    rightdictdummy = {
        "perm": None,
        "owner": None,
        "group": None,
        "atime": None,
        "mtime": None,
        "selinux_context": None,
        "statsbackwriter": None,
    }
    for folder, file, path, ext in listOfFiles2:
        allmyfiles = {}
        allmyfiles["folder"] = folder
        allmyfiles["file"] = file
        allmyfiles["path"] = path
        allmyfiles["ext"] = ext
        fstat = os.stat(path)
        try:
            inputdata = rf'''
sourcef='{path}'
perm=$(stat -c '%a' "$sourcef")
owner=$(stat -c '%U' "$sourcef")
group=$(stat -c '%G' "$sourcef")
atime=$(stat -c '%X' "$sourcef")
mtime=$(stat -c '%Y' "$sourcef")
selinux_context="$(ls -Z "$sourcef" | awk '{{print $1}}')"
echo "{{\"perm\":\"$perm\", \"owner\": \"$owner\", \"group\": \"$group\", \"atime\": \"$atime\", \"mtime\": \"$mtime\", \"selinux_context\": \"$selinux_context\"}}"'''
            rightsdict = eval(
                subprocess.run(
                    "sh",
                    input=inputdata.encode(),
                    shell=True,
                    env=os.environ,
                    capture_output=True,
                ).stdout.decode("utf-8", "backslashreplace")
            )
            statsbackwriter = StatsWriter(path, rightsdict)
            rightsdict["statsbackwriter"] = statsbackwriter
        except Exception:
            errwrite()
            rightsdict = rightdictdummy

        allmyfiles.update(
            dict((x, getattr(fstat, x)) for x in dir(fstat) if x.startswith("st_"))
        )
        allmyfiles.update(rightsdict)
        allmyfiles_list.append(allmyfiles)

    return pd.DataFrame(allmyfiles_list)


def random_function(minint, maxint):
    try:
        return random.randint(minint, maxint)
    except Exception:
        return minint


def create_sendkey_command(
    exefile, device_path, text, min_time_key_press, max_time_key_press
):
    min_time_key_press_int = int(min_time_key_press)
    max_time_key_press_int = int(max_time_key_press)
    commands = []
    for letter in text:
        commands.append(
            mappingdict[letter]
            % str(random_function(min_time_key_press_int, max_time_key_press_int))
        )
    return exefile + " " + device_path + " " + "#".join(commands)


def _download_and_save(link, folder, filename):
    filepath = os.path.join(
        folder,
        filename,
    )
    with requests.get(link) as r:
        with open(
            filepath,
            "wb",
        ) as f:
            f.write(r.content)
    return filepath


def download_uiautomator_dump_without_could_not_detect_idle_state():
    return _download_and_save(
        link_uiautomator_dump_without_could_not_detect_idle_state,
        folder_uiautomator_dump_without_could_not_detect_idle_state,
        "cppfile.cpp",
    )


def download_uiautomator_dump_to_csv():
    return _download_and_save(
        link_uiautomator_dump_to_csv,
        folder_uiautomator_dump_to_csv,
        "cppfile.cpp",
    )


def download_sendevent_multicommands_type_text():
    return _download_and_save(
        link_sendevent_multicommands_type_text,
        folder_sendevent_multicommands_type_text,
        "cppfile.cpp",
    )


def download_mouse_sendevent_android():
    return _download_and_save(
        link_mouse_sendevent_android,
        folder_mouse_sendevent_android,
        "cppfile.cpp",
    )


def download_getevent_pretty_print_linux():
    return _download_and_save(
        link_getevent_pretty_print_linux,
        folder_getevent_pretty_print_linux,
        "cppfile.cpp",
    )


def download_android_fragment_parser():
    return _download_and_save(
        link_android_fragment_parser,
        folder_android_fragment_parser,
        "cppfile.cpp",
    )


def download_uiautomator_eventsparser_cpp():
    return _download_and_save(
        link_uiautomator_eventsparser_cpp,
        folder_uiautomator_eventsparser_cpp,
        "cppfile.cpp",
    )


def download_lcp():
    return _download_and_save(
        link_lcp,
        folder_lcp,
        "cppfile.cpp",
    )


def download_getevent_keydumper_linux():
    return _download_and_save(
        link_getevent_keydumper_linux,
        folder_getevent_keydumper_linux,
        "cppfile.cpp",
    )


def download_all_scripts():
    return (
        download_uiautomator_dump_without_could_not_detect_idle_state(),
        download_uiautomator_dump_to_csv(),
        download_sendevent_multicommands_type_text(),
        download_mouse_sendevent_android(),
        download_getevent_keydumper_linux(),
        download_getevent_pretty_print_linux(),
        download_android_fragment_parser(),
        download_uiautomator_eventsparser_cpp(),
        download_lcp(),
    )


def compile_files(
    allscripts,
    compiler=r"g++",
    compiler_args=(
        "-std=c++2a",
        "-O3",
        "-g0",
        "-o",
        "a.out",
    ),
):
    compiler_args = (compiler,) + compiler_args
    all_executable_files = {}
    current_working_dict = os.getcwd()
    for script in allscripts:
        next_working_dict = os.path.dirname(script)
        os.chdir(next_working_dict)
        cmd2execute = compiler_args + (script,)
        subprocess.run(
            " ".join(cmd2execute),
            shell=True,
            env=os.environ,
            cwd=next_working_dict,
        )
        executable_file = os.path.join(next_working_dict, "a.out")
        all_executable_files[next_working_dict.split(os.sep)[-1]] = executable_file
        # print(executable_file)
    os.chdir(current_working_dict)
    return all_executable_files


def download_and_compile_files(gcc_exe="g++"):
    allscripts = download_all_scripts()
    return compile_files(
        allscripts,
        compiler=gcc_exe,
        compiler_args=(
            "-std=c++2a",
            "-O3",
            "-g0",
            "-o",
            "a.out",
        ),
    )


def convert_to_csv(bytedata):
    return pd.read_csv(
        io.StringIO(bytedata.stdout.decode("utf-8", "backslashreplace")),
        engine="python",
        on_bad_lines="warn",
        sep=",",
        na_filter=False,
        quoting=1,
        encoding_errors="backslashreplace",
    )


def convert_to_csv_bytes(bytedata):
    return pd.read_csv(
        io.StringIO(bytedata.decode("utf-8", "backslashreplace")),
        engine="python",
        on_bad_lines="warn",
        sep=",",
        na_filter=False,
        quoting=1,
        encoding_errors="backslashreplace",
    )


def get_uiautomator_data(uiautomator_dump_to_csv_exe, timeout=30):
    try:
        return pd.read_csv(
            io.StringIO(
                (
                    b"".join(
                        subprocess.run(
                            f"rm -f /sdcard/window_dump.xml;{sconfig.mycfg_system_folder}uiautomator dump > /dev/null 2>&1 && {uiautomator_dump_to_csv_exe} /sdcard/window_dump.xml",
                            shell=True,
                            capture_output=True,
                            env=os.environ,
                        ).stdout.splitlines(keepends=True)[1:]
                    )
                ).decode("utf-8", "backslashreplace")
            ),
            engine="python",
            on_bad_lines="warn",
            sep=",",
            na_filter=False,
            quoting=1,
            encoding_errors="backslashreplace",
            index_col=False,
            names=columns_uiautomator,
            dtype=dtypes_uiautomator,
        )
    except Exception:
        errwrite()
        return pd.DataFrame()


def save_bmp(filename, img):
    image_array = img[..., [2, 0, 1]]
    height, width, channels = image_array.shape
    # BMP headers
    file_size = (
        54 + (3 * width + width % 4) * height
    )  # File header + pixel data (including padding)
    reserved = 0
    offset = 54  # Header size
    header_size = 40
    planes = 1
    bits_per_pixel = 24
    compression = 0
    image_size = (3 * width + width % 4) * height  # Pixel data size including padding
    ppm = 2835  # 72 DPI in pixels per meter
    important_colors = 0

    # File header
    bmp_file_header = [
        0x42,
        0x4D,  # 'BM'
        file_size & 0xFF,
        (file_size >> 8) & 0xFF,
        (file_size >> 16) & 0xFF,
        (file_size >> 24) & 0xFF,
        reserved & 0xFF,
        (reserved >> 8) & 0xFF,
        (reserved >> 16) & 0xFF,
        (reserved >> 24) & 0xFF,
        offset & 0xFF,
        (offset >> 8) & 0xFF,
        (offset >> 16) & 0xFF,
        (offset >> 24) & 0xFF,
    ]

    # DIB header (BITMAPINFOHEADER)
    bmp_info_header = [
        header_size & 0xFF,
        (header_size >> 8) & 0xFF,
        (header_size >> 16) & 0xFF,
        (header_size >> 24) & 0xFF,
        width & 0xFF,
        (width >> 8) & 0xFF,
        (width >> 16) & 0xFF,
        (width >> 24) & 0xFF,
        height & 0xFF,
        (height >> 8) & 0xFF,
        (height >> 16) & 0xFF,
        (height >> 24) & 0xFF,
        planes & 0xFF,
        (planes >> 8) & 0xFF,
        bits_per_pixel & 0xFF,
        (bits_per_pixel >> 8) & 0xFF,
        compression & 0xFF,
        (compression >> 8) & 0xFF,
        (compression >> 16) & 0xFF,
        (compression >> 24) & 0xFF,
        image_size & 0xFF,
        (image_size >> 8) & 0xFF,
        (image_size >> 16) & 0xFF,
        (image_size >> 24) & 0xFF,
        ppm & 0xFF,
        (ppm >> 8) & 0xFF,
        (ppm >> 16) & 0xFF,
        (ppm >> 24) & 0xFF,
        ppm & 0xFF,
        (ppm >> 8) & 0xFF,
        (ppm >> 16) & 0xFF,
        (ppm >> 24) & 0xFF,
        important_colors & 0xFF,
        (important_colors >> 8) & 0xFF,
        (important_colors >> 16) & 0xFF,
        (important_colors >> 24) & 0xFF,
    ]

    pixel_data = []
    row_padding = (4 - (width * 3) % 4) % 4
    for row in reversed(image_array):
        for pixel in row:
            pixel_data.extend(pixel)
        pixel_data.extend([0] * row_padding)  # Add padding

    with open(filename, "wb") as f:
        f.write(bytearray(bmp_file_header))
        f.write(bytearray(bmp_info_header))
        f.write(bytearray(pixel_data))


def get_uiautomator_data_with_cpu_limit(
    uiautomator_dump_to_csv_exe, cpu_limit=5, timeout=30
):
    try:
        return pd.read_csv(
            io.StringIO(
                (
                    b"".join(
                        subprocess.run(
                            f"rm -f /sdcard/window_dump.xml;{sconfig.mycfg_system_folder}uiautomator dump > /dev/null 2>&1 && {uiautomator_dump_to_csv_exe} {cpu_limit}",
                            shell=True,
                            capture_output=True,
                            env=os.environ,
                        ).stdout.splitlines(keepends=True)[2:]
                    )
                ).decode("utf-8", "backslashreplace")
            ),
            engine="python",
            on_bad_lines="warn",
            sep=",",
            na_filter=False,
            quoting=1,
            encoding_errors="backslashreplace",
            index_col=False,
            names=columns_uiautomator,
            dtype=dtypes_uiautomator,
        )
    except Exception:
        errwrite()
        return pd.DataFrame()


def get_fragment_data(android_fragment_parser_exe, timeout=30):
    try:
        dff = pd.read_csv(
            io.StringIO(
                (
                    b"".join(
                        subprocess.run(
                            android_fragment_parser_exe,
                            shell=False,
                            capture_output=True,
                            env=os.environ,
                        ).stdout.splitlines(keepends=True)[1:]
                    )
                ).decode("utf-8", "backslashreplace")
            ),
            engine="python",
            on_bad_lines="warn",
            sep=",",
            na_filter=False,
            quoting=1,
            encoding_errors="backslashreplace",
            index_col=False,
            names=columns_fragments,
            dtype=dtypes_fragments,
        )
        dff.loc[:, "aa_is_child"] = False
        dff.loc[
            (~dff.aa_MY_PARENT_IDS.str.endswith(","))
            & (dff.aa_MY_PARENT_IDS.str.len() > 0),
            "aa_is_child",
        ] = True
        return dff
    except Exception:
        errwrite()
        return pd.DataFrame()


def get_key_events(keyevent_dumper_exe, timeout=30):
    try:
        return convert_to_csv(
            subprocess.run(
                keyevent_dumper_exe,
                shell=False,
                capture_output=True,
                env=os.environ,
            )
        )
    except Exception:
        errwrite()
        return pd.DataFrame()


def execute_sk_cmd(
    exefile,
    text,
    device_path,
    remove_accents=False,
    min_time_key_press=1,
    max_time_key_press=3,
):
    if remove_accents:
        text = "".join(
            [
                lookup(k, case_sens=True, replace="", add_to_printable="")["suggested"]
                for k in text
            ]
        )
    wholecmd = create_sendkey_command(
        exefile=exefile,
        device_path=device_path,
        text=text,
        min_time_key_press=min_time_key_press,
        max_time_key_press=max_time_key_press,
    )
    return subprocess.run(
        wholecmd,
        shell=True,
        capture_output=True,
        env=os.environ,
    ).stderr.decode("utf-8", "backslashreplace")


class LcpParser:
    def __init__(
        self,
        cmdline=r"/data/data/com.termux/files/usr/bin/lcp/a.out",
        deque_size=300,
    ):
        self.cmdline = cmdline
        self.deque_size = deque_size
        self.d = deque([], maxlen=deque_size)
        self.t1 = None
        self.l = []
        self.p = None

    def __str__(self):
        return (b"".join(self.d)).decode("utf-8", "backslashreplace")

    def __repr__(self):
        return self.__str__()

    def start(self):
        self.p = subprocess.Popen(
            self.cmdline,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            stdin=subprocess.DEVNULL,
            env=os.environ,
            **invisibledict,
        )
        self.t1 = threading.Thread(target=self._threadreader, daemon=True)
        self.t1.start()
        return self

    def _threadreader(self):
        func = self.p.stdout.readline
        _ = [line for line in iter(func, b"") if self.d.append(line)]

    def stop(self):
        self.p.terminate()
        if not iswindows:
            subprocess.run(
                " ".join(["kill", "-9", str(self.p.pid)]), shell=True, env=os.environ
            )
            subprocess.run(
                sconfig.mycfg_shell,
                input=r"""top -b -n1 | grep -F 'sh -c -- stty raw' | grep -v "grep -F" | awk '{system("kill "$1)}'""".encode(),
                shell=True,
                env=os.environ,
            )
            subprocess.run(
                sconfig.mycfg_shell,
                input=r"""top -b -n1 | grep -F '--dividers' | grep -v "grep -F" | awk '{system("kill "$1)}'""".encode(),
                shell=True,
                env=os.environ,
            )
        else:
            subprocess.Popen(
                ["taskkill", "/PID", str(self.p.pid), "/F"], shell=True, env=os.environ
            )
        killthread(self.t1)

    def get_dataframe(self):
        try:
            self.l.clear()
            sizeofdeque = len(self.d)
            for _ in range(sizeofdeque):
                self.l.append(self.d.popleft())
            return pd.read_csv(
                io.StringIO((b"".join(self.l)).decode("utf-8", "backslashreplace")),
                engine="python",
                sep=",",
                index_col=False,
                names=columns,
                dtype=dtypes,
                na_filter=False,
                quoting=1,
                encoding_errors="backslashreplace",
                on_bad_lines="warn",
            )
        except Exception:
            errwrite()
            return pd.DataFrame()

    def clear_deque(self):
        self.d.clear()
        return self


class EventParser:
    def __init__(
        self,
        cmdline=r"/data/data/com.termux/files/usr/bin/uiautomator_eventsparser_cpp/a.out",
        deque_size=300,
    ):
        self.cmdline = cmdline
        self.deque_size = deque_size
        self.d = deque([], maxlen=deque_size)
        self.t1 = None
        self.l = []
        self.p = None

    def __str__(self):
        return (b"".join(self.d)).decode("utf-8", "backslashreplace")

    def __repr__(self):
        return self.__str__()

    def start(self):
        subprocess.run("pkill uiautomator", shell=True, env=os.environ)
        time.sleep(1)
        self.p = subprocess.Popen(
            self.cmdline,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            stdin=subprocess.DEVNULL,
            env=os.environ,
            shell=True,
            **invisibledict,
        )
        self.t1 = threading.Thread(target=self._threadreader, daemon=True)
        self.t1.start()
        return self

    def _threadreader(self):
        func = self.p.stdout.readline
        _ = [line for line in iter(func, b"") if self.d.append(line)]
        # try:
        #     for line in iter(func, b""):
        #         self.d.append(line)
        # except Exception:
        #     errwrite()

    def stop(self):
        self.p.terminate()
        if not iswindows:
            subprocess.run(
                " ".join(["kill", "-9", str(self.p.pid)]), shell=True, env=os.environ
            )
            subprocess.run(
                sconfig.mycfg_shell,
                input=r"""top -b -n1 | grep -F 'uiautomator events' | grep -v "grep" | awk '{system("kill "$1)}'""".encode(),
                shell=True,
                env=os.environ,
            )
        else:
            subprocess.Popen(
                ["taskkill", "/PID", str(self.p.pid), "/F"], shell=True, env=os.environ
            )
        killthread(self.t1)

    def get_dataframe(self):
        try:
            self.l.clear()
            sizeofdeque = len(self.d)
            for _ in range(sizeofdeque):
                self.l.append(self.d.popleft())
            return pd.read_csv(
                io.StringIO((b"".join(self.l)).decode("utf-8", "backslashreplace")),
                engine="python",
                sep=",",
                index_col=False,
                names=[
                    "TimeStampInt",
                    "AccessibilityDataSensitive",
                    "AccessibilityFocused",
                    "AccessibilityTool",
                    "Action",
                    "Active",
                    "AddedCount",
                    "BeforeText",
                    "BooleanProperties",
                    "Checked",
                    "ClassName",
                    "ConnectionId",
                    "ContentChangeTypes",
                    "ContentDescription",
                    "ContentInvalid",
                    "CurrentItemIndex",
                    "Empty",
                    "Enabled",
                    "EventTime",
                    "EventType",
                    "Focused",
                    "FromIndex",
                    "FullScreen",
                    "ItemCount",
                    "Loggable",
                    "MaxScrollX",
                    "MaxScrollY",
                    "MovementGranularity",
                    "PackageName",
                    "ParcelableData",
                    "Password",
                    "Records",
                    "RemovedCount",
                    "ScrollDeltaX",
                    "ScrollDeltaY",
                    "ScrollX",
                    "ScrollY",
                    "Scrollable",
                    "Sealed",
                    "Source",
                    "SourceDisplayId",
                    "SourceNodeId",
                    "SourceWindowId",
                    "SpeechStateChangeTypes",
                    "Text",
                    "TimeNow",
                    "TimeStamp",
                    "ToIndex",
                    "WindowChangeTypes",
                    "WindowChanges",
                    "WindowId",
                    "recordCount",
                ],
                dtype=object,
                na_filter=False,
                quoting=1,
                encoding_errors="backslashreplace",
                on_bad_lines="warn",
            )
        except Exception:
            errwrite()
            return pd.DataFrame()

    def clear_deque(self):
        self.d.clear()
        return self


def get_screen_width_height():
    try:
        width, height = (
            subprocess.run(
                f'''{sconfig.mycfg_system_folder}wm size | sort | head -n1 | grep -Eo "[[:digit:]]+x[[:digit:]]+"''',
                shell=True,
                env=os.environ,
                capture_output=True,
            )
            .stdout.strip()
            .split(b"x")
        )
        return int(width), int(height)
    except Exception:
        errwrite()
        return -1, -1


def _execute_command_run_shell(cmdline, timeout=100000):
    if isinstance(cmdline, bytes):
        cmdline = cmdline.decode("utf-8", "backslashreplace")
    if isinstance(cmdline, (tuple, list)):
        cmdline = " ".join([str(x) for x in cmdline])
    try:
        return subprocess.run(
            cmdline, shell=True, capture_output=False, env=os.environ, timeout=timeout
        )
    except Exception:
        errwrite()
        return


def _execute_command_run_shell_capture_output(cmdline, timeout=100000):
    if isinstance(cmdline, bytes):
        cmdline = cmdline.decode("utf-8", "backslashreplace")
    if isinstance(cmdline, (tuple, list)):
        cmdline = " ".join([str(x) for x in cmdline])
    try:
        return subprocess.run(
            cmdline, shell=True, capture_output=True, env=os.environ, timeout=timeout
        )
    except Exception:
        errwrite()
        return


def _execute_command_run_shell_open_shell_first(cmdline, timeout=100000):
    if isinstance(cmdline, str):
        cmdline = cmdline.encode("utf-8")
    if isinstance(cmdline, (tuple, list)):
        cmdline = " ".join([str(x) for x in cmdline])
        cmdline = cmdline.encode("utf-8")
    try:
        return subprocess.run(
            sconfig.mycfg_shell,
            input=cmdline,
            shell=True,
            capture_output=False,
            env=os.environ,
            timeout=timeout,
        )
    except Exception:
        errwrite()
        return


def _execute_command_run_shell_capture_output_open_shell_first(cmdline, timeout=100000):
    if isinstance(cmdline, str):
        cmdline = cmdline.encode("utf-8")
    if isinstance(cmdline, (tuple, list)):
        cmdline = " ".join([str(x) for x in cmdline])
        cmdline = cmdline.encode("utf-8")
    try:
        return subprocess.run(
            sconfig.mycfg_shell,
            input=cmdline,
            shell=True,
            capture_output=True,
            env=os.environ,
            timeout=timeout,
        )
    except Exception:
        errwrite()
        return


class TermuAutoADB:
    def __init__(
        self,
        android_fragment_parser,
        getevent_keydumper_linux,
        getevent_pretty_print_linux,
        mouse_sendevent_android,
        sendevent_multicommands_type_text,
        uiautomator_dump_to_csv,
        uiautomator_dump_without_could_not_detect_idle_state,
        uiautomator_eventsparser_cpp,
        lcp,
        device_mouse="",
        device_keyboard="",
        deque_size_event_parser=1000,
        deque_size_lcp=1000,
        screen_width=720,
        screen_height=1280,
    ):
        self.cmd = ExecuteShellCmds()
        self.android_fragment_parser = android_fragment_parser
        self.getevent_keydumper_linux = getevent_keydumper_linux
        self.getevent_pretty_print_linux = getevent_pretty_print_linux
        self.mouse_sendevent_android = mouse_sendevent_android
        self.sendevent_multicommands_type_text = sendevent_multicommands_type_text
        self.uiautomator_dump_to_csv = uiautomator_dump_to_csv
        self.uiautomator_dump_without_could_not_detect_idle_state = (
            uiautomator_dump_without_could_not_detect_idle_state
        )
        self.uiautomator_eventsparser_cpp = uiautomator_eventsparser_cpp
        self.lcp = lcp
        self.device_mouse = device_mouse
        self.device_keyboard = device_keyboard
        self._event_parser = EventParser(
            cmdline=uiautomator_eventsparser_cpp,
            deque_size=deque_size_event_parser,
        )
        self._lcp_parser = LcpParser(cmdline=lcp, deque_size=deque_size_lcp)
        self.screen_width = screen_width
        self.screen_height = screen_height

    def event_parser_start(self):
        self._event_parser.start()
        return self

    def event_parser_get_df(self):
        return self._event_parser.get_dataframe()

    def event_parser_stop(self):
        self._event_parser.stop()
        return self

    def event_parser_clear_deque(self):
        self._event_parser.clear_deque()
        return self

    def lcp_parser_start(self):
        self._lcp_parser.start()
        return self

    def lcp_parser_get_df(self):
        return self._lcp_parser.get_dataframe()

    def lcp_parser_stop(self):
        self._lcp_parser.stop()
        return self

    def lcp_parser_clear_deque(self):
        self._lcp_parser.clear_deque()
        return self

    @staticmethod
    def get_df_window_elements():
        alldfs = []
        itemindex = 0
        allparsed = parse_window_elements(
            dump_cmd=[
                f"{sconfig.mycfg_system_folder}cmd",
                "window",
                "dump-visible-window-views",
            ],
        )
        for parsed in allparsed:
            try:
                alldfs.append(
                    pd.DataFrame.from_dict(parsed, orient="index", dtype=object).assign(
                        aa_itemindex=itemindex
                    )
                )
                itemindex += 1
            except Exception:
                errwrite()
        return pd.concat(alldfs, ignore_index=True)

    def get_df_uiautomator_frame(self, timeout=30):
        return get_uiautomator_data(self.uiautomator_dump_to_csv, timeout=timeout)

    def get_df_fragments(self, timeout=30):
        return get_fragment_data(self.android_fragment_parser, timeout=timeout)

    def get_df_uiautomator_frame_with_cpu_limit(self, cpu_limit=5, timeout=30):
        return get_uiautomator_data_with_cpu_limit(
            self.uiautomator_dump_without_could_not_detect_idle_state,
            cpu_limit=cpu_limit,
            timeout=timeout,
        )

    def get_df_all_devices_and_keys(self, timeout=30):
        return get_key_events(self.getevent_keydumper_linux, timeout=timeout)

    def set_mouse_device(self, device_mouse):
        self.device_mouse = device_mouse
        return self

    def set_keyboard_device(self, device_keyboard):
        self.device_keyboard = device_keyboard
        return self

    def write_text(
        self,
        text,
        remove_accents=True,
        min_time_key_press=0,
        max_time_key_press=0,
    ):
        return execute_sk_cmd(
            exefile=self.sendevent_multicommands_type_text,
            text=text,
            device_path=self.device_keyboard,
            remove_accents=remove_accents,
            min_time_key_press=min_time_key_press,
            max_time_key_press=max_time_key_press,
        )

    def start_getevent(self):
        return subprocess.Popen(
            self.getevent_pretty_print_linux
            + " "
            + str(self.screen_width)
            + " "
            + str(self.screen_height),
            shell=True,
            env=os.environ,
        )

    def mouse_move_from_current_to(
        self,
        x,
        y,
        sleep_time=0,
        debug=0,
        event_multiply=1,
        natural_movement=1,
        use_every_n_element=1,
        min_x_variation=0,
        max_x_variation=0,
        min_y_variation=0,
        max_y_variation=0,
        print_device_info=1,
        device=None,
    ):
        if device:
            device2use = device
        else:
            device2use = self.device_mouse
        return _execute_command_run_shell(
            [
                self.mouse_sendevent_android,
                "--screen_width=" + str(self.screen_width),
                "--screen_height=" + str(self.screen_height),
                "--device=" + device2use,
                "--x=" + str(x),
                "--y=" + str(y),
                "--action=0",
                "--sleep_time=" + str(sleep_time),
                "--debug=" + str(debug),
                "--event_multiply=" + str(event_multiply),
                "--natural_movement=" + str(natural_movement),
                "--use_every_n_element=" + str(use_every_n_element),
                "--min_x_variation=" + str(min_x_variation),
                "--max_x_variation=" + str(max_x_variation),
                "--min_y_variation=" + str(min_y_variation),
                "--max_y_variation=" + str(max_y_variation),
                "--print_device_info=" + str(print_device_info),
            ],
            timeout=100000,
        )

    def _mclick(
        self,
        action,
        device=None,
        other_args=(),
    ):
        if device:
            device2use = device
        else:
            device2use = self.device_mouse
        return _execute_command_run_shell(
            [
                self.mouse_sendevent_android,
                "--screen_width=" + str(self.screen_width),
                "--screen_height=" + str(self.screen_height),
                "--device=" + device2use,
                "--action=" + str(action),
                *other_args,
            ],
            timeout=100000,
        )

    def mouse_left_click_here(
        self,
        device=None,
    ):
        return self._mclick(4, device=device)

    def mouse_right_click_here(
        self,
        device=None,
    ):
        return self._mclick(5, device=device)

    def mouse_middle_click_here(
        self,
        device=None,
    ):
        return self._mclick(6, device=device)

    def mouse_downscroll_here(
        self,
        number_of_scrolls=1,
        device=None,
    ):
        return self._mclick(
            8,
            device=device,
            other_args=[
                "--number_of_scrolls=" + str(number_of_scrolls),
            ],
        )

    def mouse_upscroll_here(
        self,
        number_of_scrolls=1,
        device=None,
    ):
        return self._mclick(
            10,
            device=device,
            other_args=[
                "--number_of_scrolls=" + str(number_of_scrolls),
            ],
        )

    @staticmethod
    def download_and_compile_cpp_files(gcc_exe="g++"):
        apps = download_and_compile_files()
        pprint(apps)
        return apps

    def get_screenshot(self):
        return np.frombuffer(
            subprocess.run(
                f"{sconfig.mycfg_system_folder}screencap",
                capture_output=True,
                env=os.environ,
            ).stdout,
            dtype=np.uint8,
        )[16:].reshape((self.screen_height, self.screen_width, 4))[..., [2, 1, 0]]

    def save_screenshot_to_disk(self, path):
        save_bmp(
            path,
            np.frombuffer(
                subprocess.run(
                    f"{sconfig.mycfg_system_folder}screencap",
                    capture_output=True,
                    env=os.environ,
                ).stdout,
                dtype=np.uint8,
            )[16:].reshape((self.screen_height, self.screen_width, 4))[..., [2, 1, 0]],
        )

    @staticmethod
    def list_files_in_folders(folders, maxsubfolders=-1):
        return get_folder_file_complete_path(
            folders=folders, maxsubfolders=maxsubfolders
        )

    @staticmethod
    def list_all_files_in_folders_quick(folders, maxdepth=30, timeout=100000):
        if isinstance(folders, str):
            folders = [folders]
        allmycmds = []
        for f in folders:
            cmds2execute = rf'''find "{f}" -maxdepth {maxdepth} -printf "\"%M\",\"%Z\",\"%s\",\"%u\",\"%g\",\"%l\",\"%T@\",\"%U\",\"%G\",\"%m\",\"%p\",\"%f\"\n";find "{f}" -maxdepth {maxdepth} -iname ".*" -printf "\"%M\",\"%Z\",\"%s\",\"%u\",\"%g\",\"%l\",\"%T@\",\"%U\",\"%G\",\"%m\",\"%p\",\"%f\"\n"'''
            allmycmds.append(cmds2execute)
        wholecmd = ("\n".join(allmycmds)).encode("utf-8")
        return pd.read_csv(
            io.StringIO(
                _execute_command_run_shell_capture_output_open_shell_first(
                    wholecmd, timeout=timeout
                )
                .stdout.decode("utf-8", "backslashreplace")
                .strip()
            ),
            encoding="utf-8",
            sep=",",
            index_col=False,
            encoding_errors="backslashreplace",
            on_bad_lines="warn",
            engine="python",
            na_filter=False,
            quoting=1,
            names=columns_files,
            dtype=dtypes_files,
        )


# TermuAutoADB.download_and_compile_cpp_files("g++-14")

# screen_width, screen_height = get_screen_width_height()
# all_exes = {
#     "android_fragment_parser": "/data/data/com.termux/files/usr/bin/android_fragment_parser/a.out",
#     "getevent_keydumper_linux": "/data/data/com.termux/files/usr/bin/getevent_keydumper_linux/a.out",
#     "getevent_pretty_print_linux": "/data/data/com.termux/files/usr/bin/getevent_pretty_print_linux/a.out",
#     "lcp": "/data/data/com.termux/files/usr/bin/lcp/a.out",
#     "mouse_sendevent_android": "/data/data/com.termux/files/usr/bin/mouse_sendevent_android/a.out",
#     "sendevent_multicommands_type_text": "/data/data/com.termux/files/usr/bin/sendevent_multicommands_type_text/a.out",
#     "uiautomator_dump_to_csv": "/data/data/com.termux/files/usr/bin/uiautomator_dump_to_csv/a.out",
#     "uiautomator_dump_without_could_not_detect_idle_state": "/data/data/com.termux/files/usr/bin/uiautomator_dump_without_could_not_detect_idle_state/a.out",
#     "uiautomator_eventsparser_cpp": "/data/data/com.termux/files/usr/bin/uiautomator_eventsparser_cpp/a.out",
# }
# termuxauto = TermuAutoADB(
#     **all_exes,
#     deque_size_event_parser=300,
#     deque_size_lcp=300,
#     screen_width=screen_width,
#     screen_height=screen_height,
# )
# df01 = termuxauto.get_df_window_elements()
# df02 = termuxauto.get_df_uiautomator_frame(timeout=30)
# df03 = termuxauto.get_df_fragments(timeout=30)
# myscreenshot = termuxauto.get_screenshot()
# termuxauto.save_screenshot_to_disk("/sdcard/uncompressedscreenshotx.bmp")
# # save_bmp("/sdcard/uncompressedscreenshot.bmp", myscreenshot)
# df_key_events = termuxauto.get_df_all_devices_and_keys(timeout=30)
# print(df_key_events)
# my_mouse_device = df_key_events.loc[
#     df_key_events.name == "VirtualBox mouse integration"
# ].devname.iloc[0]
# my_keyboard_device = df_key_events.loc[
#     df_key_events.name == "AT Translated Set 2 keyboard"
# ].devname.iloc[0]
# termuxauto.set_mouse_device(my_mouse_device)
# termuxauto.set_keyboard_device(my_keyboard_device)
# dddd = termuxauto.get_df_uiautomator_frame(timeout=30)
# allmysdcards = termuxauto.list_files_in_folders(folders=["/sdcard"], maxsubfolders=-1)
# dodfs = False
# ddd = termuxauto.get_df_fragments(timeout=30)
# allfoldersquick = termuxauto.list_all_files_in_folders_quick(
#     folders=["/sdcard/"], maxdepth=30, timeout=100000
# )
# print(ddd)
# print(allfoldersquick)
# # termuxauto.cmd.sh_grand_all_android_rights_to_package("com.kiwibrowser.browser.dev")
# termuxauto.cmd.sh_set_some_speed_up_configs()
# if dodfs:
#     termuxauto.mouse_move_from_current_to(
#         x=500,
#         y=500,
#         sleep_time=0,
#         debug=0,
#         event_multiply=1,
#         natural_movement=1,
#         use_every_n_element=1,
#         min_x_variation=0,
#         max_x_variation=0,
#         min_y_variation=0,
#         max_y_variation=0,
#         print_device_info=1,
#         device=None,
#     )

#     termuxauto.mouse_left_click_here(device=None)
#     termuxauto.mouse_right_click_here(device=None)
#     termuxauto.mouse_middle_click_here(device=None)
#     termuxauto.mouse_upscroll_here(10, device=None)
#     termuxauto.mouse_downscroll_here(10, device=None)
#     df_uiautomator = termuxauto.get_df_uiautomator_frame(timeout=30)
#     print(df_uiautomator)
#     df_fragments = termuxauto.get_df_fragments(timeout=30)
#     print(df_fragments)
#     df_uiautomator_with_cpu_limit = termuxauto.get_df_uiautomator_frame_with_cpu_limit(
#         cpu_limit=5, timeout=30
#     )
#     print(df_uiautomator_with_cpu_limit)
#     termuxauto.write_text(
#         "hello, I am the greatest",
#         remove_accents=True,
#         min_time_key_press=0,
#         max_time_key_press=0,
#     )
#     getevent_pretty_print_prc = termuxauto.start_getevent()
#     time.sleep(5)
#     getevent_pretty_print_prc.terminate()


# def move_to_coord_and_click(x, y):
#     subprocess.run(
#         f"su -c '/data/data/com.termux/files/usr/bin/mouse_sendevent_android/a.out --x={int(x)} --y={int(y)} --action=0 --screen_width=1024 --screen_height=768 --device={my_mouse_device}'",
#         shell=True,
#         capture_output=False,
#         env=os.environ,
#     )

# while True:
#     move_to_coord_and_click(x=100, y=100)
#     move_to_coord_and_click(x=700, y=700)
#     time.sleep(1)

# evparse = EventParser(
#     cmdline=r"/data/data/com.termux/files/usr/bin/uiautomator_eventsparser_cpp/a.out",
#     deque_size=300,
# )
# evparse.start()
# try:
#     while True:
#         df = evparse.get_dataframe()
#         # print(lcat)
#         # lcat.clear_deque()
#         print(df)
#         time.sleep(5)
# except KeyboardInterrupt:
#     pass
# evparse.stop()


# lcat = LcpParser(
#     cmdline=r"/data/data/com.termux/files/usr/bin/lcp/a.out",
#     deque_size=300,
# )

# lcat.start()
# try:
#     while True:
#         df = lcat.get_dataframe()
#         # print(lcat)
#         # lcat.clear_deque()
#         print(df)
#         time.sleep(1)

# except KeyboardInterrupt:
#     pass
# lcat.stop()
