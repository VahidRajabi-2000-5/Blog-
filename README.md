# وبلاگ با Django

این پروژه یک وبلاگ ساده است که با استفاده از فریم‌ورک Django توسعه داده شده است. امکانات اصلی این وبلاگ شامل مشاهده لیست پست‌ها، مشاهده جزئیات هر پست، ایجاد، ویرایش و حذف پست‌ها می‌باشد.&#8203;:contentReference[oaicite:2]{index=2}

## 🚀 راه‌اندازی پروژه در محیط محلی

### پیش‌نیازها

- :contentReference[oaicite:3]{index=3}&#8203;:contentReference[oaicite:4]{index=4}
- :contentReference[oaicite:5]{index=5}&#8203;:contentReference[oaicite:6]{index=6}
- :contentReference[oaicite:7]{index=7}&#8203;:contentReference[oaicite:8]{index=8}
- :contentReference[oaicite:9]{index=9}&#8203;:contentReference[oaicite:10]{index=10}

### مراحل نصب و راه‌اندازی

1. **کلون کردن پروژه:**

   ```bash
   git clone [URL_REPOSITORY]
   cd [PROJECT_DIRECTORY]
   ```
:contentReference[oaicite:11]{index=11}

2. **نصب وابستگی‌ها و ساخت محیط مجازی با pipenv:**

   ```bash
   pipenv install
   ```
:contentReference[oaicite:12]{index=12}

3. **فعال‌سازی محیط مجازی:**

   ```bash
   pipenv shell
   ```
:contentReference[oaicite:13]{index=13}

4. **نصب پکیج mysqlclient (ممکن است به نصب libmysqlclient-dev نیاز باشد):**

   ```bash
   pipenv install mysqlclient
   ```
:contentReference[oaicite:14]{index=14}

5. **تنظیمات دیتابیس:**

   در فایل `project_name/settings.py`، بخش `DATABASES` را به صورت زیر تنظیم کنید:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'blog_db',
           'USER': 'your_mysql_user',
           'PASSWORD': 'your_mysql_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```
:contentReference[oaicite:15]{index=15}

6. **اجرای مهاجرت‌ها:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
:contentReference[oaicite:16]{index=16}

7. **ساخت ادمین (اختیاری):**

   ```bash
   python manage.py createsuperuser
   ```
:contentReference[oaicite:17]{index=17}

8. **اجرای سرور:**

   ```bash
   python manage.py runserver
   ```
:contentReference[oaicite:18]{index=18}

:contentReference[oaicite:19]{index=19}&#8203;:contentReference[oaicite:20]{index=20}

## ساختار پروژه


```plaintext
project_name/
├── blog/               # اپلیکیشن وبلاگ
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py        # فرم‌های مربوط به پست‌ها
│   ├── models.py      # مدل Post
│   ├── tests.py
│   ├── urls.py       # مسیرهای مربوط به وبلاگ
│   └── views.py      # ویوهای مربوط به پست‌ها
├── project_name/      # تنظیمات اصلی پروژه Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py    # تنظیمات کلی پروژه
│   ├── urls.py       # آدرس‌دهی‌های اصلی پروژه
│   └── wsgi.py
├── manage.py
├── Pipfile
├── Pipfile.lock
└── ...
```
:contentReference[oaicite:21]{index=21}

## تکنولوژی‌های استفاده‌شده

- :contentReference[oaicite:22]{index=22}&#8203;:contentReference[oaicite:23]{index=23}
- :contentReference[oaicite:24]{index=24}&#8203;:contentReference[oaicite:25]{index=25}
- :contentReference[oaicite:26]{index=26}&#8203;:contentReference[oaicite:27]{index=27}
- :contentReference[oaicite:28]{index=28}&#8203;:contentReference[oaicite:29]{index=29}

## API Endpoints

:contentReference[oaicite:30]{index=30}&#8203;:contentReference[oaicite:31]{index=31}

| Endpoint                | Method | توضیحات                                 |
|-------------------------|--------|------------------------------------------|
| :contentReference[oaicite:32]{index=32}                     | :contentReference[oaicite:33]{index=33}    | :contentReference[oaicite:34]{index=34}           |
| :contentReference[oaicite:35]{index=35}             | :contentReference[oaicite:36]{index=36} | :contentReference[oaicite:37]{index=37}                   |
| :contentReference[oaicite:38]{index=38}      | :contentReference[oaicite:39]{index=39}    | :contentReference[oaicite:40]{index=40}                 |
| :contentReference[oaicite:41]{index=41} | :contentReference[oaicite:42]{index=42} | :contentReference[oaicite:43]{index=43}                         |
| :contentReference[oaicite:44]{index=44} | :contentReference[oaicite:45]{index=45} | :contentReference[oaicite:46]{index=46}                            |&#8203;:contentReference[oaicite:47]{index=47}

:contentReference[oaicite:48]{index=48}&#8203;:contentReference[oaicite:49]{index=49}

## توسعه‌دهندگان

- **[Your Name]**
  - GitHub: [YourGitHubUsername](https://github.com/YourGitHubUsername)

## لایسنس

:contentReference[oaicite:50]{index=50}&#8203;:contentReference[oaicite:51]{index=51}
