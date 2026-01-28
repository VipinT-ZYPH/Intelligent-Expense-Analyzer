from sqlalchemy.orm import Session
from models import User, Income, Expense
from auth import hash_password, verify_password

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, email: str, password: str):
    user = User(
        email=email,
        hashed_password=hash_password(password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

def create_income(db: Session, amount: float, source: str, user_id: int):
    income = Income(amount=amount, source=source, user_id=user_id)
    db.add(income)
    db.commit()
    db.refresh(income)
    return income

def create_expense(db: Session, amount: float, category: str, user_id: int):
    expense = Expense(amount=amount, category=category, user_id=user_id)
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense
