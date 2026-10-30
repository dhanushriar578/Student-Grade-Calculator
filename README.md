# Student Grade Calculator 🎓

A beginner-friendly Python project that calculates a student's total marks, percentage, grade, and pass/fail status using Streamlit.

## Features

- Enter a student's name.
- Enter marks for five subjects.
- Calculate total marks out of 500.
- Calculate percentage.
- Automatically assign a grade.
- Check pass/fail status for each subject.
- Display the final result in a simple web interface.

## Technologies Used

- Python
- Streamlit

## Project Structure

```text
student-grade-calculator/
├── app.py
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Install Python

Install Python 3.9 or later from https://www.python.org/downloads/.

### 2. Download or clone this repository

```bash
git clone https://github.com/YOUR-USERNAME/Student-Grade-Calculator.git
cd Student-Grade-Calculator
```

### 3. Install the required library

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your web browser.

## Grade Criteria

| Percentage | Grade |
|---|---|
| 90–100% | A+ |
| 80–89% | A |
| 70–79% | B |
| 60–69% | C |
| 50–59% | D |
| Below 50% | E |
| Any subject below 35 | F (Fail) |

A student must score at least 35 marks in every subject to pass.

## Example

For marks 90, 85, 78, 88, and 79:

- Total: 420 / 500
- Percentage: 84%
- Grade: A
- Result: PASS

## Future Improvements

- Add more subjects.
- Save student results to a database.
- Generate downloadable result reports.
- Add student login functionality.

## Author

Add your name here.
