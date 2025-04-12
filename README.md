# 📝 Django Blog Project

پروژه بلاگ ساده‌ای است که با استفاده از فریم‌ورک Django ساخته شده و کاربران می‌توانند پست‌های خود را ایجاد، خواندن، ویرایش و حذف کنند. این پروژه از نماهای مبتنی بر کلاس‌های عمومی (CBV) دیجانگو استفاده می‌کند.

---

## 🚀 اجرای پروژه روی لوکال

### 🧱 پیش‌نیازها

- Python 3.10 یا بالاتر
- pip
- SQLite (پایگاه داده پیش‌فرض)

### 🛠️ مراحل نصب

````bash
# 1. کلون کردن پروژه
git clone https://github.com/yourusername/django-blog.git
cd django-blog

# 2. ایجاد محیط مجازی
python3 -m venv env
source env/bin/activate   # برای ویندوز: env\Scripts\activate

# 3. نصب وابستگی‌ها
pip install -r requirements.txt

# 4. اعمال مهاجرت‌ها
python manage.py migrate

# 5. ساخت سوپر یوزر (اختیاری)
python manage.py createsuperuser

# 6. اجرای سرور
python manage.py runserver


📍 حالا پروژه از آدرس زیر قابل دسترسیه:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## ⚙️ تنظیمات اتصال به MySQL

در فایل `store_project/settings.py` قسمت `DATABASES` باید به شکل زیر تنظیم شده باشد:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'store_db',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
````

## 📁 ساختار اصلی پروژه

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

## 🧰 تکنولوژی‌های استفاده‌شده

- Django 🌐
- Python 3.10 🐍
- MySQL 🛢️
- pipenv برای مدیریت محیط مجازی و پکیج‌ها
- Git & GitHub برای کنترل نسخه

## 📡 URLS

| Endpoint                 | Method | توضیحات                      |
| ------------------------ | ------ | ---------------------------- |
| `/post/`                 | GET    | نمایش لیست پست‌های منتشر شده |
| `/post/<int:pk>/`        | GET    | نمایش جزئیات یک پست          |
| `/create/`               | GET    | ایجاد یک پست جدید            |
| `/post/<int:pk>/update/` | GET    | ویرایش یک پست موجود          |
| `/post/<int:pk>/delete/` | GET    | حذف یک پست                   |

---

## 🧑‍💻 توسعه‌دهنده

- 👤 **وحید رجبی**
- 🔗 [گیت‌هاب من](https://github.com/VahidRajabi-2000-5)

---

## 📃 لایسنس

این پروژه به صورت آموزشی ساخته شده و استفاده از آن آزاد است.
