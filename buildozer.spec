[app]
title = CIE MCQ Checker
package.name = mcqchecker
package.domain = org.caiehelp
source.dir = .
source.include_exts = py

# CHANGED: Replaced explicit strict sub-versions with clean target names
requirements = python3,kivy,pillow

orientation = portrait
fullscreen = 0

# Fixed deployment variables matching the GitHub Actions Environment
android.api = 33
android.minapi = 24
android.ndk_api = 24
android.archs = arm64-v8a

# Necessary build permissions
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
