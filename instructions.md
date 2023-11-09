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
2) metricstics_exceptions.py: Contains custom exception classes for the application.
3) metricstics_app.py: Manages the Tkinter GUI and user interactions.

There are also two example dataset files:
1) valid_dataset.txt: A text file with valid numeric data.
2) invalid_dataset.txt: A text file with some non-numeric data to demonstrate error handling.

## Running the Application
1) Clone the repository or download the .py files and the dataset examples.
2) Open a terminal or command prompt.
3) Navigate to the directory containing the downloaded files.
4) Run the application with:

```bash
python metricstics_app.py
```
The GUI should open, where you can upload a dataset or generate a random dataset for analysis.4

## Usage
1) Use the "Upload Dataset" button to load a dataset from a text file.
2) Use the "Generate Random Dataset" button to create a dataset with 1000 random numbers between 0 and 1000.
3) Calculate the mean, median, mode, min, and max using the corresponding buttons.

##Error Handling
The application includes error handling for:

1) Incorrect file types or file content when uploading a dataset.
2) Errors during statistical calculations if the dataset is inappropriate (e.g., non-numeric values, empty dataset).
If errors occur, informative messages will be displayed to the user.

