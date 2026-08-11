# FastAPI & PostgreSQL Masterclass

Welcome to the ultimate step-by-step guide to building a robust, production-ready RESTful API using Python and FastAPI. This repository chronicles the journey from basic setup to advanced database relationships, authentication, and deployment configurations.

##  Tech Stack

* **Framework:** FastAPI
* **Language:** Python 3.x
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy
* **Data Validation:** Pydantic
* **Authentication:** JWT (JSON Web Tokens)
* **Database Migrations:** Alembic
* **Testing & API Interaction:** Postman

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

### Project 5: Advanced Models & User Management

* **Model Architecture:** Understanding the difference between Pydantic Models and ORM Models (Response Models).
* **User Registration:** Creating the Users table and building the registration endpoint.
* **Security:** Hashing passwords securely before saving them to the database.
* **User Retrieval:** Fetching and returning user data safely by ID.

### Project 6: Project Structuring & JWT Authentication

* **Refactoring:** Organizing routes and splitting code using FastAPI Routers (Prefixes and Tags).
* **JWT Basics:** Understanding JSON Web Tokens.
* **Login Flow:** Implementing the login process and generating tokens via `OAuth2PasswordRequestForm`.
* **Token Verification:** Ensuring users are logged in and handling expired tokens.

### Project 7: Protected Routes & Database Relationships

* **Route Protection:** Securing endpoints to ensure only authenticated users can access them.
* **Relational Databases:** Implementing Foreign Keys in PostgreSQL and SQLAlchemy.
* **Data Ownership:** Adding an `owner_id` to link resources (e.g., posts) to specific users.
* **Authorization:** Ensuring users can only update or delete their own data.
* **SQLAlchemy Relationships:** Automatically fetching a user's data alongside their posts.

### Project 8: Environment Variables & Voting/Likes System

* **Query Parameters:** Adding filtering, search, and pagination capabilities.
* **Security Configuration:** Hiding sensitive credentials using Environment Variables (`.env`).
* **System Architecture:** Designing the logic behind a Vote/Like system.
* **Implementation:** Creating the Votes table, establishing SQLAlchemy relationships, and building the voting route.

### Project 9: Data Aggregation with SQL Joins

* **SQL Joins:** Understanding database table joins conceptually.
* **SQLAlchemy Joins:** Writing join queries in Python to combine Post data with Vote counts.
* **Complex Retrieval:** Fetching single items and lists with fully aggregated join data.

### Project 10: Migrations (Alembic) & CORS

* **Database Migrations:** Understanding why schema tracking is necessary for production.
* **Alembic Setup:** Configuring Alembic, disabling SQLAlchemy's auto-table generation, and running the first migration.
* **CORS:** Configuring Cross-Origin Resource Sharing (CORS) to allow front-end applications (React, Vue, etc.) to communicate securely with the API.

---

## ⚙️ How to Run Locally

1. **Clone the repository:**
```bash
git clone 
cd <your-repo-folder>

```


2. **Create and activate a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

```


3. **Install dependencies:**
```bash
pip install -r requirements.txt

```


4. **Set up Environment Variables:**
Create a `.env` file in the root directory and add your database credentials and JWT secret key.
5. **Run the server:**
```bash
uvicorn main:app --reload

```
