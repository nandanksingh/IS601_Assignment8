##  **Assignment 8 – FastAPI Calculator**

**Author:** Nandan Kumar
**Date:** October 27, 2025

---

##  **Project Overview**

This project implements a **FastAPI-based web calculator** that performs four basic arithmetic operations—**addition**, **subtraction**, **multiplication**, and **division**—through a modern web interface and RESTful API endpoints.

It demonstrates the **full web development workflow**:
from backend development and frontend integration to **automated testing**, **logging**, **version control**, and **continuous integration (CI)** using **GitHub Actions** and **Docker**.

---

##  **Learning Objectives**

Through this assignment, I learned to:

* Develop a **FastAPI** web application with RESTful API endpoints
* Integrate **frontend (HTML, CSS, JS)** with backend logic
* Implement **unit**, **integration**, and **end-to-end (E2E)** testing using **Pytest** and **Playwright**
* Add **structured logging** for debugging and transparency
* Use **Git** and **GitHub** for version control
* Set up **Continuous Integration** using **GitHub Actions**
* Containerize the app using **Docker and docker-compose**

---

##  **Application Structure**
--------------------------------------------------------------------------------------------------- 
| **app/operations.py**                            | Contains all arithmetic functions and validation logic. Includes error handling, logging, and numeric input verification. |
| **app/**init**.py**                              | Initializes the `app` package and makes it importable within FastAPI.                                                     |
| **templates/index.html**                         | Frontend calculator UI using HTML, CSS, and JavaScript. Sends API requests and dynamically displays results.              |
| **tests/unit/test_calculator.py**                | Tests individual arithmetic functions to ensure correct mathematical behavior.                                            |
| **tests/integration/test_fastapi_calculator.py** | Tests FastAPI API endpoints for addition, subtraction, multiplication, and division.                                      |
| **tests/e2e/test_e2e.py**                        | Performs full browser-based End-to-End testing using Playwright to simulate user actions.                                 |
| **Dockerfile**                                   | Defines how to build the Docker image for the FastAPI Calculator application.                                             |
| **docker-compose.yml**                           | Manages and runs the FastAPI application inside a containerized environment.                                              |
| **main.py**                                      | Entry point of the FastAPI application that serves both the frontend and backend APIs.                                    |
| **pytest.ini**                                   | Configures Pytest options such as test paths, coverage threshold, and test markers.                                       |
| **requirements.txt**                             | Lists all required dependencies for the project including FastAPI, Pytest, and Playwright.                                |


---

##  **Setup and Installation**

### ** Clone the Repository**

```bash
git clone https://github.com/nandanksingh/IS601_Assignment8.git
cd IS601_Assignment8
```

### ** Create and Activate Virtual Environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

### ** Install Dependencies**

```bash
pip install -r requirements.txt
```

### ** Run the FastAPI Application**

```bash
uvicorn main:app --reload
```

Then open the browser:
👉 **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

##  **Running with Docker**

You can also containerize and run the app using Docker.

### **Build and Run Container**

```bash
docker-compose up --build
```

### **Stop the Container**

```bash
docker-compose down
```

Once the container is running, access the application via:
👉 **[http://localhost:8000](http://localhost:8000)**

---

##  **Understanding How It Works**

### **Backend (FastAPI)**

Handles computation and serves results as JSON:

```python
@app.post("/add")
async def add_numbers(numbers: Numbers):
    result = add(numbers.a, numbers.b)
    logger.info(f"Addition performed: {numbers.a} + {numbers.b} = {result}")
    return {"result": result}
```

### **Frontend (index.html)**

Collects user input, sends API requests, and displays results:

```javascript
async function calculate(operation) {
    const a = document.getElementById("a").value;
    const b = document.getElementById("b").value;
    const response = await fetch(`/${operation}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ a: parseFloat(a), b: parseFloat(b) })
    });
    const data = await response.json();
    document.getElementById("result").innerText = `Result: ${data.result}`;
}
```

---


## **Testing and Code Coverage**

The project includes **unit**, **integration**, and **E2E** tests.

### **Run All Tests**

```bash
pytest -v --cov=app --cov-report=term-missing
```

### **Run Only E2E Tests**

```bash
pytest -m "e2e" --headed -v
```

**Test Breakdown**

| Test Type         | Location            | Description                                   |
| ----------------- | ------------------- | --------------------------------------------- |
| Unit Tests        | `tests/unit`        | Verify arithmetic functions individually      |
| Integration Tests | `tests/integration` | Validate FastAPI endpoints and responses      |
| End-to-End Tests  | `tests/e2e`         | Simulate browser interactions with Playwright |

**Final Coverage:** **100%**

---


The workflow ensures:

* All tests pass before merging
* Code quality and coverage remain consistent
* CI pipeline visible in **GitHub Actions tab**

---
##  **Reflection**

This project provided hands-on experience with **modern web application architecture** using **FastAPI** and **Python**.
I learned how **unit, integration, and E2E testing** work together to ensure reliability, and how **GitHub Actions** automates the testing process for continuous integration.
Dockerization improved my understanding of containerized development environments, ensuring consistent builds across systems.

Achieving **100% code coverage** strengthened my understanding of **test-driven development (TDD)** and professional software workflows.

---

##  **Technology Stack**

| Category         | Tools                   |
| ---------------- | ----------------------- |
| Language         | Python 3.12             |
| Framework        | FastAPI                 |
| Frontend         | HTML5, CSS3, JavaScript |
| Testing          | Pytest, Playwright      |
| CI/CD            | GitHub Actions          |
| Containerization | Docker, Docker Compose  |
| Server           | Uvicorn                 |
| Logging          | Python logging module   |

---

## **Conclusion**

The **FastAPI Calculator** is a fully functional and tested web application that integrates modern **web development**, **testing**, and **CI/CD** practices.
It serves as a strong foundation for more complex API-driven applications in real-world scenarios.

---

