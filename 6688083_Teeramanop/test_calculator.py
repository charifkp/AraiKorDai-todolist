"""Unit tests for the calculator module."""

import pytest
from calculator import add, subtract, multiply, divide


class TestAdd:
    def test_add_positive_numbers(self):
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        assert add(-2, -3) == -5

    def test_add_mixed_numbers(self):
        assert add(5, -3) == 2


class TestSubtract:
    def test_subtract_positive_numbers(self):
        assert subtract(5, 3) == 2

    def test_subtract_negative_numbers(self):
        assert subtract(-2, -3) == 1

    def test_subtract_mixed_numbers(self):
        assert subtract(5, -3) == 8


class TestMultiply:
    def test_multiply_positive_numbers(self):
        assert multiply(3, 4) == 12

    def test_multiply_negative_numbers(self):
        assert multiply(-3, -4) == 12

    def test_multiply_mixed_numbers(self):
        assert multiply(3, -4) == -12

    def test_multiply_by_zero(self):
        assert multiply(5, 0) == 0


class TestDivide:
    def test_divide_positive_numbers(self):
        assert divide(10, 2) == 5

    def test_divide_negative_numbers(self):
        assert divide(-10, -2) == 5

    def test_divide_mixed_numbers(self):
        assert divide(10, -2) == -5

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)

    def test_divide_floats(self):
        assert divide(7.5, 2.5) == 3.0
