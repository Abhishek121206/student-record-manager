# Student Record Manager

A Python-based command-line application for managing student records using a CSV file for data storage.

The project demonstrates fundamental Python programming, file handling, data processing, input validation, automated testing, and Git/GitHub-based software development.

## Problem

Managing student records manually can become inefficient and error-prone when adding, updating, deleting, or analyzing student information.

This project provides a simple command-line system to manage student records and perform basic analysis of student marks.

## Dataset / Input

The application uses a CSV file named `students.csv` to store student records.

Each record contains:

| Field | Description                |
| ----- | -------------------------- |
| ID    | Unique student identifier  |
| Name  | Student's name             |
| Marks | Student's marks out of 100 |

Example:

```csv
ID,Name,Marks
1,Abhishek,89
2,Rahul,92
3,Priya,76
4,Arun,85
```

## Features

* Display all student records
* Add a new student
* Update an existing student
* Delete a student
* Calculate average marks
* Find the highest scorer
* Prevent duplicate student IDs
* Validate student names and IDs
* Validate marks between 0 and 100
* Handle invalid numerical input
* Store changes permanently in the CSV file
* Automated testing using `pytest`

## Approach

The application follows a simple CSV-based data management workflow:

```text
students.csv
     ↓
Read CSV using csv.DictReader
     ↓
Store records as Python dictionaries
     ↓
Perform requested operation
     ↓
Validate user input
     ↓
Update records in memory
     ↓
Save changes using csv.DictWriter
```

For analysis operations, the program processes the student records directly in Python.

For example:

* Average marks are calculated by summing all marks and dividing by the number of students.
* The highest scorer is identified by comparing the marks of each student.

## Technologies Used

* **Python 3**
* **CSV module** — reading and writing student records
* **pytest** — automated testing
* **Git** — version control
* **GitHub** — remote repository and project collaboration

## Project Structure

```text
student-record-manager/
│
├── main.py
├── test_main.py
├── students.csv
├── requirements.txt
├── README.md
└── .gitignore
```

### File Description

| File               | Purpose                 |
| ------------------ | ----------------------- |
| `main.py`          | Main application logic  |
| `test_main.py`     | Automated tests         |
| `students.csv`     | Student data storage    |
| `requirements.txt` | Python dependencies     |
| `.gitignore`       | Files excluded from Git |
| `README.md`        | Project documentation   |

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Abhishek121206/student-record-manager.git
```

### 2. Navigate to the project

```bash
cd student-record-manager
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the application with:

```bash
python main.py
```

The application displays a menu:

```text
====== Student Record Manager ======
1. Display students
2. Add student
3. Update student
4. Delete student
5. Calculate average
6. Find highest scorer
7. Exit
```

Select the required operation by entering its corresponding number.

### Example

```text
Enter choice of func to perform: 5

Average Marks: 85.5
```

## Testing

The project uses `pytest` for automated testing.

Run:

```bash
python -m pytest
```

Current tests verify:

* Average marks calculation
* Highest scorer identification

Expected result:

```text
2 passed
```

## Results

The application successfully provides basic CRUD operations for student records:

* **Create** — Add new students
* **Read** — Display student records
* **Update** — Modify student information
* **Delete** — Remove student records

It also provides basic analytical functionality through average-mark calculation and highest-scorer identification.

Input validation prevents invalid marks, empty fields, duplicate IDs, and non-numeric marks from being stored.

## Limitations

* Uses a CSV file instead of a database.
* Command-line interface only.
* Limited analytical functionality.
* No authentication or user roles.
* Student IDs are treated as strings rather than being automatically generated.
* Error handling for file-related issues can be improved.
* The application is designed for small datasets.

## Future Improvements

Possible future versions could include:

* Search students by ID or name
* Sort students by marks
* Filter students based on marks
* Grade calculation
* Student performance reports
* Better exception handling
* SQLite/MySQL database integration
* Graphical user interface
* REST API
* More comprehensive automated testing

## Version

**v1.0.0 — Initial Stable Release**

This release contains the core student record management functionality, input validation, CSV persistence, and automated tests.
