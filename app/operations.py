# ----------------------------------------------------------
# Author: Nandan Kumar
# Date: 10/27/2025
# Assignment-8: FastAPI Calculator
# File: app/operations.py
# ----------------------------------------------------------
# Description:
# Defines core arithmetic functions for the FastAPI Calculator app.
# Each operation validates input types, logs execution, and returns
# accurate numerical results with consistent error handling.
# ----------------------------------------------------------

from typing import Union
import logging

Number = Union[int, float]

# Configure module-level logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# ----------------------------------------------------------
# Validate numeric input
# ----------------------------------------------------------
def _validate_numbers(a: Number, b: Number) -> None:
    """Validate that both inputs are numeric."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        logger.error(f"Invalid operands: a={a}, b={b}")
        raise TypeError("Both operands must be numbers.")
    return None


# ----------------------------------------------------------
# Add two numbers
# ----------------------------------------------------------
def add(a: Number, b: Number) -> Number:
    """Return the sum of two numbers."""
    _validate_numbers(a, b)
    result = a + b
    logger.info(f"Addition performed: {a} + {b} = {result}")
    return result


# ----------------------------------------------------------
# Subtract two numbers
# ----------------------------------------------------------
def subtract(a: Number, b: Number) -> Number:
    """Return the result of subtracting b from a."""
    _validate_numbers(a, b)
    result = a - b
    logger.info(f"Subtraction performed: {a} - {b} = {result}")
    return result


# ----------------------------------------------------------
# Multiply two numbers
# ----------------------------------------------------------
def multiply(a: Number, b: Number) -> Number:
    """Return the product of two numbers."""
    _validate_numbers(a, b)
    result = a * b
    logger.info(f"Multiplication performed: {a} * {b} = {result}")
    return result


# ----------------------------------------------------------
# Divide two numbers
# ----------------------------------------------------------
def divide(a: Number, b: Number) -> float:
    """Return the result of dividing a by b. Raise error if b is zero."""
    _validate_numbers(a, b)
    if b == 0:
        logger.error("Division by zero attempted.")
        raise ValueError("Cannot divide by zero.")
    result = a / b
    logger.info(f"Division performed: {a} / {b} = {result}")
    return result
