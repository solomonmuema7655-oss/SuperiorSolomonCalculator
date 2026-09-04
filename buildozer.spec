[app]

title = Superior Solomon Scientific Calculator
package.name = superiorsolomoncalculator
package.domain = org.siyomacodingprograms

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas

version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.archs = arm64-v8a, armeabi-v7a

android.allow_backup = True

android.api = 35
android.minapi = 21

android.accept_sdk_license = True

[buildozer]

log_level = 2
warn_on_root = 0
