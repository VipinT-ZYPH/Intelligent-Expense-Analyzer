from sqlalchemy.orm import Session
from models import Expense


def analyze_expenses(db: Session, user_id: int):
    expenses = db.query(Expense).filter(Expense.user_id == user_id).all()

    if not expenses:
        return {
            "total_expense": 0,
            "by_category": {}
        }

    total = 0
    by_category = {}

    for e in expenses:
        total += e.amount
        by_category[e.category] = by_category.get(e.category, 0) + e.amount

    return {
        "total_expense": total,
        "by_category": by_category
    }
