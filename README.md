## **Assignment 8 – FastAPI Calculator**

**Author:** Nandan Kumar
**Date:** October 27, 2025

---

## **Project Overview**

This project implements a **FastAPI-based web calculator** that performs four basic arithmetic operations—**addition**, **subtraction**, **multiplication**, and **division**—through a modern web interface and RESTful API endpoints.

It demonstrates the **complete web development lifecycle**, from backend and frontend integration to **automated testing**, **logging**, **containerization**, and **continuous integration (CI)** using **GitHub Actions** and **Docker**.

---

## **Learning Objectives**

Through this assignment, I learned to:

* Develop a **FastAPI** web application with RESTful API endpoints
* Integrate **frontend (HTML, CSS, JavaScript)** with backend logic
* Implement **unit**, **integration**, and **end-to-end (E2E)** testing using **Pytest** and **Playwright**
* Add **structured logging** for monitoring and debugging
* Manage version control using **Git and GitHub**
* Automate workflows with **GitHub Actions**
* Containerize and deploy the application using **Docker and Docker Compose**

---

## **Application Structure**

| File                                             | Description                                                                         |
| ------------------------------------------------ | ----------------------------------------------------------------------------------- |
| **app/operations.py**                            | Contains arithmetic functions and validation logic with error handling and logging. |
| **templates/index.html**                         | Frontend calculator UI with JavaScript-based interaction.                           |
| **tests/unit/test_calculator.py**                | Unit tests for arithmetic operations.                                               |
| **tests/integration/test_fastapi_calculator.py** | Integration tests for API endpoints.                                                |
| **tests/e2e/test_e2e.py**                        | End-to-end Playwright tests simulating real user behavior.                          |
| **Dockerfile**                                   | Defines how the Docker image is built for the application.                          |
| **docker-compose.yml**                           | Manages and runs the application in a containerized environment.                    |
| **main.py**                                      | Main FastAPI entry point for backend and frontend routes.                           |
| **pytest.ini**                                   | Configures test behavior, coverage, and warnings.                                   |
| **requirements.txt**                             | Lists project dependencies.                                                         |

---

## **Setup and Installation**

### **1. Clone the Repository**

```bash
git clone https://github.com/nandanksingh/IS601_Assignment8.git
cd IS601_Assignment8
```

### **2. Create and Activate Virtual Environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4. Run the FastAPI Application**

```bash
uvicorn main:app --reload
```

Then open your browser at:
👉 **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## **Running with Docker**

This project is fully containerized for portability and deployment consistency.

### **1. Build and Run using Docker Compose**

```bash
docker-compose up --build
```

Access the app at:
👉 **[http://localhost:8000](http://localhost:8000)**

### **2. Stop the Container**

```bash
docker-compose down
```

---

## **Published Docker Image**

The pre-built image is available publicly on **Docker Hub**:

🔗 **Docker Hub Repository:**
[https://hub.docker.com/r/nandanksingh/module8_fastapi_calculator](https://hub.docker.com/r/nandanksingh/module8_fastapi_calculator)

### **Pull the Image**

```bash
docker pull nandanksingh/module8_fastapi_calculator:latest
```

### **Run the Container**

```bash
docker run -d -p 8000:8000 nandanksingh/module8_fastapi_calculator:latest
```

### **Verify the Deployment**

* Web App: [http://localhost:8000](http://localhost:8000)
* Health Check: [http://localhost:8000/health](http://localhost:8000/health)

---

## **Testing and Code Coverage**

The project includes **Unit**, **Integration**, and **E2E** tests.
All tests run automatically via **GitHub Actions** using the workflow file
`.github/workflows/test.yml`, which enforces a **90% coverage threshold**.

---

### ** Test Execution Commands**

#### **Run All Tests (Unit + Integration + E2E)**

```bash
pytest -v --cov=app --cov=main --cov-report=term-missing --cov-fail-under=90
```

#### **Run Only Unit + Integration Tests**

```bash
pytest -m "not e2e" --cov=app --cov=main
```

#### **Run Only E2E Tests (Playwright)**

```bash
pytest -m "e2e" --headed -v
```

---

### ** Test Categories**

| Test Type             | Location            | Description                                          |
| --------------------- | ------------------- | ---------------------------------------------------- |
| **Unit Tests**        | `tests/unit`        | Validate arithmetic logic in `operations.py`         |
| **Integration Tests** | `tests/integration` | Verify FastAPI API routes and JSON responses         |
| **End-to-End Tests**  | `tests/e2e`         | Simulate browser-based interactions using Playwright |

---

### ** Coverage Summary**

| Category                         | Coverage         | Status    |
| -------------------------------- | ---------------- | --------- |
| **Unit Tests**                   | 100%             |  Passed   |
| **Integration Tests**            | 100%             |  Passed   |
| **End-to-End Tests**             | Functional       |  Passed   |


---

### ** GitHub Actions Workflow Highlights**

| Stage        | Description                                                   |
| ------------ | ------------------------------------------------------------- |
| **Test**     | Runs Unit + Integration + E2E tests                           |
| **Security** | Performs vulnerability scanning using Trivy                   |
| **Deploy**   | Builds and pushes verified Docker image to Docker Hub         |

Sample command from workflow:

```yaml
pytest --cov=app --cov=main --cov-report=term-missing --cov-fail-under=90 -m "not e2e"
pytest -m "e2e" --headed -v
```

---

## **Reflection**

This project provided practical experience with **modern web development workflows** integrating:

* FastAPI for backend APIs
* Pytest and Playwright for multi-level testing
* Docker for consistent environment deployment
* GitHub Actions for CI/CD automation

Achieving **100% unit and integration coverage**, with **functional E2E tests**, helped strengthen my understanding of test-driven development and DevOps best practices.

---

## **Technology Stack**

| Category         | Tools                  |
| ---------------- | ---------------------- |
| Language         | Python 3.12            |
| Framework        | FastAPI                |
| Frontend         | HTML, CSS, JavaScript  |
| Testing          | Pytest, Playwright     |
| CI/CD            | GitHub Actions         |
| Containerization | Docker, Docker Compose |
| Deployment       | Docker Hub             |
| Logging          | Python Logging Module  |
| Server           | Uvicorn                |

---

## **Conclusion**

The **FastAPI Calculator** is a fully functional and containerized web application that demonstrates the integration of **FastAPI**, **Pytest**, **Playwright**, and **Docker** with **automated CI/CD**.
