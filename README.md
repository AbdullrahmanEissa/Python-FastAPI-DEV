# FastAPI & PostgreSQL Masterclass

Welcome to the ultimate step-by-step guide to building a robust, production-ready RESTful API using Python and FastAPI. This documentation outlines the complete engineering lifecycle, from basic setup and architectural design to advanced asynchronous database relationships, security, and deployment configurations.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/dbfb86be-274b-4d1f-a37a-b154371615dc" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e9ad1fa0-fdaa-489b-a670-9c322cdf5bcf" />



---

## Tech Stack

* **Framework:** FastAPI
* **Language:** Python 3.x
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy (Async)
* **Database Driver:** Asyncpg
* **Data Validation:** Pydantic
* **Authentication:** JWT (JSON Web Tokens)
* **Testing:** Postman / Swagger UI
* **Deployment:** Docker, Nginx, Kubernetes

---

## Getting Started: Local Setup & Testing

### How to Run Locally

1. **Clone the repository:**

```bash
git clone https://github.com/AbdullrahmanEissa/Python-FastAPI-DEV/
cd ./Python-FastAPI-DEV
cd ./fastapi-async-fullapp

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
docker compose up -d --build

```

### API Testing Toolkit (Swagger UI Guide)

To easily verify that the application and database are working correctly, navigate to `http://localhost/docs` (or `[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)` if running locally without Docker) and follow this exact sequence:

1. **Add a New User**
* **Endpoint:** `POST /users/`
* **Action:** Click *Try it out*.
* **Request Body:**
```json
{
  "email": "test@mail.com",
  "password": "password123"
}

```


* **Execute:** You should receive a `201 Created` response with the user's ID.


2. **Login & Authorize**
* **Action:** Scroll to the top of the page and click the **Authorize** button (the lock icon).
* **Credentials:**
* Username: `test@mail.com`
* Password: `password123`


* **Execute:** Click *Authorize*, then *Close*. All lock icons should now be locked, meaning your JWT token is active.


3. **Add an Item**
* **Endpoint:** `POST /items/`
* **Action:** Click *Try it out*.
* **Request Body:**
```json
{
  "name": "Mechanical Keyboard",
  "description": "RGB mechanical keyboard with blue switches"
}

```


* **Execute:** You should receive a `201 Created` response. Note the returned `"id"`.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7272f2c8-b99e-4711-83f8-70e697e199ab" />



4. **Find the Item in DB**
* **Endpoint:** `GET /items/{item_id}`
* **Action:** Click *Try it out*.
* **Input:** Enter the ID of the item you just created.
* **Execute:** You should receive a `200 OK` response with the item's details.

  <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/0cfb6ac8-dc31-438d-8aaf-1f6cff084b79" />



5. **Delete the Item**
* **Endpoint:** `DELETE /items/{item_id}`
* **Action:** Click *Try it out*.
* **Input:** Enter the item ID.
* **Execute:** You should receive a `204 No Content` response.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/19edce11-d569-4d28-8cd1-9d042c40d95e" />

---

## Advanced Architecture: Asynchronous Migration

This application was migrated from a traditional Synchronous (Blocking) architecture to a modern, high-performance Asynchronous (Non-blocking) architecture. This allows the server to handle thousands of concurrent requests efficiently without freezing during I/O operations.

### Core Technical Concepts

* **Sync vs. Async (Blocking vs. Non-Blocking):**
* **Sync:** The application executes tasks sequentially. If a database query takes time, the entire server thread blocks and cannot serve other users.
* **Async:** The application sends the query to the database and uses `await` to pause the task. The server is freed up to serve other users while waiting. Once the database replies, the task resumes.


* **The Event Loop:**
The engine behind Async. It is a single thread that continuously monitors tasks. When it hits an `await`, it shelves that task and moves to the next ready task, ensuring the CPU is never idle during network waits.
* **Concurrency:**
Handling multiple tasks at the same time by intelligently switching between them during wait periods.
* **Connection Pooling:**
To prevent the async app from overwhelming the database by opening thousands of simultaneous connections, a Connection Pool is utilized to recycle a fixed number of active connections.

### Implementation Details

1. **Database Driver Upgrade (`requirements.txt`)**
Replaced the synchronous `psycopg2-binary` with `asyncpg`, a high-speed, purely asynchronous PostgreSQL driver.
2. **Database Configuration (`database.py`)**
Updated the URL scheme to `postgresql+asyncpg://`. Replaced `create_engine` with `create_async_engine`, and `SessionLocal` with an `AsyncSession` factory.
3. **Application Lifespan (`main.py`)**
Implemented a FastAPI `@asynccontextmanager` called `lifespan`. Async engines cannot execute synchronous table creation directly, so `await conn.run_sync(models.Base.metadata.create_all)` is used to ensure tables are safely generated before accepting traffic.
4. **Refactoring the Routers (`routers/`)**
Converted route functions to `async def`. Upgraded queries to SQLAlchemy 2.0 syntax (e.g., `await db.execute(select(models.User))`). Added the `await` keyword before every database execution, commit, and refresh.
5. **Unchanged Modules**
`models.py` (Schema definition), `schemas.py` (In-memory validation), and `utils.py` (CPU-Bound password hashing) remained synchronous as they do not involve I/O waits.

---

## Backend Development Workflow

This section outlines the standard workflow for building a FastAPI application from scratch to production.

### Phase 1: Engineering Design

Before writing code, the architecture must be clearly mapped out.

1. **Identify Entities:** Define the core database tables (e.g., User, Item).
2. **Database Modeling:** Define columns and data types (e.g., ID as integer, Email as unique string).
3. **Validation Schemas:**
* **Input (Create):** What data is required from the client?
* **Output (Response):** What data is safely returned to the client (excluding passwords)?


4. **Routing Design:** Define HTTP methods, paths, and security dependencies.

### Phase 2: Project Foundation & Boilerplates

1. **Environment Setup:** Create the virtual environment and install dependencies.
2. **Database Engine (`database.py`):** Establish the connection URL, async engine, and session makers.
3. **Security Utilities (`utils.py`):** Configure the bcrypt hashing context.
4. **Authentication Logic (`oauth2.py`):** Setup JWT token generation and verification.

### Phase 3: Application Logic (Implementation)

1. **Define Models (`models.py`):** Translate the engineering design into SQLAlchemy ORM classes.
2. **Define Schemas (`schemas.py`):** Translate the design into Pydantic models.
3. **Initialize Application (`main.py`):** Instantiate the FastAPI app and configure the database lifespan events.

> **Testing Checkpoint 1 (Database Verification):** Run the server locally and use a database client (e.g., pgAdmin) to verify that tables and columns were created successfully.

4. **Develop Routers (`routers/`):** Implement the CRUD endpoints for authentication, users, and items.
5. **Wire Routers:** Include the routers in the main application executable.

> **Testing Checkpoint 2 (API Verification):** Access the Swagger UI documentation to test user registration, token generation, and authorized CRUD operations.

### Phase 4: Production Preparation

1. **CORS Configuration:** Configure Cross-Origin Resource Sharing in `main.py` to allow frontend clients to communicate with the API.
2. **Dockerization:** Write the `Dockerfile` to package the application.
3. **Reverse Proxy:** Configure `nginx.conf` to handle incoming internet traffic.
4. **Orchestration:** Bind the application, database, and proxy together using `docker-compose.yml`.

> **Testing Checkpoint 3 (Production Verification):** Build and run the Docker containers. Access the API through the Nginx proxy port to ensure internal container networking is fully functional.

---

## Production Deployment Boilerplates

### Docker Integration

When moving a FastAPI application to a Dockerized production environment, these standard adjustments are required:

**1. Dynamic Database URL (`database.py`)**
Always use environment variables to dynamically inject the database URL. Hardcoding `localhost` will fail inside Docker networks.

```python
import os
from sqlalchemy.ext.asyncio import create_async_engine

SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql+asyncpg://postgres:1@localhost/postgres"
)
engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

```

**2. Exposing the Server Interface (`Dockerfile`)**
You must explicitly bind the host to `0.0.0.0` to allow external traffic into the container.

```dockerfile
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

```

**3. Cross-Origin Resource Sharing (`main.py`)**

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"] 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

```

**4. Nginx Reverse Proxy (`nginx.conf`)**
Nginx acts as the entry point, handling worker connections and forwarding client headers to the backend service. Note that Docker uses the service name (`fastapi_app`) instead of localhost for internal routing.

```nginx
worker_processes auto;

events {
    worker_connections 1024;
}

http {
    server {
        listen 80;
        server_name _; 

        location / {
            proxy_pass http://fastapi_app:8000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
}

```

### Kubernetes (K8s) Architecture

Transitioning to Kubernetes requires separating components: APIs are Stateless (Deployments) and Databases are Stateful (StatefulSets).

**1. Database Boilerplate (StatefulSet + Headless Service)**

```yaml
apiVersion: v1
kind: Service
metadata:
  name: postgres-service
spec:
  clusterIP: None
  ports:
  - port: 5432
  selector:
    app: postgres
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: postgres-statefulset
spec:
  serviceName: "postgres-service"
  replicas: 1
  selector:
    matchLabels:
      app: postgres
  template:
    metadata:
      labels:
        app: postgres
    spec:
      containers:
      - name: postgres
        image: postgres:15-alpine
        env:
        - name: POSTGRES_USER
          value: "postgres"
        - name: POSTGRES_PASSWORD
          value: "1"
        - name: POSTGRES_DB
          value: "postgres"
        ports:
        - containerPort: 5432
        volumeMounts:
        - name: postgres-storage
          mountPath: /var/lib/postgresql/data
  volumeClaimTemplates:
  - metadata:
      name: postgres-storage
    spec:
      accessModes: [ "ReadWriteOnce" ]
      resources:
        requests:
          storage: 1Gi

```

**2. API Boilerplate (Deployment + LoadBalancer Service)**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fastapi-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: fastapi
  template:
    metadata:
      labels:
        app: fastapi
    spec:
      containers:
      - name: fastapi
        image: your-dockerhub-username/fastapi-backend:latest 
        ports:
        - containerPort: 8000
        env:
        - name: DATABASE_URL
          value: "postgresql+asyncpg://postgres:1@postgres-service:5432/postgres"
---
apiVersion: v1
kind: Service
metadata:
  name: fastapi-service
spec:
  type: LoadBalancer
  ports:
  - port: 80
    targetPort: 8000
  selector:
    app: fastapi

```

---

## Course Outline & Project History

### Project 1: Fundamentals & Environment Setup

* **Environment Preparation:** Installing Python and VS Code.
* **Virtual Environments:** Isolating project dependencies.
* **FastAPI Basics:** Initializing the framework and creating HTTP Requests.
* **API Testing:** Introduction to Postman.

### Project 2: Basic CRUD & Pydantic Validation

* **Schema Validation:** Enforcing strict data structures using Pydantic.
* **In-Memory CRUD:** Building Create, Read, Update, and Delete operations using local arrays.
* **Status Codes:** Implementing proper HTTP status codes.
* **API Documentation:** Exploring automatic documentation (Swagger UI/ReDoc).
* **Postman Mastery:** Organizing requests into Collections.

### Project 3: PostgreSQL Database Introduction

* **Database Setup:** Installing PostgreSQL and pgAdmin.
* **Schema Design:** Creating database schemas and tables.
* **Raw SQL Mastery:** Writing foundational SQL queries.
* **Advanced Querying:** Filtering, pattern matching, and ordering results.

### Project 4: SQLAlchemy & Database Integration

* **ORM Introduction:** Understanding Object-Relational Mapping.
* **Connecting the App:** Bridging the Python codebase with PostgreSQL.
* **Real CRUD Operations:** Replacing in-memory arrays with persistent database transactions.

### Project 5: Advanced Models & User Management

* **Model Architecture:** Pydantic Models vs. ORM Models.
* **User Registration:** Creating endpoints for user creation.
* **Security:** Hashing passwords securely.
* **User Retrieval:** Fetching data safely by ID.

### Project 6: Project Structuring & JWT Authentication

* **Refactoring:** Organizing routes using FastAPI Routers.
* **JWT Basics:** Understanding JSON Web Tokens.
* **Login Flow:** Implementing authentication endpoints.
* **Token Verification:** Ensuring users are logged in and handling token expiration.
