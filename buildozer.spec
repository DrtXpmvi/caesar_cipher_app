[app]

# Your app name as shown on the device
title = Ceasar Cipher

# Package name (used for APK file and internal Android ID)
package.name = ceasar_cipher

# Domain name (reverse-style, required for Android)
package.domain = org.ceasarcipher

# Source directory of your main.py
source.dir = .

# Entry point (the main Python script)
source.main = main.py

# App versioning
version = 1.0.0
version.regex = __version__ = ['"](.*)['"]

# Application icon (make sure this file exists)
icon.filename = assets/icon.png

# Presplash image (optional)
presplash.filename = assets/presplash.png

# Supported orientations (can be portrait, landscape, all)
orientation = portrait

# Supported architectures
android.archs = armeabi-v7a, arm64-v8a

# Permissions (adjust as needed)
android.permissions = INTERNET

# Full-screen mode
fullscreen = 0

# Logging level (1 = verbose, 2 = normal)
log_level = 2

# Include specific files or folders
include_exts = py,png,jpg,kv,atlas,txt,json

# Include your app data directory if you have one
# (optional)
# source.include_exts = assets/*

# Custom application name in APK
android.entrypoint = org.kivy.android.PythonActivity
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.ndk_api = 21

# Buildozer settings
requirements = python3,kivy
requirements.source.kivy = https://github.com/kivy/kivy/archive/master.zip

# Use the latest stable build tools
android.build_tools_version = 36.1.0
android.api = 34

# Keystore configuration (for release builds)
# Uncomment and replace with your keystore info if signing release APKs
# android.release_keystore = keystore.jks
# android.release_keyalias = ceasar_cipher_key
# android.release_keyalias_passwd = mypassword
# android.release_keystore_passwd = mypassword

# Entry point arguments
# (leave empty unless you use command-line args)
args =

# Package whitelist (default)
android.whitelist =

# If True, prevents screen dimming
android.prevent_sleep = False

# If True, include debug symbols
android.debug_symbols = False

# (Auto-handled by GitHub Actions workflow)
# Don't change these:
# export BUILDOZER_ALLOW_ROOT=1
# buildozer -v android debug

[buildozer]
log_level = 2
warn_on_root = 0
