from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import models
import schemas
import crud

from database import engine
from dependencies import get_db, get_current_user
from auth import create_access_token
from services.analyzer import analyze_expenses

from models import Base

Base.metadata.create_all(bind=engine)


# ----------------------------------------
# App init
# ----------------------------------------

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Expense Analyzer v2")

# ----------------------------------------
# AUTH
# ----------------------------------------

@app.post("/auth/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if crud.get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="User already exists")
    return crud.create_user(db, user.email, user.password)


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


# ----------------------------------------
# INCOME
# ----------------------------------------

@app.post("/income")
def add_income(
    income: schemas.IncomeCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return crud.create_income(
        db,
        income.amount,
        income.source,
        user.id
    )


@app.get("/income")
def get_income(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return crud.get_incomes(db, user.id)


# ----------------------------------------
# EXPENSE
# ----------------------------------------

@app.post("/expense")
def add_expense(
    expense: schemas.ExpenseCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return crud.create_expense(
        db,
        expense.amount,
        expense.category,
        user.id
    )


@app.get("/expense")
def get_expense(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return crud.get_expenses(db, user.id)


# ----------------------------------------
# ANALYSIS (Version-1 style)
# ----------------------------------------

@app.get("/analysis/summary")
def expense_summary(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return analyze_expenses(db, user.id)



@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

