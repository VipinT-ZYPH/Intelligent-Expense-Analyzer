# services/analyzer.py
def analyze_expenses(expenses):
    total = sum(e.amount for e in expenses)

    by_category = {}
    for e in expenses:
        by_category[e.category] = by_category.get(e.category, 0) + e.amount

    return {
        "total_expense": total,
        "category_breakdown": by_category
    }
