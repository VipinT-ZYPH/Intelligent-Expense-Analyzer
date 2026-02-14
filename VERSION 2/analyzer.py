from sqlalchemy import func
import models

def analyze_expenses(db, user_id):
    results = (
        db.query(
            models.Expense.category,
            func.sum(models.Expense.amount).label("total")
        )
        .filter(models.Expense.user_id == user_id)
        .group_by(models.Expense.category)
        .all()
    )

    breakdown = [
        {"category": r.category, "total": float(r.total)}
        for r in results
    ]

    return {
        "category_breakdown": breakdown
    }
