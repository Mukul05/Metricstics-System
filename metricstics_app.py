# Metricstics_app.py
import tkinter as tk
from tkinter import messagebox, filedialog
import random

from metricstics import Metricstics
from exceptions import DataFileError, CalculationError, LoginError, SessionError
from login import Login
from session_manager import SessionManager




def changeOnHover(button: object, colorOnHover: object, colorOnLeave: object) -> object:
    # adjusting background of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))

    # background color on leaving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))

# Login window
class LoginWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Login')
        # width*height
        self.geometry('250x200')
        self.configure(background='lightgray')
        tk.Label(self, text='Username:',background='lightgray').pack(pady=5)
        self.username_entry = tk.Entry(self,highlightthickness=2,highlightbackground='black')
        self.username_entry.pack()

        tk.Label(self, text='Password:',background='lightgray').pack(pady=5)
        self.password_entry = tk.Entry(self, show='*',highlightthickness=2,highlightbackground='black')
        self.password_entry.pack()

        login_button = tk.Button(self, text='Login', command=self.attempt_login, fg='black', bg='light blue')
        login_button.pack(pady=15)

        # Apply hover effect to the login button
        changeOnHover(login_button, 'green', 'yellow')

    def attempt_login(self):
        # Your login logic here
        pass

    def on_close(self):
        self.destroy()
        self.master.destroy()

    def attempt_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        try:
            if Login.verify_login(username, password):
                self.destroy()
                self.master.deiconify()
                self.master.configure(background='lightgray')
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

        self.start_session_button = tk.Button(self, text='Start New Session', command=self.start_new_session,fg='black',bg='light blue')
        self.start_session_button.pack(pady=10)
        changeOnHover(self.start_session_button,'green','yellow')

        self.load_session_label = tk.Label(self, text='Load Previous Session:')
        self.load_session_label.pack(pady=5)

        self.sessions_var = tk.StringVar(self)
        self.update_session_dropdown()

        # Apply hover effect to the login button

        self.load_session_button = tk.Button(self, text='Load Session', command=self.load_session,fg='black', bg='light blue',)
        self.load_session_button.pack(pady=10)
        changeOnHover(self.load_session_button, 'green', 'yellow')

        self.upload_button = tk.Button(self, text='Upload Dataset', command=self.upload_dataset,fg='black', bg='light blue')
        self.upload_button.pack(pady=10)
        changeOnHover(self.upload_button, 'green', 'yellow')

        self.random_button = tk.Button(self, text='Generate Random Dataset', command=self.generate_random_dataset,fg='black', bg='light blue')
        self.random_button.pack(pady=10)
        changeOnHover(self.random_button, 'green', 'yellow')

        self.calculate_button = tk.Button(self, text='Calculate Statistics', command=self.calculate_statistics,fg='black', bg='light blue')
        self.calculate_button.pack(pady=10)
        changeOnHover(self.calculate_button, 'green', 'yellow')



        self.results_label = tk.Label(self, text='Results will appear here', height=10,highlightthickness=2,highlightbackground='black')
        self.results_label.pack(pady=10)

        self.dataset_source_label = tk.Label(self, text='No dataset loaded')
        self.dataset_source_label.pack(pady=10)

        self.show_mode_button = tk.Button(self, text='Show Mode',fg='black',bg='light blue')
        changeOnHover(self.show_mode_button, 'green', 'yellow')


        self.complete_results = ""

        self.save_as_button = tk.Button(self, text="Save Result", command=self.save_results,fg='black',bg='light blue')
        self.save_as_button.pack(pady=10)
        changeOnHover(self.save_as_button, 'green', 'yellow')
        self.save_dataset_button = tk.Button(self, text="Save Used Dataset", command=self.save_dataset,fg='black',bg='light blue')
        self.save_dataset_button.pack(pady=10)
        changeOnHover(self.save_dataset_button, 'green', 'yellow')
        self.quit_button = tk.Button(self, text="Quit", command=self.close_application,fg='black',bg='light blue')
        self.quit_button.pack(pady=10)
        changeOnHover(self.quit_button, 'red', 'yellow')
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
        self.complete_results = ""  # Reset the complete results string

        result_text = ''
        for stat, value in statistics.items():
            if stat == 'mode':
                mode_values = value if isinstance(value, list) else [value]
                self.complete_results += f"Mode: {', '.join(map(str, mode_values))}\n"

                if len(mode_values) > 10:
                    # Configure the button with the current mode values and show it
                    self.show_mode_button.configure(command=lambda mv=mode_values: self.show_mode(mv))
                    self.show_mode_button.pack(before=self.save_as_button)  # Position the button
                    result_text += 'Mode: [Click to view]\n'
                else:
                    # Mode values fit in the label, so just display them and hide the button
                    result_text += f"Mode: {', '.join(map(str, mode_values))}\n"
                    self.show_mode_button.pack_forget()  # Hide the button
            else:
                result_text += f"{stat.capitalize()}: {value}\n"
                self.complete_results += f"{stat.capitalize()}: {value}\n"

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

    def save_results(self):
        if not self.complete_results:
            messagebox.showinfo("Info", "No results to save.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if not file_path:
            return  # User cancelled; exit the method

        with open(file_path, 'w') as file:
            file.write(self.complete_results)

        messagebox.showinfo("Info", f"Results saved to {file_path}")

    def save_dataset(self):
        if self.stats is None or not self.stats.data:
            messagebox.showinfo("Info", "No dataset to save.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if not file_path:
            return  # User cancelled; exit the method

        with open(file_path, 'w') as file:
            for data_point in self.stats.data:
                file.write(f"{data_point}\n")

        messagebox.showinfo("Info", f"Dataset saved to {file_path}")


# Run the application
if __name__ == "__main__":
    app = MetricsticsApp()
    app.withdraw()


    login_window = LoginWindow(app)

    app.mainloop()
