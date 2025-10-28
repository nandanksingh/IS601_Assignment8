# ----------------------------------------------------------
# Author: Nandan Kumar
# Date: 10/27/2025
# Assignment-8: FastAPI Calculator
# File: tests/e2e/test_e2e.py
# ----------------------------------------------------------
# Description:
# End-to-End (E2E) tests for the FastAPI Calculator web app.
# These tests simulate user interactions using Playwright
# and verify that the web interface correctly performs all
# arithmetic operations and handles errors gracefully.
# ----------------------------------------------------------

import pytest


# ----------------------------------------------------------
# Test: Homepage loads correctly
# ----------------------------------------------------------
@pytest.mark.e2e
def test_homepage_load(page, fastapi_server):
    """Verify that the homepage displays the title 'FastAPI Calculator'."""
    page.goto("http://localhost:8000")
    assert page.inner_text("h1") == "FastAPI Calculator"


# ----------------------------------------------------------
# Test: Addition operation
# ----------------------------------------------------------
@pytest.mark.e2e
def test_addition(page, fastapi_server):
    """Verify that adding two numbers shows the correct result."""
    page.goto("http://localhost:8000")
    page.fill("#a", "5")
    page.fill("#b", "7")
    page.click("button:text('Add')")
    assert page.inner_text("#result") == "Result: 12"


# ----------------------------------------------------------
# Test: Subtraction operation
# ----------------------------------------------------------
@pytest.mark.e2e
def test_subtraction(page, fastapi_server):
    """Verify that subtraction shows the correct result."""
    page.goto("http://localhost:8000")
    page.fill("#a", "15")
    page.fill("#b", "4")
    page.click("button:text('Subtract')")
    assert page.inner_text("#result") == "Result: 11"


# ----------------------------------------------------------
# Test: Multiplication operation
# ----------------------------------------------------------
@pytest.mark.e2e
def test_multiplication(page, fastapi_server):
    """Verify that multiplying two numbers gives the correct result."""
    page.goto("http://localhost:8000")
    page.fill("#a", "6")
    page.fill("#b", "3")
    page.click("button:text('Multiply')")
    assert page.inner_text("#result") == "Result: 18"


# ----------------------------------------------------------
# Test: Division operation
# ----------------------------------------------------------
@pytest.mark.e2e
def test_division(page, fastapi_server):
    """Verify that dividing two numbers shows the correct result."""
    page.goto("http://localhost:8000")
    page.fill("#a", "20")
    page.fill("#b", "5")
    page.click("button:text('Divide')")
    assert page.inner_text("#result") == "Result: 4"


# ----------------------------------------------------------
# Test: Division by zero error
# ----------------------------------------------------------
@pytest.mark.e2e
def test_divide_by_zero(page, fastapi_server):
    """Verify that dividing by zero shows an appropriate error message."""
    page.goto("http://localhost:8000")
    page.fill("#a", "10")
    page.fill("#b", "0")
    page.click("button:text('Divide')")
    assert page.inner_text("#result") == "Error: Cannot divide by zero."
