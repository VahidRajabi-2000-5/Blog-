# 📝 Django Blog Project

پروژه بلاگ ساده‌ای است که با استفاده از فریم‌ورک Django ساخته شده و کاربران می‌توانند پست‌های خود را ایجاد، خواندن، ویرایش و حذف کنند. این پروژه از نماهای مبتنی بر کلاس‌های عمومی (CBV) دیجانگو استفاده
می‌کند.

## 🚀 راه‌اندازی پروژه در محیط محلی

### پیش‌نیازها

- Python 3.10 یا بالاتر
- pipenv
- MySQL (نصب و راه‌اندازی شده)
- ایجاد دیتابیس MySQL با نام دلخواه (مثلاً `bookstore_db`)

### مراحل نصب و راه‌اندازی

1. **کلون کردن پروژه:**

   ```bash
    git@github.com:VahidRajabi-2000-5/Blog-.git
    cd django-blog
   ```

2. **نصب وابستگی‌ها و ساخت محیط مجازی با pipenv:**

   ```bash
   pipenv install
   ```

3. **فعال‌سازی محیط مجازی:**

   ```bash
   pipenv shell
   ```

4. **نصب پکیج mysqlclient (ممکن است به نصب libmysqlclient-dev نیاز باشد):**

   ```bash
   pipenv install mysqlclient   
   ```

5. **تنظیمات دیتابیس:**

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'post_db',
           'USER': 'your_mysql_user',
           'PASSWORD': 'your_mysql_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

6. **اجرای مهاجرت‌ها:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **ساخت ادمین (اختیاری):**

   ```bash
   python manage.py createsuperuser
   ```

8. **اجرای سرور:**

   ```bash
   python manage.py runserver
   ```

حالا پروژه در آدرس [http://127.0.0.1:8000/](http://127.0.0.1:8000/) در دسترس است.

## ساختار پروژه

```
django_blog/
├── blog/                  # اپلیکیشن بلاگ
│   ├── models.py          # مدل‌ها: Post
│   ├── views.py           # ویوها: PostListView, PostDetailView, ...
│   ├── forms.py           # فرم‌ها برای ایجاد و ویرایش پست‌ها
│   ├── urls.py            # آدرس‌دهی اپلیکیشن بلاگ
├── django_blog/           # تنظیمات اصلی پروژه Django
│   ├── settings.py
│   ├── urls.py
├── manage.py
├── requirements.txt       # فایل وابستگی‌ها
└── ...
```

## تکنولوژی‌های استفاده‌شده

- Django
- MySQL
- pipenv برای مدیریت محیط مجازی و وابستگی‌ها
- Git & GitHub برای کنترل نسخه

## 📡 URLS

| Endpoint                 | Method | توضیحات                      |
| ------------------------ | ------ | ---------------------------- |
| `/post/`                 | GET    | نمایش لیست پست‌های منتشر شده |
| `/post/<int:pk>/`        | GET    | نمایش جزئیات یک پست          |
| `/create/`               | GET    | ایجاد یک پست جدید            |
| `/post/<int:pk>/update/` | GET    | ویرایش یک پست موجود          |
| `/post/<int:pk>/delete/` | GET    | حذف یک پست                   |

## توسعه‌دهندگان

- **وحید رجبی**
  - GitHub: [VahidRajabi-2000-5](https://github.com/VahidRajabi-2000-5)

## لایسنس

این پروژه به صورت آموزشی ساخته شده و استفاده از آن آزاد است.
