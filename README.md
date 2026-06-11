Python Desktop Calculator & Pytest Automation Suite

📌 Project Overview
This repository contains a robust Desktop Calculator application built in Python, featuring a fully functional Command Line Interface (CLI). More importantly, it demonstrates core software engineering practices by strictly separating business logic from the user interface and implementing comprehensive Unit Testing using the Pytest framework. 

This project serves as a practical demonstration of White-Box testing methodologies, input validation, and state management within a Python application.

 🚀 Key Technical Features
	•	Separation of Concerns: Independent classes for core arithmetic logic (`Calculator`) and CLI routing (`CalculatorApp`). 
	•	Defensive Programming: Strict input validation enforcing strictly numeric data types (`int`, `float`) before execution. 
	•	Advanced Error Handling: Graceful exception catching for edge cases (e.g., Division by Zero, Square Root of Negative Numbers) preventing application crashes. 
	•	State Management: Built-in timestamped history tracking for all mathematical operations performed during a session. 
	•	Automated Unit Testing: Full test suite covering positive paths, edge cases, and explicit exception assertions using `pytest.raises`.

 🛠️ Technology Stack
	•	Language: Python 3 
	•	Testing Framework: Pytest  
	•	Architecture: Object-Oriented Programming (OOP)

📂 Repository Structure
desktop-calculator/ 
├── main.py # Application entry point
├── calculator.py # Core calculation logic and application interface 
├── test_operations.py # Automated unit test suite using Pytest
├── requirements.txt # Python dependencies list 
└── README.md # Project documentation

⚙️ Installation & Setup

1. Clone the repository:
```bash
   git clone https://github.com/vladzpop11/desktop-calculator-pytest.git
   cd your-repo-name

2. Create virtual environment
```bash
    python3 -m venv venv 
    source venv/bin/activate # On Windows use: venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt


🧪 Running the Tests
To launch the interactive calculator CLI: python main.py

To run the automated Pytest suite: pytest tests/test_operations.py -v
