[app]
title = CIE MCQ Checker
package.name = mcqchecker
package.domain = org.caiehelp
source.dir = .
source.include_exts = py
version = 1.0

# Clean target dependencies 
requirements = python3,kivy,pillow

orientation = portrait
fullscreen = 0

# Force Buildozer to use the exact Android paths pre-configured on GitHub's Runner
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/27.3.13750724

# Set APIs matching NDK 27 stability baselines
android.api = 34
android.minapi = 24
android.ndk_api = 24
android.archs = arm64-v8a

android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
