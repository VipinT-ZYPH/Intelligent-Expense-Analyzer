# Intelligent Expense Analyzer – Backend (v2.1)

## Overview

Version 2.1 represents the production-ready backend layer of the Intelligent Expense Analyzer.

Built using FastAPI, PostgreSQL, and JWT-based authentication, this backend exposes secure REST APIs for managing:

- User authentication
- Income tracking
- Expense management
- Analytical summaries

The backend is modular, token-protected, and follows clean architecture principles.

---

## 🛠 Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- JWT Authentication
- Pydantic
- Uvicorn

---

## 🚀 Core Features

### 1️⃣ Authentication
- Register user (`POST /auth/register`)
- Login user (`POST /auth/login`)
- JWT token-based authorization
- Secure protected routes

### 2️⃣ Income Management
- Add income (`POST /income`)
- Fetch income (`GET /income`)

### 3️⃣ Expense Management
- Add expense (`POST /expense`)
- Fetch expenses (`GET /expense`)

### 4️⃣ Analysis Engine
- Expense summary (`GET /analysis/summary`)
- Category breakdown
- Total expense aggregation
- Backend-based analytics logic

---

## 📁 Project Structure
```
backend/
│
├── main.py
├── models.py
├── schemas.py
├── crud.py
├── database.py
├── auth.py
├── dependencies.py
├── config.py
├── requirements.txt
│
└── services/
└── analyzer.py
```
---

## ⚙️ How to Run Backend

### 1️⃣ Install Dependencies

pip install -r requirements.txt

### 2️⃣ Start Server
uvicorn main:app --reload

### 3️⃣ Access API Docs

Open in browser:

http://127.0.0.1:8000/docs

http://127.0.0.1:8000/docs

## 🔐 Authentication Flow
Register a user

Login to receive JWT token

Use Authorization: Bearer <token> for protected routes

## 📌 Notes
All expense and income routes require authentication.

Analysis is computed server-side for scalability.

Designed for frontend integration (Version 2.2).

