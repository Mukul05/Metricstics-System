# Metricstics_app.py
import tkinter as tk
from tkinter import messagebox, filedialog
import random

from metricstics import Metricstics
from exceptions import DataFileError, CalculationError, LoginError, SessionError
from login import Login
from session_manager import SessionManager

# Login window
class LoginWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Login')
        self.geometry('250x150')

        tk.Label(self, text='Username:').pack(pady=5)
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        tk.Label(self, text='Password:').pack(pady=5)
        self.password_entry = tk.Entry(self, show='*')
        self.password_entry.pack()
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        tk.Button(self, text='Login', command=self.attempt_login).pack(pady=15)

    def attempt_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        try:
            if Login.verify_login(username, password):
                self.destroy()
                self.master.deiconify()
        except LoginError as e:
            messagebox.showerror("Login Failed", e)

    def on_close(self):

        self.destroy()
        self.master.destroy()

# Main application
class MetricsticsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Metricstics Application')
        self.geometry('720x820')

        self.session_manager = SessionManager()
        self.stats = None

        self.start_session_button = tk.Button(self, text='Start New Session', command=self.start_new_session)
        self.start_session_button.pack(pady=10)

        self.load_session_label = tk.Label(self, text='Load Previous Session:')
        self.load_session_label.pack(pady=5)

        self.sessions_var = tk.StringVar(self)
        self.update_session_dropdown()

        self.load_session_button = tk.Button(self, text='Load Session', command=self.load_session)
        self.load_session_button.pack(pady=10)

        self.upload_button = tk.Button(self, text='Upload Dataset', command=self.upload_dataset)
        self.upload_button.pack(pady=10)

        self.random_button = tk.Button(self, text='Generate Random Dataset', command=self.generate_random_dataset)
        self.random_button.pack(pady=10)

        self.calculate_button = tk.Button(self, text='Calculate Statistics', command=self.calculate_statistics)
        self.calculate_button.pack(pady=10)

        self.results_label = tk.Label(self, text='Results will appear here', height=10)
        self.results_label.pack(pady=10)

        self.dataset_source_label = tk.Label(self, text='No dataset loaded')
        self.dataset_source_label.pack(pady=10)
        self.show_mode_button = None

        self.quit_button = tk.Button(self, text="Quit", command=self.close_application)
        self.quit_button.pack(pady=10)
        self.protocol("WM_DELETE_WINDOW", self.close_application)
    def update_session_dropdown(self):
        if hasattr(self, 'sessions_dropdown'):
            self.sessions_dropdown.destroy()
        sessions_descriptions = self.get_session_descriptions()
        if not sessions_descriptions:
            sessions_descriptions.append('No previous sessions')
        self.sessions_dropdown = tk.OptionMenu(self, self.sessions_var, *sessions_descriptions)
        self.sessions_dropdown.pack(pady=5)
        if sessions_descriptions:
            self.sessions_var.set(sessions_descriptions[0])
        else:
            self.sessions_var.set('No previous sessions')

    def get_session_descriptions(self):
        sessions = self.session_manager.get_last_sessions()
        return ['Session from {}'.format(session['timestamp']) for session in sessions]

    def start_new_session(self):
        self.stats = None
        self.dataset_source_label.config(text='Started a new session. Please upload or generate a dataset.')
        self.results_label.config(text='')

    def load_session(self):
        selected_session_description = self.sessions_var.get()
        selected_session = next((session for session in self.session_manager.get_last_sessions() if
                                 selected_session_description.endswith(session['timestamp'])), None)
        if selected_session:
            self.stats = Metricstics(selected_session['dataset'])
            self.display_statistics(selected_session['statistics'])
            self.dataset_source_label.config(text='Loaded previous session.')

    def display_statistics(self, statistics):
        result_text = ''
        for stat, value in statistics.items():
            if stat == 'mode':
                mode_values = value if isinstance(value, list) else [value]

                if len(mode_values) > 10:
                    result_text += 'Mode: [Click to view]\n'
                    if self.show_mode_button is None:

                        self.show_mode_button = tk.Button(self, text='Show Mode')
                        self.show_mode_button.pack()

                    self.show_mode_button.configure(command=lambda mv=mode_values: self.show_mode(mv))
                else:
                    result_text += 'Mode: {}\n'.format(', '.join(map(str, mode_values)))
                    if self.show_mode_button:
                        self.show_mode_button.pack_forget()
            else:
                result_text += '{}: {}\n'.format(stat.capitalize(), value)

        self.results_label.config(text=result_text)

    def show_mode(self, mode_values):
        mode_window = tk.Toplevel(self)
        mode_window.title('Mode Values')
        mode_window.geometry('500x800')


        mode_text = tk.Text(mode_window, height=10, width=25)
        mode_text.pack(side=tk.LEFT, fill=tk.Y, expand=True)


        mode_scrollbar = tk.Scrollbar(mode_window, command=mode_text.yview)
        mode_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        mode_text.configure(yscrollcommand=mode_scrollbar.set)


        mode_text_values = '\n'.join(map(str, mode_values))
        mode_text.insert(tk.END, mode_text_values)

    def upload_dataset(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    data = file.read()

                    data_list = []
                    for num in data.replace('\n', ',').split(','):
                        if num.strip():
                            try:
                                data_list.append(float(num))
                            except ValueError:
                                raise DataFileError("Invalid dataset: contains non-numeric values.")
                    if not data_list:
                        raise DataFileError("The data file is empty or contains only invalid entries.")

                    self.stats = Metricstics(data_list)
                    self.dataset_source_label.config(text=f"Dataset uploaded: {len(data_list)} values")
            except (ValueError, DataFileError) as e:
                messagebox.showerror("Data File Error", e)
            except FileNotFoundError:
                messagebox.showerror("Error", "The specified file was not found.")
            except PermissionError:
                messagebox.showerror("Error", "Permission denied when accessing the file.")
            except Exception as e:
                messagebox.showerror("Error", f"An unexpected error occurred: {e}")


    def generate_random_dataset(self):
        random_data = [random.uniform(0, 1000) for _ in range(1000)]
        self.stats = Metricstics(random_data)
        self.dataset_source_label.config(text="Random dataset generated: 1000 values")
        self.results_label.config(text='')

    def calculate_statistics(self):
        if self.stats is None:
            messagebox.showinfo("Info", "Please load a dataset first.")
            return
        try:
            statistics = {
                'mean': self.stats.mean(),
                'median': self.stats.median(),
                'mode': self.stats.mode(),
                'min': self.stats.min(),
                'max': self.stats.max()
            }
            self.display_statistics(statistics)
            self.session_manager.create_new_session(self.stats.data, statistics)
            self.update_session_dropdown()
        except (CalculationError, ValueError) as e:
            messagebox.showerror("Calculation Error", e)
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

    def close_application(self):
        self.destroy()



# Run the application
if __name__ == "__main__":
    app = MetricsticsApp()
    app.withdraw()


    login_window = LoginWindow(app)

    app.mainloop()
