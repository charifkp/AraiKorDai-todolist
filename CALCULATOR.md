# Simple Calculator

A lightweight, Python-based calculator that performs basic arithmetic operations: addition, subtraction, multiplication, and division.

## Features

- **Add**: Sum two numbers
- **Subtract**: Find the difference between two numbers
- **Multiply**: Calculate the product of two numbers
- **Divide**: Calculate the quotient (with zero-division protection)
- **Interactive CLI**: User-friendly command-line interface
- **Comprehensive Tests**: Full test coverage for all operations

## File Structure

```
src/
  calculator.py         # Core calculator class with all operations
  calculator_cli.py     # Command-line interface for the calculator
tests/
  test_calculator.py    # Unit tests for all calculator operations
```

## Usage

### As a Python Module

```python
from src.calculator import Calculator

calc = Calculator()

# Addition
result = calc.add(5, 3)          # 8

# Subtraction
result = calc.subtract(10, 4)    # 6

# Multiplication
result = calc.multiply(6, 7)     # 42

# Division
result = calc.divide(20, 4)      # 5.0

# Division by zero raises ValueError
try:
    result = calc.divide(10, 0)
except ValueError as e:
    print(f"Error: {e}")  # Error: Cannot divide by zero
```

### Via Command-Line Interface

Run the interactive calculator CLI:

```bash
python src/calculator_cli.py
```

The CLI will display a menu with the following options:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit

Follow the prompts to enter two numbers and perform the selected operation.

## Testing

Run all calculator tests:

```bash
pytest tests/test_calculator.py -v
```

The test suite includes:
- Addition tests (positive, negative, mixed signs, zero, floats)
- Subtraction tests (positive, negative, mixed signs, zero, floats)
- Multiplication tests (positive, negative, mixed signs, zero, floats)
- Division tests (positive, negative, mixed signs, floats, zero-division errors)

## Operations

### Addition
Adds two numbers and returns the sum.
- Input: Two floats
- Output: Float (sum)

### Subtraction
Subtracts the second number from the first and returns the difference.
- Input: Two floats
- Output: Float (difference)

### Multiplication
Multiplies two numbers and returns the product.
- Input: Two floats
- Output: Float (product)

### Division
Divides the first number by the second and returns the quotient.
- Input: Two floats
- Output: Float (quotient)
- Special: Raises `ValueError` if the divisor is zero

## Error Handling

The calculator handles the following error cases:
- **Division by Zero**: Raises `ValueError` with message "Cannot divide by zero"
- **Invalid Input (CLI)**: Displays error message and prompts user to enter valid numbers

## Example Session

```
Welcome to the Simple Calculator!

========================================
         SIMPLE CALCULATOR
========================================
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
========================================
Select an operation (1-5): 1
Enter first number: 15
Enter second number: 7

15.0 + 7.0 = 22.0

========================================
         SIMPLE CALCULATOR
========================================
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
========================================
Select an operation (1-5): 5

Thank you for using the Simple Calculator. Goodbye!
```
