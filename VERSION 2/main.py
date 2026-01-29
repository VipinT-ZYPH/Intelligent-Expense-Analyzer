from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from services.analyzer import analyze_expenses

import models, schemas, crud
from database import engine
from dependencies import get_db, get_current_user
from auth import create_access_token

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Expense Analyzer v2")

@app.post("/auth/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if crud.get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="User already exists")
    crud.create_user(db, user.email, user.password)
    return {"message": "User registered successfully"}

@app.post("/auth/login", response_model=schemas.Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}

@app.post("/income")
def add_income(
    income: schemas.IncomeCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return crud.create_income(db, income.amount, income.source, current_user.id)

@app.post("/expense")
def add_expense(
    expense: schemas.ExpenseCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return crud.create_expense(db, expense.amount, expense.category, current_user.id)


from services.analyzer import analyze_expenses
from dependencies import get_current_user
from models import User

@app.get("/analysis/summary")
def expense_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return analyze_expenses(db, current_user.id)
