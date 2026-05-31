# System Modules
import sys
import os

# Installed Modules
import pytest

# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import area_of_circle, get_nth_fibonacci   # noqa: E402


def test_area_of_circle_positive_radius():
    """Test with a positive radius."""
    # Arrange
    radius = 1

    # Act
    result = area_of_circle(radius)

    # Assert
    assert abs(result - 3.14159) < 1e-5


def test_area_of_circle_zero_radius():
    """Test with a radius of zero."""
    # Arrange
    radius = 0

    # Act
    result = area_of_circle(radius)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_zero():
    """Test with n=0."""
    # Arrange
    n = 0

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_one():
    """Test with n=1."""
    # Arrange
    n = 1

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 1


def test_area_of_circle_negative_radius_raises():
    """Test that a negative radius raises ValueError."""
    with pytest.raises(ValueError, match="Radius cannot be negative"):
        area_of_circle(-1)


def test_get_nth_fibonacci_negative_raises():
    """Test that a negative Fibonacci index raises ValueError."""
    with pytest.raises(ValueError, match="n cannot be negative"):
        get_nth_fibonacci(-5)


def test_get_nth_fibonacci_larger_value():
    """Test a larger Fibonacci value to cover the iterative branch."""
    assert get_nth_fibonacci(10) == 55


def test_area_of_circle_float_radius():
    """Test area calculation with a float radius."""
    assert abs(area_of_circle(2.5) - (math.pi * 2.5 ** 2)) < 1e-9


