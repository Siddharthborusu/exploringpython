"""
Ruff is a modern Python tool that’s incredibly fast and combines multiple tools in one:
Linting - Finding issues and potential errors
Formatting - Fixing code style automatically
Import sorting - Organizing imports cleanly
It’s beginner-friendly with clear error messages and works seamlessly with VS Code.

"""

def calculate_total(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total


shopping_cart = [
    {"name": "apple", "price": 0.5, "quantity": 6},
    {"name": "banana", "price": 0.3, "quantity": 8},
]
print(calculate_total(shopping_cart))
