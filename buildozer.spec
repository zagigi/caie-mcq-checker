[app]
title = CIE MCQ Checker
package.name = mcqchecker
package.domain = org.caiehelp
source.dir = .
source.include_exts = py
version = 1.0

requirements = python3,kivy,pillow

orientation = portrait
fullscreen = 0

# Let Buildozer manage the NDK to avoid compilation drops, but hook into the runner's SDK
android.sdk_path = /usr/local/lib/android/sdk

android.api = 33
android.minapi = 24
android.ndk_api = 24
android.archs = arm64-v8a

android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
