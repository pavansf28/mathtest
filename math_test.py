# Math operation functions


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the quotient of two numbers. Handle division by zero."""
    if b == 0:
        return "Error: Division by zero is undefined."
    return a / b



# Test functions

def main():
    """Provide an interactive menu for the user to choose operations."""
    operations = {
        "1": ("Add", add),
        "2": ("Subtract", subtract),
        "3": ("Multiply", multiply),
        "4": ("Divide", divide),
    }

    while True:
        print("\nSelect operation:")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")
        print("q. Quit")

        choice = input("Enter your choice: ").strip()
        if choice == "q":
            print("Goodbye!")
            break

        if choice not in operations:
            print("Invalid selection, try again.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        name, func = operations[choice]
        try:
            result = func(a, b)
        except Exception as exc:
            print(f"Error during {name.lower()}: {exc}")
        else:
            print(f"Result of {name.lower()} is {result}")


if __name__ == "__main__":
    main()    
