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
The application consists of three main files:

1) metricstics.py: Contains the Metricstics class with methods for statistical calculations.
2) exceptions.py: Contains custom exception classes for the application.
3) metricstics_app.py: Manages the Tkinter GUI and user interactions.
4) login.py: Handles the user authentication process.
5)session_manager.py: Manages user sessions, including saving and loading sessions.

## The application also includes a login functionality with predefined credentials 
## (username: admin, password: password)

There are also two example dataset files:
1) valid_dataset.txt: A text file with valid numeric data.
2) invalid_dataset.txt: A text file with some non-numeric data to demonstrate error handling.

## Running the Application
1. Clone the repository or download the .py files and the dataset examples.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the downloaded files.
4. Run the application with:

```bash
python metricstics_app.py
```
The GUI should open, where you can login and perform calulation.

## Usage
1. Login: Start by logging in using the username admin and the password password.

2. Starting a New Session:
* Click the "Start New Session" button to initiate a new session for statistical analysis.
  
3. Loading a Previous Session:
* To load a previous session, select it from the dropdown menu under "Load Previous Session" and click the "Load Session" button. This will display the dataset and statistics from the selected session.

4. Uploading a Dataset:
* Use the "Upload Dataset" button to load a dataset from a text file for a new session. This is suitable for performing analysis on custom data.

5. Generating a Random Dataset:
* Click the "Generate Random Dataset" button to create a dataset with 1000 random numbers between 0 and 1000. This feature is useful for quick testing or when specific data is not required.

6. Calculating Statistics:
* After uploading or generating a dataset, click "Calculate Statistics" to compute the mean, median, mode, minimum, and maximum values.
* If there are more than 10 mode values, a "Show Mode" button will appear to display all mode values in a separate window.

7. Saving Statistical Results:
* Use the "Save As" button to save the calculated statistical results to a file. This feature allows you to keep a record of the results for future reference.

8. Saving the Dataset:
* The "Save Dataset" button enables you to save the currently loaded or generated dataset. This is particularly useful for preserving data used in a session for later use or analysis.

9. Exiting the Application:
* Click the "Quit" button to close the application safely.

## Error Handling
The application includes error handling for:
1. Incorrect file types or file content when uploading a dataset.
2. Errors during statistical calculations if the dataset is inappropriate (e.g., non-numeric values, empty dataset).
3. Login errors.
4. Session management issues.
