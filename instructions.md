# Metricstics Application

The Metricstics application is a Python-based GUI tool that computes basic statistical metrics, such as mean, median, mode, minimum, and maximum values from a given dataset.

## Prerequisites

To run the Metricstics application, you will need:

- Python 3.x
- Tkinter (usually included with Python)

## Installation

Python can be downloaded from the official website:


https://www.python.org/downloads/ 

If Tkinter is not installed, it can be installed via pip:

```bash
pip install tk
```

## Application Structure
The application consists of 5 main files:

1) metricstics.py: Contains the Metricstics class with methods for statistical calculations.
2) exceptions.py: Contains custom exception classes for the application.
3) metricstics_app.py: Manages the Tkinter GUI and user interactions.
4) login.py: Handles the user authentication process.
5) session_manager.py: Manages user sessions, including saving and loading sessions.

## The application also includes a login functionality with predefined credentials 
## (username: admin, password: password)

There are also two example dataset files:
1) valid_dataset.txt: A text file with valid numeric data.
2) invalid_dataset.txt: A text file with some non-numeric data to demonstrate error handling.
3) valid_dataset_more than 10 modes: a text file with more than 10 modes
   
## Running the Application
1. Clone the repository or download the .py files and the dataset examples.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the downloaded files.
4. Run the application with:

```bash
python metricstics_app.py
```
The GUI should open, where you can log in and perform calculations.

## Usage
1. Login using the username admin and password password.
2. To start a new session, use the "Start New Session" button.
3. To load a previous session, select a session from the dropdown menu under "Load Previous Session" and click the "Load Session" button. This will display the dataset and statistics from the selected session.
4. Use the "Upload Dataset" button to load a dataset from a text file for a new session.
5. Use the "Generate Random Dataset" button to create a dataset with 1000 random numbers between 0 and 1000 for a new session.
6. Calculate statistics by clicking "Calculate Statistics". If there are more than 10 median values, a "Show Median" button will appear to view all median values.
7. Save the dataset and result to the desired location

## Error Handling
The application includes error handling for:
1. Incorrect file types or file content when uploading a dataset.
2. Errors during statistical calculations if the dataset is inappropriate (e.g., non-numeric values, empty dataset).
3. Login errors.
4. Session management issues.
