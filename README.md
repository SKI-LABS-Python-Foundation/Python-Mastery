# Python-Mastery
Practical Python programming and automation course focused on problem solving, real-world projects, APIs, and automation.

# Python Programming & Automation

**SKIhub Labs × Felcode Academy**

A practical 4-week Python course focused on **programming fundamentals, problem solving, automation, data processing, file handling, APIs, and building real-world software solutions**.

---

## Course Overview

This course is designed to move students beyond simply learning Python syntax.

The focus is on learning how to:

* Understand real-world problems
* Break problems into smaller parts
* Design solutions before coding
* Write clean Python programs
* Work with files and data
* Automate repetitive tasks
* Consume APIs
* Handle errors
* Debug applications
* Organize Python projects
* Use Git and GitHub
* Build and demonstrate a complete practical application

The course follows a **learn → solve → build → test → improve** approach.

---

# Course Details

**Duration:** 4 Weeks

**Mode:** Online

**Approach:** Practical / Project-Based

**Language:** Python 3

**Operating Environment:** Linux / Windows / macOS

**Version Control:** Git / GitHub

**Editor:** VS Code, Neovim, Nano, PyCharm or another suitable editor

---

# Prerequisites

Students should have:

* A computer
* Python 3 installed
* Internet access
* A GitHub account
* Basic computer literacy
* Willingness to practice
* No prior advanced programming experience required

---

# Learning Outcomes

By the end of the course, students should be able to:

1. Understand Python programming fundamentals.
2. Write and execute Python programs.
3. Work with variables and data types.
4. Accept and validate user input.
5. Use operators and expressions.
6. Implement conditional logic.
7. Implement loops.
8. Work with lists, tuples, sets and dictionaries.
9. Manipulate strings.
10. Write reusable functions.
11. Handle errors and exceptions.
12. Read and write files.
13. Work with JSON and structured data.
14. Use Python modules and packages.
15. Create virtual environments.
16. Automate repetitive tasks.
17. Work with APIs.
18. Process and transform data.
19. Apply Object-Oriented Programming concepts.
20. Debug and test Python applications.
21. Use Git and GitHub professionally.
22. Build a complete practical Python application.

---

# Course Philosophy

The course is not based on memorizing Python syntax.

Every concept should answer a practical question:

> **What problem does this help me solve?**

Students will be expected to write programs, modify existing programs, debug broken programs and explain their solutions.

---

# Four-Week Roadmap

```text
WEEK 1
Python Fundamentals
        ↓
WEEK 2
Problem Solving & Data
        ↓
WEEK 3
Files, Functions, OOP & APIs
        ↓
WEEK 4
Automation & Final Application
```

---

# MAIN PRACTICAL PROJECT

# Business Operations Automation System

Throughout the four weeks, students will progressively build a Python application that helps a small organization manage and automate routine business operations.

The final system will demonstrate practical Python skills rather than isolated classroom exercises.

The application will eventually support:

* Customer records
* Product/service records
* Transactions
* Data validation
* Searching
* Reporting
* File storage
* JSON data
* Automated reports
* API integration
* Basic data processing
* Error handling
* Logging
* Command-line interaction

The project begins as a simple Python program and evolves into a structured automation application.

---

# WEEK 1 — PYTHON FUNDAMENTALS

## Theme

**Learn to think in Python.**

The first week establishes the programming foundation required for solving problems.

---

## Topics

### 1. Introduction to Programming

* What programming is
* What Python is
* Interpreted languages
* Source code
* Python interpreter
* Syntax
* Logic
* Errors
* Problem solving

---

# 2. Python Environment

Students learn how to:

* Check Python installation
* Run Python from the terminal
* Create `.py` files
* Execute scripts
* Use the Python interactive shell

Example:

```bash
python3 --version
```

Run a program:

```bash
python3 main.py
```

---

# 3. Variables and Data Types

Students learn:

```python
name = "Denis"
age = 27
average = 90.5
is_active = True
```

Core types:

* `str`
* `int`
* `float`
* `bool`

---

# 4. Input and Output

Students learn:

```python
print()
input()
```

Practical applications:

* Customer information
* Product information
* Employee information
* User registration
* Transaction input

---

# 5. Operators

### Arithmetic

```text
+
-
*
/
%
**
//
```

### Comparison

```text
>
<
>=
<=
==
!=
```

### Logical

```text
and
or
not
```

---

# WEEK 1 PROBLEM-SOLVING TASKS

Students solve practical problems such as:

### Problem 1

Calculate the total and average of three marks.

### Problem 2

Determine whether a number is even or odd.

### Problem 3

Calculate a product's final price after discount.

### Problem 4

Calculate an employee's salary after deductions.

### Problem 5

Determine whether a customer qualifies for a discount.

### Problem 6

Calculate electricity or utility costs based on usage.

### Problem 7

Calculate profit from buying and selling a product.

---

# WEEK 1 MINI PROJECT

## Sales Calculator

Build a program that accepts:

* Product name
* Quantity
* Unit price
* Discount percentage

The program calculates:

* Subtotal
* Discount
* Final amount
* Profit estimate

Example:

```text
================================
       SALES CALCULATOR
================================

Product: Laptop
Quantity: 2
Unit Price: 75000
Discount: 5%

Subtotal: KSh 150000
Discount: KSh 7500
Final Amount: KSh 142500
```

---

# WEEK 1 MILESTONE

Students must have:

* Python environment working
* Git repository created
* At least 10 solved problems
* Sales Calculator completed
* Project README started
* At least 3 meaningful Git commits

Example:

```bash
git add .
git commit -m "Add sales calculator"
git push
```

---

# WEEK 2 — CONTROL FLOW, COLLECTIONS & PROBLEM SOLVING

## Theme

**Turn business rules into working programs.**

---

# Topics

## 1. Conditional Statements

```python
if
elif
else
```

Applications:

* Discounts
* Customer categories
* Payment status
* Stock status
* Eligibility systems

---

# 2. Loops

### `for`

For controlled iteration.

### `while`

For condition-based repetition.

### `break`

Stop a loop.

### `continue`

Skip an iteration.

---

# 3. Lists

```python
products = ["Laptop", "Phone", "Monitor"]
```

Students learn:

* Adding items
* Removing items
* Updating items
* Searching
* Iterating

---

# 4. Tuples

```python
coordinates = (0, 0)
```

Understanding immutable collections.

---

# 5. Sets

Used for unique values.

```python
categories = {"Electronics", "Furniture", "Software"}
```

---

# 6. Dictionaries

Used to represent structured records.

```python
customer = {
    "id": 1001,
    "name": "Denis",
    "phone": "0700000000"
}
```

---

# 7. Strings

Students practice:

* Searching
* Splitting
* Joining
* Formatting
* Validation
* Cleaning input

---

# WEEK 2 PROBLEM-SOLVING TASKS

Students solve problems involving:

* Customer registration
* Product searching
* Stock calculation
* Shopping carts
* Employee records
* Expense tracking
* Sales calculations
* Menu systems
* Input validation

---

# WEEK 2 PROJECT

## Business Operations System — Version 1

Students upgrade the Week 1 project.

The application should provide:

```text
========================================
       BUSINESS OPERATIONS SYSTEM
========================================

1. Add Customer
2. View Customers
3. Add Product
4. View Products
5. Record Sale
6. Search
7. Exit
```

Students should use:

* Lists
* Dictionaries
* Loops
* Conditions
* Functions where appropriate
* Input validation

---

# WEEK 2 MILESTONE

By the end of Week 2:

* Application supports multiple customers
* Application supports multiple products
* Sales can be recorded
* Search functionality works
* Menu system works
* Invalid input is handled
* At least 20 programming problems solved
* Git history shows progressive development

---

# WEEK 3 — FUNCTIONS, FILES, OOP & APIs

## Theme

**Move from scripts to structured applications.**

---

# 1. Functions

Students learn:

* Defining functions
* Parameters
* Arguments
* Return values
* Default parameters
* Scope
* Reusable code

Example:

```python
def calculate_total(quantity, price):
    return quantity * price
```

---

# 2. Modules

Students learn how to divide code into multiple files.

Example:

```text
app/
├── main.py
├── customers.py
├── products.py
├── sales.py
└── utils.py
```

---

# 3. File Handling

Students learn:

```python
open()
```

and file modes:

```text
r
w
a
```

Practical applications:

* Saving customers
* Saving products
* Saving sales
* Reading records

---

# 4. JSON

Students learn to work with structured data.

Example:

```json
{
    "id": 1001,
    "name": "Denis",
    "product": "Laptop",
    "amount": 75000
}
```

Python:

```python
import json
```

---

# 5. Exception Handling

Students learn:

```python
try
except
else
finally
```

The application must not crash because of normal user mistakes.

---

# 6. Object-Oriented Programming

Introduction to:

* Classes
* Objects
* Attributes
* Methods
* Constructors
* Encapsulation

Example:

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
```

---

# 7. APIs

Introduction to:

* What an API is
* HTTP requests
* GET requests
* JSON responses
* API authentication concepts
* Error handling

Students can use Python libraries such as:

```python
requests
```

---

# WEEK 3 PROJECT

## Business Operations System — Version 2

Refactor the application into a proper Python project.

Recommended structure:

```text
business-automation/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── customers.py
│   ├── products.py
│   ├── sales.py
│   ├── reports.py
│   └── utils.py
│
├── data/
│
├── tests/
│
├── requirements.txt
├── README.md
└── .gitignore
```

The system should now:

* Use functions
* Use modules
* Use classes where appropriate
* Save data
* Load data
* Handle errors
* Validate input
* Produce basic reports

---

# WEEK 3 API PRACTICAL

Students build a small Python program that consumes a public API.

The program should:

1. Send a request.
2. Receive JSON data.
3. Extract relevant information.
4. Display the result.
5. Handle connection/API errors.

This introduces students to the same basic concept they will later use when building backend applications.

---

# WEEK 3 MILESTONE

Students must demonstrate:

* Functions
* Modules
* File handling
* JSON
* Exception handling
* Classes
* API requests
* Project organization

---

# WEEK 4 — AUTOMATION & FINAL APPLICATION

## Theme

**Use Python to automate real work.**

This week moves from programming exercises into practical automation.

---

# 1. Automation Concepts

Students identify repetitive tasks that can be automated.

Examples:

* File organization
* Report generation
* Data cleaning
* File renaming
* CSV processing
* Email/report preparation
* Log processing
* Data conversion

---

# 2. Working With Files and Directories

Students learn practical automation using Python.

Useful modules:

```python
os
pathlib
shutil
```

Example tasks:

* Find files
* Create directories
* Move files
* Rename files
* Organize files by extension
* Detect duplicate filenames

---

# 3. CSV Data Processing

Students learn:

```python
import csv
```

Applications:

* Sales data
* Customer lists
* Inventory
* Reports

---

# 4. Data Processing

Students learn how to:

* Read raw data
* Clean data
* Validate data
* Calculate totals
* Calculate averages
* Group information
* Generate summaries

---

# 5. Logging

Students learn basic application logging.

```python
import logging
```

The application should record important events such as:

```text
2026-09-20 INFO Customer added
2026-09-20 INFO Sale recorded
2026-09-20 ERROR Invalid product ID
```

---

# 6. Testing

Students learn basic testing concepts.

They should test:

* Valid input
* Invalid input
* Empty data
* Missing files
* Incorrect values
* Search failures
* Calculation errors

Introduction to:

```python
pytest
```

---

# FINAL PROJECT

# Business Operations Automation System

The final application should combine the skills learned throughout the course.

---

# Required Features

## 1. Customer Management

Allow users to:

* Add customers
* View customers
* Search customers
* Update customers
* Delete customers

---

## 2. Product Management

Allow users to:

* Add products
* View products
* Search products
* Update products
* Delete products
* Track stock

---

## 3. Sales Management

Allow users to:

* Record sales
* Calculate totals
* Update stock
* Store transactions

---

## 4. Reporting

Generate:

* Total sales
* Number of transactions
* Best-selling products
* Customer activity
* Stock summary

---

## 5. Data Persistence

Data must survive application restarts.

Use:

```text
JSON / CSV
```

---

## 6. Automation

Implement at least **two meaningful automation features**.

Examples:

### Automated sales report

Generate a report such as:

```text
========================================
          SALES REPORT
========================================

Total Sales: KSh 450,000
Transactions: 27

Top Product:
Laptop

Total Customers: 18

Low Stock:
USB Cable
Wireless Mouse
```

### Automated file organization

Automatically organize files into:

```text
reports/
data/
exports/
logs/
```

---

# 7. API Integration

The final application should include at least one practical API integration.

Students must demonstrate:

* Request
* Response
* JSON processing
* Error handling

The API should provide functionality that makes sense for the application rather than being added only to satisfy a requirement.

---

# 8. Logging

The application should maintain a log file:

```text
logs/app.log
```

---

# 9. Error Handling

The application should handle expected problems gracefully.

Example:

```text
Invalid customer ID.
Please try again.
```

Instead of:

```text
Traceback...
ValueError...
```

being shown to the user.

---

# FINAL PROJECT STRUCTURE

Recommended structure:

```text
business-operations-automation/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── customer.py
│   │   ├── product.py
│   │   └── sale.py
│   │
│   ├── services/
│   │   ├── customer_service.py
│   │   ├── product_service.py
│   │   ├── sales_service.py
│   │   └── report_service.py
│   │
│   ├── automation/
│   │   ├── file_organizer.py
│   │   └── report_generator.py
│   │
│   └── utils/
│       ├── validation.py
│       └── logging_config.py
│
├── data/
│   ├── customers.json
│   ├── products.json
│   └── sales.json
│
├── reports/
│
├── logs/
│
├── tests/
│   ├── test_customers.py
│   ├── test_products.py
│   └── test_sales.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# VIRTUAL ENVIRONMENT

Students should learn to isolate project dependencies.

Create:

```bash
python3 -m venv .venv
```

Activate on Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# GIT WORKFLOW

Students should use Git throughout the course.

Example:

```bash
git status
git add .
git commit -m "Add customer management"
git push
```

Recommended commits:

```text
Initialize Python project
Add sales calculator
Add customer management
Add product management
Add sales recording
Add search functionality
Add JSON persistence
Add exception handling
Add reporting
Add API integration
Add automation features
Add logging
Add tests
Update documentation
```

---

# PROBLEM-SOLVING WORKFLOW

Students should follow this process before writing code:

```text
UNDERSTAND
     ↓
IDENTIFY THE PROBLEM
     ↓
DEFINE INPUTS
     ↓
DEFINE OUTPUTS
     ↓
BREAK INTO STEPS
     ↓
WRITE PSEUDOCODE
     ↓
IMPLEMENT
     ↓
TEST
     ↓
DEBUG
     ↓
REFACTOR
     ↓
DOCUMENT
     ↓
COMMIT
```

---

# WEEKLY PRACTICAL MILESTONES

| Week       | Focus                        | Main Deliverable        |
| ---------- | ---------------------------- | ----------------------- |
| **Week 1** | Python Fundamentals          | Sales Calculator        |
| **Week 2** | Collections & Logic          | Business Operations v1  |
| **Week 3** | Functions, OOP, Files & APIs | Business Operations v2  |
| **Week 4** | Automation & Testing         | Final Automation System |

---

# WEEKLY EXPECTATIONS

Every week students should produce:

### 1. Exercises

Independent programming problems.

### 2. Practical Work

A working feature or application.

### 3. Git Commits

Evidence of continuous development.

### 4. Documentation

Short explanations of what was built.

### 5. Demonstration

Students should be able to run and explain their solution.

---

# ASSESSMENT

Assessment is primarily practical.

## Week 1 — 15%

Python fundamentals and problem solving.

## Week 2 — 20%

Control flow, collections and application logic.

## Week 3 — 25%

Functions, OOP, files, JSON and APIs.

## Week 4 — 40%

Final automation application, testing, documentation and demonstration.

---

# FINAL DEMONSTRATION

Each student should demonstrate:

1. The problem being solved
2. Intended users
3. Application features
4. Project structure
5. Important Python concepts
6. Automation features
7. API integration
8. Error handling
9. Testing
10. GitHub repository
11. Live application demonstration
12. Challenges encountered
13. How those challenges were solved
14. Possible future improvements

---

# FINAL PROJECT SUCCESS CRITERIA

A project is considered complete when the student can:

* Explain the problem
* Explain the solution
* Run the application
* Demonstrate core features
* Store and retrieve data
* Handle invalid input
* Generate useful reports
* Automate repetitive work
* Consume an API
* Explain their code
* Demonstrate tests
* Explain errors they encountered
* Show Git history
* Maintain clear documentation

---

# FUTURE EXTENSIONS

After the four-week course, students can extend the system with:

* PostgreSQL
* SQLite
* FastAPI
* Django
* React
* Authentication
* Role-based access control
* Background tasks
* Docker
* Cloud deployment
* CI/CD
* Advanced testing
* Web dashboards

These are **post-course extensions**, not requirements for the four-week project.

---

# REPOSITORY STRUCTURE

The main course repository should be organized as:

```text
python-programming-automation/
│
├── README.md
│
├── week-01/
│   ├── notes/
│   ├── exercises/
│   └── project/
│
├── week-02/
│   ├── notes/
│   ├── exercises/
│   └── project/
│
├── week-03/
│   ├── notes/
│   ├── exercises/
│   └── project/
│
├── week-04/
│   ├── notes/
│   ├── exercises/
│   └── project/
│
├── final-project/
│
├── resources/
│
└── .gitignore
```

---

# CODE QUALITY EXPECTATIONS

Students should practice:

* Meaningful variable names
* Small functions
* Clear project structure
* Avoiding unnecessary duplication
* Useful comments
* Input validation
* Error handling
* Consistent formatting
* Meaningful Git commits
* Documentation

---

# CORE PRINCIPLE

Do not ask:

> “What Python syntax should I learn?”

Ask:

> **“What problem am I trying to solve, and how can Python help me solve it?”**

The course is built around that mindset.

---

# THE FOUR-WEEK JOURNEY

```text
LEARN
  ↓
SOLVE
  ↓
BUILD
  ↓
AUTOMATE
  ↓
TEST
  ↓
EXPLAIN
  ↓
IMPROVE
```

By the end of the four weeks, students should have more than a collection of Python exercises.

They should have:

* Practical programming experience
* Problem-solving experience
* Automation experience
* API experience
* A complete Python project
* A GitHub portfolio project
* Experience debugging real problems
* A foundation for backend development and further Python specialization

---

**SKIhub Labs × Felcode Academy**

**Python Programming & Automation**

**4 Weeks | Practical | Problem-Solving | Project-Based**
