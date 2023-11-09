# This is the metricstics_app.py file
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import random
from metricstics import Metricstics
from metricstics_exceptions import DataFileError, CalculationError

class MetricsticsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Metricstics Application')
        self.geometry('350x400')

        self.stats = None

        # Add a button to upload a dataset
        self.upload_button = tk.Button(self, text='Upload Dataset', command=self.upload_dataset)
        self.upload_button.pack(pady=10)

        # Add a button to generate a random dataset
        self.random_button = tk.Button(self, text='Generate Random Dataset', command=self.generate_random_dataset)
        self.random_button.pack(pady=10)

        # Add buttons for each statistical method
        self.mean_button = tk.Button(self, text='Calculate Mean', command=lambda: self.calculate_statistic('mean'))
        self.mean_button.pack(pady=10)

        self.median_button = tk.Button(self, text='Calculate Median', command=lambda: self.calculate_statistic('median'))
        self.median_button.pack(pady=10)

        self.mode_button = tk.Button(self, text='Calculate Mode', command=lambda: self.calculate_statistic('mode'))
        self.mode_button.pack(pady=10)

        self.min_button = tk.Button(self, text='Calculate Min', command=lambda: self.calculate_statistic('min'))
        self.min_button.pack(pady=10)

        self.max_button = tk.Button(self, text='Calculate Max', command=lambda: self.calculate_statistic('max'))
        self.max_button.pack(pady=10)

        # Add a label to show the dataset source
        self.dataset_source_label = tk.Label(self, text='No dataset loaded')
        self.dataset_source_label.pack(pady=10)

    def upload_dataset(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    data = file.read()
                    data_list = [float(num) for num in data.replace('\n', ',').split(',') if num.strip()]
                    if not data_list:
                        raise DataFileError("The data file is empty or contains non-numeric values.")
                    self.stats = Metricstics(data_list)
                    self.dataset_source_label.config(text=f"Dataset uploaded: {len(data_list)} values")
            except ValueError:
                messagebox.showerror("Data File Error", "The data file must contain only numeric values.")
            except DataFileError as e:
                messagebox.showerror("Data File Error", e)
            except Exception as e:
                messagebox.showerror("Error", f"An unexpected error occurred: {e}")

    def generate_random_dataset(self):
        random_data = [random.uniform(0, 1000) for _ in range(1000)]
        self.stats = Metricstics(random_data)
        self.dataset_source_label.config(text="Random dataset generated: 1000 values")

    def calculate_statistic(self, statistic):
        if self.stats is None:
            messagebox.showinfo("Info", "Please load a dataset first.")
            return
        try:
            result = getattr(self.stats, statistic)()
            messagebox.showinfo("Result", f"The {statistic} is: {result}")
        except CalculationError as e:
            messagebox.showerror("Calculation Error", e)
        except ValueError as e:
            messagebox.showerror("Value Error", e)
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

# Create the GUI app
app = MetricsticsApp()

# Run the application
app.mainloop()
