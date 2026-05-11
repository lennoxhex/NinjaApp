[app]
title = NinjaScreen
package.name = ninjascreen
package.domain = com.ninja
source.dir = .
source.include_exts = html,css,js,png,jpg,json
version = 0.1

# Requerimientos mínimos para que Buildozer no falle
requirements = python3,kivy

orientation = portrait
fullscreen = 1

# Configuraciones de Android para GitHub Actions
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
android.skip_update = False

[buildozer]
log_level = 2
warn_on_root = 1
