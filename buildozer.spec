[app]
title = CIE MCQ Checker
package.name = mcqchecker
package.domain = org.caiehelp
source.dir = .
source.include_exts = py

# Crucial version dependencies 
version = 1.0
requirements = python3==3.10.12,kivy==2.3.0,kivymd==1.2.0,pillow

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a

# Necessary build permissions
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
