import tkinter as tk
from tkinter import ttk, messagebox
import time

# Color Palette
BG_COLOR = "#2E3440"  # Dark background
FG_COLOR = "#D8DEE9"  # Light text color
BUTTON_COLOR = "#5E81AC"  # Blue buttons
BUTTON_HOVER_COLOR = "#81A1C1"  # Lighter blue for hover
ENTRY_COLOR = "#4C566A"  # Darker entry field
LISTBOX_COLOR = "#3B4252"  # Listbox background
LISTBOX_FG_COLOR = "#ECEFF4"  # Listbox text color

# Fonts
FONT = ("Helvetica", 12)
BUTTON_FONT = ("Helvetica", 10, "bold")

tasks = []

# Global Variables for GUI Elements
task_entry = None
task_list = None

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_entry.delete(0, tk.END)
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty")

def update_task_list():
    task_list.delete(0, tk.END)
    for task in tasks:
        task_list.insert(tk.END, task)

def remove_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task_list.delete(selected_task_index)
        tasks.pop(selected_task_index[0])

def on_enter(event):
    event.widget.config(bg=BUTTON_HOVER_COLOR)

def on_leave(event):
    event.widget.config(bg=BUTTON_COLOR)

def clear_frame():
    """Clear the current frame."""
    for widget in app.winfo_children():
        widget.destroy()

def start_gui():
    global task_entry, task_list, app
    app = tk.Tk()
    app.title("Enhanced To-Do List GUI")
    app.geometry("600x500")
    app.configure(bg=BG_COLOR)

    # Start Page (Welcome Screen)
    start_page()

    app.mainloop()

def start_page():
    """Create the Start Page."""
    clear_frame()

    header_label = tk.Label(app, text="Welcome to To-Do List!", font=("Helvetica", 18, "bold"), fg=FG_COLOR, bg=BG_COLOR, pady=20)
    header_label.pack(fill=tk.X)

    start_button = tk.Button(app, text="Start", font=BUTTON_FONT, bg=BUTTON_COLOR, fg=FG_COLOR, relief=tk.FLAT, command=login_page)
    start_button.pack(pady=20)
    start_button.bind("<Enter>", on_enter)
    start_button.bind("<Leave>", on_leave)

def login_page():
    """Create the Login Page."""
    clear_frame()

    header_label = tk.Label(app, text="Login", font=("Helvetica", 18, "bold"), fg=FG_COLOR, bg=BG_COLOR, pady=20)
    header_label.pack(fill=tk.X)

    username_label = tk.Label(app, text="Username:", font=FONT, fg=FG_COLOR, bg=BG_COLOR)
    username_label.pack(pady=5)
    username_entry = tk.Entry(app, font=FONT, bg=ENTRY_COLOR, fg=FG_COLOR, insertbackground=FG_COLOR)
    username_entry.pack(pady=5, padx=20)

    password_label = tk.Label(app, text="Password:", font=FONT, fg=FG_COLOR, bg=BG_COLOR)
    password_label.pack(pady=5)
    password_entry = tk.Entry(app, font=FONT, bg=ENTRY_COLOR, fg=FG_COLOR, insertbackground=FG_COLOR, show="*")
    password_entry.pack(pady=5, padx=20)

    login_button = tk.Button(app, text="Login", font=BUTTON_FONT, bg=BUTTON_COLOR, fg=FG_COLOR, relief=tk.FLAT, command=lambda: verify_login(username_entry, password_entry))
    login_button.pack(pady=20)
    login_button.bind("<Enter>", on_enter)
    login_button.bind("<Leave>", on_leave)

def verify_login(username_entry, password_entry):
    """Verify the username and password."""
    username = username_entry.get()
    password = password_entry.get()

    # Simple hardcoded authentication
    if username == "admin" and password == "password":
        main_page()
    else:
        messagebox.showerror("Login Failed", "Invalid credentials. Please try again.")

def main_page():
    """Create the Main Page after successful login."""
    clear_frame()

    header_label = tk.Label(app, text="Main Menu", font=("Helvetica", 18, "bold"), fg=FG_COLOR, bg=BG_COLOR, pady=20)
    header_label.pack(fill=tk.X)

    task_button = tk.Button(app, text="Task Management", font=BUTTON_FONT, bg=BUTTON_COLOR, fg=FG_COLOR, relief=tk.FLAT, command=task_page)
    task_button.pack(pady=10)
    task_button.bind("<Enter>", on_enter)
    task_button.bind("<Leave>", on_leave)

    calc_button = tk.Button(app, text="Calculator", font=BUTTON_FONT, bg=BUTTON_COLOR, fg=FG_COLOR, relief=tk.FLAT, command=calculator_page)
    calc_button.pack(pady=10)
    calc_button.bind("<Enter>", on_enter)
    calc_button.bind("<Leave>", on_leave)

    test_button = tk.Button(app, text="Test System", font=BUTTON_FONT, bg=BUTTON_COLOR, fg=FG_COLOR, relief=tk.FLAT, command=test_page)
    test_button.pack(pady=10)
    test_button.bind("<Enter>", on_enter)
    test_button.bind("<Leave>", on_leave)

    fun_button = tk.Button(app, text="Fun Animation", font=BUTTON_FONT, bg=BUTTON_COLOR, fg=FG_COLOR, relief=tk.FLAT, command=fun_page)
    fun_button.pack(pady=10)
    fun_button.bind("<Enter>", on_enter)
    fun_button.bind("<Leave>", on_leave)

    logout_button = tk.Button(app, text="Logout", font=BUTTON_FONT, bg=BUTTON_COLOR, fg=FG_COLOR, relief=tk.FLAT, command=start_page)
    logout_button.pack(pady=20)
    logout_button.bind("<Enter>", on_enter)
    logout_button.bind("<Leave>", on_leave)

def task_page():
    """Create the Task Management Page."""
    clear_frame()

    header_label = tk.Label(app, text="Task Management", font=("Helvetica", 18, "bold"), fg=FG_COLOR, bg=BG_COLOR, pady=20)
    header_label.pack(fill=tk.X)

    global task_entry, task_list
    task_entry = tk.Entry(app, width=40, font=FONT, bg=ENTRY_COLOR, fg=FG_COLOR, insertbackground=FG_COLOR, relief=tk.FLAT)
    task_entry.pack(pady=10, padx=20, ipady=5)

    add_button = tk.Button(app, text="Add Task", command=add_task, font=BUTTON_FONT, bg=BUTTON_COLOR, fg=FG_COLOR, relief=tk.FLAT)
    add_button.pack(pady=5)
    add_button.bind("<Enter>", on_enter)
    add_button.bind("<Leave>", on_leave)

    remove_button = tk.Button(app, text="Remove Task", command=remove_task, font=BUTTON_FONT, bg=BUTTON_COLOR, fg=FG_COLOR, relief=tk.FLAT)
    remove_button.pack(pady=5)
    remove_button.bind("<Enter>", on_enter)
    remove_button.bind("<Leave>", on_leave)

    task_list = tk.Listbox(app, width=40, height=10, font=FONT, bg=LISTBOX_COLOR, fg=LISTBOX_FG_COLOR, relief=tk.FLAT, selectbackground=BUTTON_COLOR, selectforeground=FG_COLOR)
    task_list.pack(pady=10, padx=20, ipady=5)

    back_button = tk.Button(app, text="Back", font=BUTTON_FONT, bg=BUTTON_COLOR, fg=FG_COLOR, relief=tk.FLAT, command=main_page)
    back_button.pack(pady=10)
    back_button.bind("<Enter>", on_enter)
    back_button.bind("<Leave>", on_leave)

def calculator_page():
    """Create the Calculator Page."""
    clear_frame()

    header_label = tk.Label(app, text="Calculator", font=("Helvetica", 18, "bold"), fg=FG_COLOR, bg=BG_COLOR, pady=20)
    header_label.pack(fill=tk.X)

    expression_entry = tk.Entry(app, font=FONT, bg=ENTRY_COLOR, fg=FG_COLOR, insertbackground=FG_COLOR)
    expression_entry.pack(pady=10, padx=20)

    calc_button = tk.Button(app, text="Calculate", font=BUTTON_FONT, bg=BUTTON_COLOR, fg=FG_COLOR, relief=tk.FLAT, command=lambda: calculate(expression_entry))
    calc_button.pack(pady=10)
    calc_button.bind("<Enter>", on_enter)
    calc_button.bind("<Leave>", on_leave)

    back_button = tk.Button(app, text="Back", font=BUTTON_FONT, bg=BUTTON_COLOR, fg=FG_COLOR, relief=tk.FLAT, command=main_page)
    back_button.pack(pady=10)
    back_button.bind("<Enter>", on_enter)
    back_button.bind("<Leave>", on_leave)

def calculate(entry):
    """Perform the calculation."""
    try:
        result = eval(entry.get())
        messagebox.showinfo("Result", f"Result: {result}")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

def test_page():
    """Create the Test Page."""
    clear_frame()

    header_label = tk.Label(app, text="Test System", font=("Helvetica", 18, "bold"), fg=FG_COLOR, bg=BG_COLOR, pady=20)
    header_label.pack(fill=tk.X)

    questions = [
        {"question": "What is 2 + 2?", "answer": "4"},
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "What is 5 * 6?", "answer": "30"}
    ]

    score = 0
    test_answers = {}

    for idx, q in enumerate(questions):
        question_label = tk.Label(app, text=q["question"], font=FONT, fg=FG_COLOR, bg=BG_COLOR)
        question_label.pack(pady=5)
        test_answers[idx] = tk.Entry(app, font=FONT, bg=ENTRY_COLOR, fg=FG_COLOR, insertbackground=FG_COLOR)
        test_answers[idx].pack(pady=5, padx=20)

    submit_button = tk.Button(app, text="Submit", font=BUTTON_FONT, bg=BUTTON_COLOR, fg=FG_COLOR, relief=tk.FLAT, command=lambda: submit_test(test_answers))
    submit_button.pack(pady=20)
    submit_button.bind("<Enter>", on_enter)
    submit_button.bind("<Leave>", on_leave)

    back_button = tk.Button(app, text="Back", font=BUTTON_FONT, bg=BUTTON_COLOR, fg=FG_COLOR, relief=tk.FLAT, command=main_page)
    back_button.pack(pady=10)
    back_button.bind("<Enter>", on_enter)
    back_button.bind("<Leave>", on_leave)

def submit_test(test_answers):
    """Submit the test and calculate the score."""
    correct_answers = [
        "4", "Paris", "30"
    ]
    score = 0
    for idx, answer in enumerate(correct_answers):
        user_answer = test_answers[idx].get().strip()
        if user_answer.lower() == answer.lower():
            score += 1

    messagebox.showinfo("Test Result", f"Your score: {score}/3")

def fun_page():
    """Display Fun Animation (Train)."""
    clear_frame()

    header_label = tk.Label(app, text="Fun Animation", font=("Helvetica", 18, "bold"), fg=FG_COLOR, bg=BG_COLOR, pady=20)
    header_label.pack(fill=tk.X)

    animate_train()

    back_button = tk.Button(app, text="Back", font=BUTTON_FONT, bg=BUTTON_COLOR, fg=FG_COLOR, relief=tk.FLAT, command=main_page)
    back_button.pack(pady=10)
    back_button.bind("<Enter>", on_enter)
    back_button.bind("<Leave>", on_leave)

def animate_train():
    """Simulate moving train in GUI."""
    train = ["🚂   ", "   🚂 ", "     🚂", "   🚂 ", "🚂   "]
    for frame in train:
        label = tk.Label(app, text=frame, font=("Helvetica", 36))
        label.pack()
        app.update()
        time.sleep(0.2)
        label.destroy()

# Start the application
if __name__ == "__main__":
    start_gui()
