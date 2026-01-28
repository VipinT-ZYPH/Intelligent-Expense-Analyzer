from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class IncomeCreate(BaseModel):
    amount: float
    source: str


class ExpenseCreate(BaseModel):
    amount: float
    category: str
