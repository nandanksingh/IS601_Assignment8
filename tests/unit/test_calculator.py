# ----------------------------------------------------------
# Author: Nandan Kumar
# Date: 10/27/2025
# Assignment-8: FastAPI Calculator
# File: tests/unit/test_calculator.py
# ----------------------------------------------------------
# Description:
# Unit tests for arithmetic functions in app/operations.py.
# Each test validates expected outputs for valid inputs and
# ensures proper error handling for division by zero.
# ----------------------------------------------------------

import pytest
from app.operations import add, subtract, multiply, divide


# ----------------------------------------------------------
# Test add() function
# ----------------------------------------------------------
@pytest.mark.parametrize("a, b, expected", [
    (3, 5, 8),
    (-2, 6, 4),
    (2.5, 1.5, 4.0),
    (0, 0, 0)
])
def test_add(a, b, expected):
    """Check addition results with integers and floats."""
    assert add(a, b) == expected


# ----------------------------------------------------------
# Test subtract() function
# ----------------------------------------------------------
@pytest.mark.parametrize("a, b, expected", [
    (10, 4, 6),
    (4, 10, -6),
    (-3, -2, -1),
    (7.5, 2.5, 5.0)
])
def test_subtract(a, b, expected):
    """Check subtraction for positive, negative, and float values."""
    assert subtract(a, b) == expected


# ----------------------------------------------------------
# Test multiply() function
# ----------------------------------------------------------
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-2, 3, -6),
    (1.5, 2.0, 3.0),
    (0, 7, 0)
])
def test_multiply(a, b, expected):
    """Check multiplication results."""
    assert multiply(a, b) == expected


# ----------------------------------------------------------
# Test divide() function
# ----------------------------------------------------------
@pytest.mark.parametrize("a, b, expected", [
    (8, 2, 4.0),
    (-9, 3, -3.0),
    (7.5, 2.5, 3.0),
    (0, 5, 0.0)
])
def test_divide(a, b, expected):
    """Check division results for valid input cases."""
    assert divide(a, b) == expected


# ----------------------------------------------------------
# Test divide() raises ValueError for divide by zero
# ----------------------------------------------------------
def test_divide_by_zero():
    """Ensure divide() raises ValueError when dividing by zero."""
    with pytest.raises(ValueError):
        divide(10, 0)

# ----------------------------------------------------------
# Validate numbers
# ----------------------------------------------------------
def test_validate_numbers_invalid_type():
    """Ensure TypeError is raised for non-numeric input."""
    from app.operations import _validate_numbers
    with pytest.raises(TypeError):
        _validate_numbers("abc", 5)
