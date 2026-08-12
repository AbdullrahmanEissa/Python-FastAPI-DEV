# FastAPI & PostgreSQL Masterclass

Welcome to the ultimate step-by-step guide to building a robust, production-ready RESTful API using Python and FastAPI. This repository chronicles the journey from basic setup to advanced database relationships, authentication, and deployment configurations.

---

## Backend Development Flow (Cheat Sheet)

هذا الملخص يمثل سير العمل (Flow) الأساسي لبناء أي تطبيق Backend من الصفر وحتى النشر:

1. **الأساسيات والتحقق من البيانات (Pydantic & Routing):**
   * **الفكرة:** التأكد من صحة البيانات التي يرسلها المستخدم قبل ربط الكود بقاعدة البيانات.
   * **التنفيذ:** إنشاء كلاسات ترث من `BaseModel` لتحديد هيكل البيانات، واستخدام الروابط مثل `@app.get` و `@app.post` لاستقبال الطلبات.

2. **ربط قاعدة البيانات (SQLAlchemy & Postgres):**
   * **الفكرة:** حفظ البيانات بشكل دائم في قاعدة بيانات حقيقية بدلاً من الذاكرة العشوائية.
   * **التنفيذ:** إعداد `database.py` للاتصال بـ Postgres، وإنشاء الجداول في `models.py` باستخدام SQLAlchemy.

3. **التشفير وإدارة المستخدمين (Security):**
   * **الفكرة:** تأمين كلمات المرور الخاصة بالمستخدمين وعدم حفظها بنصوص واضحة.
   * **التنفيذ:** استخدام مكتبة `passlib` لإنشاء دوال التشفير (`hash_password`) والتحقق (`verify_password`).

4. **تنظيم الكود (Refactoring & APIRouter):**
   * **الفكرة:** تقسيم ملف `main.py` الضخم إلى ملفات أصغر لتسهيل الصيانة والقراءة.
   * **التنفيذ:** إنشاء مجلد `routers` وفصل مسارات المستخدمين والمنتجات، ثم ربطها بالتطبيق الرئيسي عبر `app.include_router()`.

5. **نظام المصادقة (Authentication & JWT):**
   * **الفكرة:** التحقق من هوية المستخدم وإعطائه صلاحيات (Token) قبل تعديل البيانات.
   * **التنفيذ:** إنشاء ملف `oauth2.py` لتوليد الـ JWT Token، وإضافة مسار `/login`، واستخدام `Depends(oauth2.get_current_user)` كحارس أمني للمسارات.

6. **الحاويات والنشر (Docker & Nginx):**
   * **الفكرة:** تغليف التطبيق ليعمل على أي سيرفر بنفس الكفاءة وبدون مشاكل في بيئة التشغيل.
   * **التنفيذ:** كتابة `Dockerfile` لتطبيق بايثون، إعداد `nginx.conf` ليعمل كـ Reverse Proxy، وجمع المكونات عبر `docker-compose.yml`.

---

## Tech Stack

* **Framework:** FastAPI
* **Language:** Python 3.x
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy
* **Data Validation:** Pydantic
* **Authentication:** JWT (JSON Web Tokens)
* **Testing & API Interaction:** Postman
* **Deployment:** Docker & Nginx

---

## Course Outline

### Project 1: Fundamentals & Environment Setup

* **Environment Preparation:** Installing Python and VS Code (Windows/Mac).
* **Virtual Environments:** Isolating project dependencies.
* **FastAPI Basics:** Initializing the framework and creating the first Path Operations and HTTP Requests.
* **API Testing:** Introduction to Postman for testing endpoints.

<img width="738" height="210" alt="image" src="https://github.com/user-attachments/assets/871d4215-f81c-4081-9815-bb6bbd17f123" />

### Project 2: Basic CRUD & Pydantic Validation

* **Schema Validation:** Enforcing strict data structures using Pydantic.
* **In-Memory CRUD:** Building Create, Read, Update, and Delete operations using local arrays.
* **Status Codes:** Implementing proper HTTP status codes for responses.
* **API Documentation:** Exploring FastAPI’s built-in automatic documentation (Swagger UI/ReDoc).
* **Postman Mastery:** Organizing requests into Postman Collections.

<img width="753" height="305" alt="image" src="https://github.com/user-attachments/assets/704bf443-244e-4c70-b206-9585ced94e01" />

### Project 3: PostgreSQL Database Introduction

* **Database Setup:** Installing PostgreSQL and pgAdmin.
* **Schema Design:** Creating database schemas and tables.
* **Raw SQL Mastery:** Writing foundational SQL queries (`SELECT`, `INSERT`, `UPDATE`, `DELETE`).
* **Advanced Querying:** Filtering with `WHERE`, utilizing operators, pattern matching with `LIKE`, ordering results, and using `LIMIT`/`OFFSET`.

<img width="1462" height="705" alt="image" src="https://github.com/user-attachments/assets/e1ffeff4-877c-4614-9c4e-738ed5fbc702" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ae68d1b3-e2a4-4f50-85b8-e973a36d2295" />

### Project 4: SQLAlchemy & Database Integration

* **ORM Introduction:** Understanding Object-Relational Mapping and configuring SQLAlchemy.
* **Connecting the App:** Bridging the Python codebase with the PostgreSQL database.
* **Real CRUD Operations:** Replacing in-memory arrays with persistent database transactions (Get All, Create, Get by ID, Delete, Update).

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/cabcd9c1-3a20-4054-9dc2-d4b87ad555a2" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/21289c0d-9e93-4531-89b5-618be3537562" />

### Project 5: Advanced Models & User Management

* **Model Architecture:** Understanding the difference between Pydantic Models and ORM Models (Response Models).
* **User Registration:** Creating the Users table and building the registration endpoint.
* **Security:** Hashing passwords securely before saving them to the database.
* **User Retrieval:** Fetching and returning user data safely by ID.

<img width="1920" height="1080" alt="Screenshot from 2026-08-11 12-52-38" src="https://github.com/user-attachments/assets/33466251-beef-40d1-af16-35d79b8c5d05" />

<img width="1920" height="1080" alt="Screenshot from 2026-08-11 12-54-10" src="https://github.com/user-attachments/assets/08075ecd-3b7f-468c-ba6f-4a5b17d3450c" />

<img width="1920" height="1080" alt="Screenshot from 2026-08-11 21-13-10" src="https://github.com/user-attachments/assets/adbbe0e3-0aad-41c5-9885-bd90d81f9e1e" />

<img width="1920" height="1080" alt="Screenshot from 2026-08-11 21-13-29" src="https://github.com/user-attachments/assets/7f1c3e4a-2b59-4ae4-9b4c-612ed6ab6f59" />

### Project 6: Project Structuring & JWT Authentication

* **Refactoring:** Organizing routes and splitting code using FastAPI Routers (Prefixes and Tags).
* **JWT Basics:** Understanding JSON Web Tokens.
* **Login Flow:** Implementing the login process and generating tokens via `OAuth2PasswordRequestForm`.
* **Token Verification:** Ensuring users are logged in and handling expired tokens.

<img width="1920" height="1080" alt="Screenshot from 2026-08-12 07-45-22" src="https://github.com/user-attachments/assets/f25b5b96-fac0-49a9-9d69-316ec4dd3178" />

<img width="1920" height="1080" alt="Screenshot from 2026-08-12 07-49-21" src="https://github.com/user-attachments/assets/bb0a561f-a8e7-42a3-9caa-605818a62f1b" />

<img width="1920" height="1080" alt="Screenshot from 2026-08-12 07-49-45" src="https://github.com/user-attachments/assets/c0d607d8-22a5-4433-817b-9db451f9965d" />

<img width="1920" height="1080" alt="Screenshot from 2026-08-12 07-49-53" src="https://github.com/user-attachments/assets/87c57fb4-734d-4e8a-9041-3a54cad39f48" />

<img width="1920" height="1080" alt="Screenshot from 2026-08-12 08-05-51" src="https://github.com/user-attachments/assets/6ce8c814-3e40-46a0-82c6-256982aaa54a" />

<img width="1920" height="1080" alt="Screenshot from 2026-08-12 08-11-49" src="https://github.com/user-attachments/assets/cb7e6ea3-d1e3-44a1-8bf3-305ca4879ad6" />

<img width="1920" height="1080" alt="Screenshot from 2026-08-12 08-15-24" src="https://github.com/user-attachments/assets/f175e3bb-54e1-4b32-8f1b-9daf88fa12b2" />

---

## ⚙️ How to Run Locally

1. **Clone the repository:**
```bash
git clone [https://github.com/AbdullrahmanEissa/Python-FastAPI-DEV/](https://github.com/AbdullrahmanEissa/Python-FastAPI-DEV/)
cd ./Python-FastAPI-DEV

```

2. **Create and activate a virtual environment:**

```bash
python -m venv venv
source ./venv/bin/activate

```

3. **Install dependencies:**

```bash
pip install -r requirements.txt

```

4. **Set up Environment Variables:**
Create a `.env` file in the root directory and add your database credentials and JWT secret key.
5. **Run the server:**

```bash
# To run locally with Uvicorn
uvicorn main:app --reload

# To run using Docker Compose (includes Nginx & PostgreSQL)
docker-compose up -d --build

```

```

```
