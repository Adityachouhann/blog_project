# 📰 Django Blog API with JWT Authentication

A simple and secure **Blog Backend API** built with **Python & Django REST Framework**, featuring **JWT-based user authentication**.  
Users can register, log in, and manage blog posts (CRUD operations).

---

## 🚀 Features
✅ User Registration and Login using JWT  
✅ Create, Read, Update, and Delete Blog Posts  
✅ RESTful API built with Django REST Framework  
✅ PostgreSQL Database (Neon/Postgres)  
✅ Environment variable support with `.env`  
✅ Ready for deployment and GitHub upload  

---

## 🏗️ Project Structure
my_blog_project/
│
├── blog/ # Blog CRUD app
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── urls.py
│ └── admin.py
│
├── users/ # User Authentication app
│ ├── serializers.py
│ ├── views.py
│ ├── urls.py
│ └── admin.py
│
├── config/ # Django main config
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── asgi.py
│
├── .env # Environment variables
├── .gitignore
├── manage.py
└── requirements.txt
