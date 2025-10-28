# ----------------------------------------------------------
# Author: Nandan Kumar
# Date: 10/27/2025
# Assignment-8: FastAPI Calculator
# File: tests/integration/test_fastapi_calculator.py
# ----------------------------------------------------------
# Description:
# Integration tests for FastAPI Calculator endpoints.
# These tests use FastAPI's TestClient to verify that
# API routes (/add, /subtract, /multiply, /divide)
# return correct JSON responses and proper error messages.
# ----------------------------------------------------------

import pytest
from fastapi.testclient import TestClient
from main import app

# Create a reusable test client fixture
@pytest.fixture(scope="module")
def client():
    """Fixture to create a FastAPI test client."""
    return TestClient(app)


# ----------------------------------------------------------
# Test: /add endpoint
# ----------------------------------------------------------
def test_add_endpoint(client):
    response = client.post("/add", json={"a": 5, "b": 7})
    assert response.status_code == 200
    assert response.json() == {"result": 12}


# ----------------------------------------------------------
# Test: /subtract endpoint
# ----------------------------------------------------------
def test_subtract_endpoint(client):
    response = client.post("/subtract", json={"a": 15, "b": 4})
    assert response.status_code == 200
    assert response.json() == {"result": 11}


# ----------------------------------------------------------
# Test: /multiply endpoint
# ----------------------------------------------------------
def test_multiply_endpoint(client):
    response = client.post("/multiply", json={"a": 6, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 18}


# ----------------------------------------------------------
# Test: /divide endpoint
# ----------------------------------------------------------
def test_divide_endpoint(client):
    response = client.post("/divide", json={"a": 20, "b": 5})
    assert response.status_code == 200
    assert response.json() == {"result": 4.0}


# ----------------------------------------------------------
# Test: /divide endpoint with division by zero
# ----------------------------------------------------------
def test_divide_by_zero_error(client):
    response = client.post("/divide", json={"a": 10, "b": 0})
    assert response.status_code == 400
    assert response.json() == {"error": "Cannot divide by zero."}
