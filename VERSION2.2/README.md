

# 🎨 VERSION 2.2 – Frontend README
# Intelligent Expense Analyzer – Frontend (v2.2)

## Overview

Version 2.2 is the interactive frontend layer of the Intelligent Expense Analyzer.

Built using Streamlit, this version integrates with the v2.1 FastAPI backend and provides:

- User authentication interface
- Expense & income entry forms
- Dashboard view
- Analytical insights with visualizations

---

## 🛠 Tech Stack

- Streamlit
- Requests
- Pandas
- Matplotlib
- JWT-based API communication

---

## 🚀 Core Features

### 1️⃣ User Authentication
- Register new users
- Login
- Secure session handling
- Token storage using Streamlit session state

### 2️⃣ Expense Management
- Add expense
- View expenses in tabular format
- Real-time backend sync

### 3️⃣ Dashboard
- Clean navigation layout
- Session-based user state
- Logout functionality

### 4️⃣ Insights Page
- Category-wise expense breakdown
- Total expense visualization
- Bar chart representation
- Handles empty transaction cases safely

---

## 📁 Project Structure
```
frontend/
│
├── app.py
├── config.py
│
├── api/
│ ├── auth_api.py
│ ├── expense_api.py
│ └── analysis_api.py
│
└── pages/
├── login.py
├── register.py
├── add_expense.py
├── view_expenses.py
├── dashboard.py
└── insights.py
```

---

## ⚙️ How to Run Frontend

### 1️⃣ Install Dependencies

pip install streamlit requests pandas matplotlib

### 2️⃣ Start Application
streamlit run app.py

### 3️⃣ Access App
http://localhost:8501


## 🔗 Backend Configuration

Ensure config.py contains:

BACKEND_BASE_URL = "http://127.0.0.1:8000"
REQUEST_TIMEOUT = 10


Backend must be running before starting frontend.

## ⚠️ Edge Case Handling

If user has no transactions, Insights page handles empty data gracefully.

Session token required for all expense operations.

Automatic UI feedback on success/failure actions.


