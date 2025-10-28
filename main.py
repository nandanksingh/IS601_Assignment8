# ----------------------------------------------------------
# Author: Nandan Kumar
# Date: 10/27/2025
# Assignment-8: FastAPI Calculator
# File: main.py
# ----------------------------------------------------------
# Description:
# Entry point for the FastAPI Calculator web application.
# Creates the FastAPI instance, defines routes for arithmetic
# operations, serves index.html, and includes error handling.
# ----------------------------------------------------------

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from app.operations import add, subtract, multiply, divide
import logging

# ----------------------------------------------------------
# Configure logging
# ----------------------------------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ----------------------------------------------------------
# Create FastAPI app instance
# ----------------------------------------------------------
app = FastAPI(title="FastAPI Calculator")

# ----------------------------------------------------------
# Load HTML templates
# ----------------------------------------------------------
templates = Jinja2Templates(directory="templates")


# ----------------------------------------------------------
# Pydantic model for request validation
# ----------------------------------------------------------
class Numbers(BaseModel):
    a: float
    b: float


# ----------------------------------------------------------
# Route: Health Check
# ----------------------------------------------------------
@app.get("/health")
async def health_check():
    """Return a simple health message for Docker or CI."""
    return {"status": "ok", "message": "FastAPI Calculator is running"}


# ----------------------------------------------------------
# Route: Homepage
# ----------------------------------------------------------
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Render the main calculator page."""
    return templates.TemplateResponse("index.html", {"request": request})


# ----------------------------------------------------------
# Route: Addition
# ----------------------------------------------------------
@app.post("/add")
async def add_numbers(data: Numbers):
    """Perform addition and return the result."""
    try:
        result = add(data.a, data.b)
        return {"result": result}
    except Exception as e:
        logger.error(f"Addition failed: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))


# ----------------------------------------------------------
# Route: Subtraction
# ----------------------------------------------------------
@app.post("/subtract")
async def subtract_numbers(data: Numbers):
    """Perform subtraction and return the result."""
    try:
        result = subtract(data.a, data.b)
        return {"result": result}
    except Exception as e:
        logger.error(f"Subtraction failed: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))


# ----------------------------------------------------------
# Route: Multiplication
# ----------------------------------------------------------
@app.post("/multiply")
async def multiply_numbers(data: Numbers):
    """Perform multiplication and return the result."""
    try:
        result = multiply(data.a, data.b)
        return {"result": result}
    except Exception as e:
        logger.error(f"Multiplication failed: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))


# ----------------------------------------------------------
# Route: Division
# ----------------------------------------------------------
@app.post("/divide")
async def divide_numbers(data: Numbers):
    """Perform division and handle divide-by-zero errors."""
    try:
        result = divide(data.a, data.b)
        return {"result": result}
    except ValueError as e:
        logger.warning(f"Division error: {str(e)}")
        return JSONResponse(status_code=400, content={"error": str(e)})
    except Exception as e:
        logger.error(f"Unexpected division error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


# ----------------------------------------------------------
# Main entry point
# ----------------------------------------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
