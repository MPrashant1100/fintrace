from datetime import datetime

# isinstance() → to check type
# simple conditions → to check correctness
# raise Exception → to stop program

def validate_expense(expense):
    if not isinstance(expense, dict):
        raise TypeError("Expense must be a dictionary")
    
    required_fields = ["amount", "category", "description", "date"]

    # check required fields exist
    for field in required_fields:
        if field not in expense:
            raise ValueError(f"Missing required field: {field}")
        
    # Validate amount
    amount = expense["amount"]
    if not isinstance(amount, (int, float)):    
        raise TypeError("Amount must be a number")
    
    if amount <= 0:
        raise ValueError("Amount must be greater than zero")
    
    # validate category
    category = expense["category"]
    if not isinstance(category, str) or not category.strip():
        raise ValueError("Category must be a non empty string")
    
    # validate description
    description = expense["description"]

    if not isinstance(description, str):
        raise TypeError("Description must be a string")
    
    # validate date format
    date = expense["date"]

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError( "Date must be in YYYY-MM-DD formate")    