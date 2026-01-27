"""Simple calculator module with basic arithmetic operations."""


class Calculator:
    """A simple calculator for basic arithmetic operations."""

    def add(self, a: float, b: float) -> float:
        """Add two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Sum of a and b
        """
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Subtract two numbers.

        Args:
            a: First number
            b: Second number (subtrahend)

        Returns:
            Difference of a and b (a - b)
        """
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Product of a and b
        """
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Divide two numbers.

        Args:
            a: Dividend
            b: Divisor

        Returns:
            Quotient of a and b (a / b)

        Raises:
            ValueError: If b is zero (division by zero)
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
