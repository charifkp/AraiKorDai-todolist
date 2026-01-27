"""Simple calculator CLI application."""

from calculator import add, subtract, multiply, divide


def main():
    """Main calculator loop."""
    print("Simple Calculator")
    print("================")
    print("Commands: add, subtract, multiply, divide, exit")
    print()

    while True:
        try:
            operation = input("Enter operation (add/subtract/multiply/divide/exit): ").strip().lower()

            if operation == "exit":
                print("Goodbye!")
                break

            if operation not in ["add", "subtract", "multiply", "divide"]:
                print("Invalid operation. Please try again.\n")
                continue

            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if operation == "add":
                result = add(a, b)
            elif operation == "subtract":
                result = subtract(a, b)
            elif operation == "multiply":
                result = multiply(a, b)
            elif operation == "divide":
                result = divide(a, b)

            print(f"Result: {result}\n")

        except ValueError as e:
            print(f"Error: {e}\n")
        except Exception as e:
            print(f"Invalid input. Please try again.\n")


if __name__ == "__main__":
    main()
