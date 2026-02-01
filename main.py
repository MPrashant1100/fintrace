from storage import load_expenses, save_expenses
from validators import validate_expense
from processor import generate_summary
from logger import get_logger
import json

logger = get_logger()

def main():
    logger.info("Loading existing expenses")
    expenses = load_expenses()

    new_expense = {
        "amount": 250,
        "category": "food",
        "description": "Lunch",
        "date": "2026-01-19"
    }

    logger.info("Validating new expense")
    validate_expense(new_expense)

    expenses.append(new_expense)
    save_expenses(expenses)
    logger.info("Expense saved successfully")

    summary = generate_summary(expenses)

    with open("reports/summary.json", "w") as f:
        json.dump(summary, f, indent=2)

    logger.info("Summary report generated")

if __name__ == "__main__":
    main()
