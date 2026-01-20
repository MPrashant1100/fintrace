def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total

# Function to calculate category-wise totals
def calculate_by_category(expenses):
    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category] += amount

    return category_totals        

# Combines result into one summary 
def generate_summary(expenses):
    summary = {
        "total_spent": calculate_total(expenses),
        "category_breakdown": calculate_by_category(expenses),
        "expense_count": len(expenses)
    }

    return summary
