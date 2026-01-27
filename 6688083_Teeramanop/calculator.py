"""Simple calculator module with basic arithmetic operations."""


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate_velocity(distance: float, time: float) -> float:
    """Calculate velocity given distance and time.
    
    Args:
        distance: The distance traveled
        time: The time taken to travel the distance
        
    Returns:
        The velocity (distance / time)
        
    Raises:
        ValueError: If time is not greater than zero
    """
    if time <= 0:
        raise ValueError("Time must be greater than zero")
    return distance / time
