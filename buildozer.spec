[app]
title = CIE MCQ Checker
package.name = mcqchecker
package.domain = org.caiehelp
source.dir = .
source.include_exts = py

# Crucial app identification lines
version = 1.0

# Clean target dependencies 
requirements = python3,kivy,pillow

orientation = portrait
fullscreen = 0

# Deployment variables matching the GitHub Environment
android.api = 33
android.minapi = 24
android.ndk_api = 24
android.archs = arm64-v8a

# Necessary build permissions
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
