JWT Authentication with Django REST Framework 🛡️

این پروژه یک پیاده‌سازی کامل از احراز هویت با استفاده از JWT در Django REST Framework است. همچنین امکان لاگین با شبکه‌های اجتماعی هم وجود دارد (Google, GitHub و ...).

🚀 ویژگی‌ها

ثبت‌نام و ورود با شماره تلفن یا ایمیل

استفاده از JWT برای احراز هویت ایمن

تمدید توکن با رفرش توکن

اتصال به شبکه‌های اجتماعی (Social Authentication)

پیاده‌سازی با ساختار ماژولار و قابل توسعه

مستندسازی API با Swagger و Redoc با استفاده از drf-yasg

🛠 تکنولوژی‌ها

Python 3

Django

Django REST Framework

djangorestframework-simplejwt

dj-rest-auth

django-allauth

drf-yasg ✅

Pipenv

SQLite (برای توسعه)

⚙️ راه‌اندازی پروژه

1. کلون کردن مخزن و ورود به آن:

git clone <your-repo-url>
cd JWT_Authentication

2. ساخت محیط مجازی با pipenv:

pipenv install
pipenv shell

3. تنظیم متغیرهای محیطی

فایل .env را مطابق نمونه زیر تنظیم کنید:

SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

4. اعمال مهاجرت‌ها و اجرای سرور:

python manage.py migrate
python manage.py runserver

5. دسترسی به پنل مدیریت:

python manage.py createsuperuser

🔐 JWT Token Endpoints

URL

Method

توضیح

/api/token/

POST

دریافت Access و Refresh Token

/api/token/refresh/

POST

دریافت Access جدید با Refresh

/api/token/verify/

POST

بررسی معتبر بودن توکن

🌐 Social Auth Endpoints

/dj-rest-auth/google/

/dj-rest-auth/github/

برای استفاده نیاز به ثبت اپ در Google یا GitHub و تنظیم کلیدها در .env دارید.

📘 مستندات API (Swagger & ReDoc)

مستندات خودکار API با استفاده از drf-yasg در این آدرس‌ها در دسترس است:

Swagger UI 👉 http://localhost:8000/swagger/

Redoc UI 👉 http://localhost:8000/redoc/

نصب و راه‌اندازی drf-yasg:

pipenv install drf-yasg

اضافه کردن به INSTALLED_APPS:

'drf_yasg',

اضافه کردن به urls.py:

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="To-Do API",
      default_version='v1',
      description="مستندات API پروژه احراز هویت با JWT",
      contact=openapi.Contact(email="your@email.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

📚 منابع مفید

Django REST Framework

JWT with DRF

dj-rest-auth

django-allauth

drf-yasg Docs

Social Auth Docs

📌 نکته: اگر سؤال یا مشکلی داشتی، خوشحال می‌شم راهنمایی‌ات کنم. فقط بپرس! 😄