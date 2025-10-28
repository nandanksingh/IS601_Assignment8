# ----------------------------------------------------------
# Author: Nandan Kumar
# Date: 10/27/2025
# Assignment-8: FastAPI Calculator
# File: tests/e2e/conftest.py
# ----------------------------------------------------------
# Description:
# Sets up test fixtures for E2E (End-to-End) testing.
# Starts the FastAPI server before tests, launches a browser
# with Playwright, and closes everything after tests finish.
# ----------------------------------------------------------

import subprocess
import time
import pytest
from playwright.sync_api import sync_playwright
import requests


# ----------------------------------------------------------
# Fixture: Start and stop FastAPI server
# ----------------------------------------------------------
@pytest.fixture(scope="session")
def fastapi_server():
    """Start the FastAPI app before E2E tests and stop it afterward."""
    print("Starting FastAPI server...")
    server = subprocess.Popen(["python", "main.py"])
    url = "http://127.0.0.1:8000/"
    started = False

    # Wait until server responds
    for _ in range(30):
        try:
            if requests.get(url).status_code == 200:
                started = True
                print("FastAPI server is running.")
                break
        except requests.exceptions.ConnectionError:
            pass
        time.sleep(1)

    if not started:
        server.terminate()
        raise RuntimeError("Server did not start in time.")

    yield

    # Stop the server after tests
    print("Stopping FastAPI server...")
    server.terminate()
    server.wait()
    print("Server stopped successfully.")


# ----------------------------------------------------------
# Fixture: Initialize Playwright
# ----------------------------------------------------------
@pytest.fixture(scope="session")
def playwright_instance():
    """Manage Playwright instance lifecycle."""
    with sync_playwright() as playwright:
        yield playwright


# ----------------------------------------------------------
# Fixture: Launch browser for testing
# ----------------------------------------------------------
@pytest.fixture(scope="session")
def browser(playwright_instance):
    """Launch Chromium browser once per session."""
    browser = playwright_instance.chromium.launch(headless=True)
    yield browser
    browser.close()


# ----------------------------------------------------------
# Fixture: Create a new page for each test
# ----------------------------------------------------------
@pytest.fixture(scope="function")
def page(browser):
    """Open a new browser page for each test."""
    page = browser.new_page()
    yield page
    page.close()
