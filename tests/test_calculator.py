"""Unit tests for the calculator module."""

import pytest
from src.calculator import Calculator


class TestCalculator:
    """Test suite for the Calculator class."""

    @pytest.fixture
    def calc(self):
        """Create a calculator instance for testing."""
        return Calculator()

    # Addition tests
    def test_add_positive_numbers(self, calc):
        """Test addition of two positive numbers."""
        assert calc.add(2, 3) == 5

    def test_add_negative_numbers(self, calc):
        """Test addition of two negative numbers."""
        assert calc.add(-2, -3) == -5

    def test_add_mixed_signs(self, calc):
        """Test addition of numbers with different signs."""
        assert calc.add(5, -3) == 2

    def test_add_zero(self, calc):
        """Test addition with zero."""
        assert calc.add(5, 0) == 5
        assert calc.add(0, 0) == 0

    def test_add_floats(self, calc):
        """Test addition of floating-point numbers."""
        assert calc.add(2.5, 1.5) == 4.0

    # Subtraction tests
    def test_subtract_positive_numbers(self, calc):
        """Test subtraction of two positive numbers."""
        assert calc.subtract(5, 3) == 2

    def test_subtract_negative_numbers(self, calc):
        """Test subtraction of two negative numbers."""
        assert calc.subtract(-5, -3) == -2

    def test_subtract_mixed_signs(self, calc):
        """Test subtraction of numbers with different signs."""
        assert calc.subtract(5, -3) == 8
        assert calc.subtract(-5, 3) == -8

    def test_subtract_zero(self, calc):
        """Test subtraction with zero."""
        assert calc.subtract(5, 0) == 5

    def test_subtract_floats(self, calc):
        """Test subtraction of floating-point numbers."""
        assert calc.subtract(5.5, 2.3) == pytest.approx(3.2)

    # Multiplication tests
    def test_multiply_positive_numbers(self, calc):
        """Test multiplication of two positive numbers."""
        assert calc.multiply(3, 4) == 12

    def test_multiply_negative_numbers(self, calc):
        """Test multiplication of two negative numbers."""
        assert calc.multiply(-3, -4) == 12

    def test_multiply_mixed_signs(self, calc):
        """Test multiplication of numbers with different signs."""
        assert calc.multiply(3, -4) == -12
        assert calc.multiply(-3, 4) == -12

    def test_multiply_by_zero(self, calc):
        """Test multiplication by zero."""
        assert calc.multiply(5, 0) == 0
        assert calc.multiply(0, 0) == 0

    def test_multiply_floats(self, calc):
        """Test multiplication of floating-point numbers."""
        assert calc.multiply(2.5, 4.0) == 10.0

    # Division tests
    def test_divide_positive_numbers(self, calc):
        """Test division of two positive numbers."""
        assert calc.divide(10, 2) == 5

    def test_divide_negative_numbers(self, calc):
        """Test division of two negative numbers."""
        assert calc.divide(-10, -2) == 5

    def test_divide_mixed_signs(self, calc):
        """Test division of numbers with different signs."""
        assert calc.divide(10, -2) == -5
        assert calc.divide(-10, 2) == -5

    def test_divide_floats(self, calc):
        """Test division of floating-point numbers."""
        assert calc.divide(10.0, 2.5) == pytest.approx(4.0)

    def test_divide_by_zero_raises_error(self, calc):
        """Test that dividing by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(10, 0)

    def test_divide_by_zero_with_zero_dividend(self, calc):
        """Test that 0 divided by 0 raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(0, 0)
