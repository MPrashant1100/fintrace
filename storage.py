import json
import os

DATA_FILE = "data/expense.json"

# Load expenses
def load_expenses():
    if not os.path.exists(DATA_FILE):
        return[]
    
    with open(DATA_FILE, "r") as f:
        return json.load(f)
    
# Save expenses
def save_expenses(expenses):                    # takes full list of expenses
    with open(DATA_FILE, "w") as f:             # overwrites file with updated list
        json.dump(expenses, f, indent=2)        # indent=2 → readable JSON