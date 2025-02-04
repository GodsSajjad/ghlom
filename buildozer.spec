[app]
# عنوان برنامه
title = NeuralGame
# نام بسته (به صورت کوچک و بدون فاصله)
package.name = neuralgame
# دامنه بسته (به صورت معکوس دامنه‌ی وب یا هر مقدار دلخواه)
package.domain = org.example
# دایرکتوری حاوی کدهای برنامه (معمولاً ریشه‌ی پروژه)
source.dir = .
# پسوندهای فایل‌هایی که باید در بسته گنجانده شوند
source.include_exts = py,png,jpg,kv,ttf,gif
# نسخه برنامه
version = 0.1
# کتابخانه‌های مورد نیاز
requirements = python3,kivy,cython,tensorflow,numpy
# جهت صفحه نمایش (portrait یا landscape)
orientation = portrait
# اجرای برنامه بصورت تمام صفحه (اختیاری)
fullscreen = 1
# نقطه ورود برنامه
entrypoint = main.py
# اگر از bootstrap sdl2 استفاده می‌کنید (بسته به نسخه‌ی buildozer ممکن است لازم باشد)
android.bootstrap = sdl2

# مجوزهای مورد نیاز برای اندروید
android.permissions = INTERNET

# (اختیاری) تنظیمات آیکون برنامه
# icon.filename = assets/icon.png

[buildozer]
# سطح لاگ (می‌تواند 1 تا 2 یا بیشتر باشد)
log_level = 2
# هشدار در صورت اجرای buildozer به عنوان کاربر روت
warn_on_root = 1

[app:android]
# نسخه API اندروید هدف
android.api = 28
# نسخه NDK اندروید مورد استفاده (ممکن است با نسخه‌های جدید تغییر کند)
android.ndk = 21b
# معماری‌های پشتیبانی شده؛ armeabi-v7a معماری رایج است
android.arch = armeabi-v7a
