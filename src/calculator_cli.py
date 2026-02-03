"""Command-line interface for the calculator application."""

from src.calculator import Calculator


def display_menu() -> None:
    """Display the calculator menu."""
    print("\n" + "=" * 40)
    print("         SIMPLE CALCULATOR")
    print("=" * 40)
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("=" * 40)


def get_numbers() -> tuple:
    """Get two numbers from the user.

    Returns:
        A tuple of two floats

    Raises:
        ValueError: If input cannot be converted to float
    """
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Error: Please enter valid numbers.")
        return None, None


def run_calculator() -> None:
    """Run the calculator CLI application."""
    calc = Calculator()

    print("\nWelcome to the Simple Calculator!")

    while True:
        display_menu()
        choice = input("Select an operation (1-5): ").strip()

        if choice == "1":
            num1, num2 = get_numbers()
            if num1 is not None:
                result = calc.add(num1, num2)
                print(f"\n{num1} + {num2} = {result}")

        elif choice == "2":
            num1, num2 = get_numbers()
            if num1 is not None:
                result = calc.subtract(num1, num2)
                print(f"\n{num1} - {num2} = {result}")

        elif choice == "3":
            num1, num2 = get_numbers()
            if num1 is not None:
                result = calc.multiply(num1, num2)
                print(f"\n{num1} * {num2} = {result}")

        elif choice == "4":
            num1, num2 = get_numbers()
            if num1 is not None:
                try:
                    result = calc.divide(num1, num2)
                    print(f"\n{num1} / {num2} = {result}")
                except ValueError as e:
                    print(f"\nError: {e}")

        elif choice == "5":
            print("\nThank you for using the Simple Calculator. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select 1-5.")


if __name__ == "__main__":
    run_calculator()
