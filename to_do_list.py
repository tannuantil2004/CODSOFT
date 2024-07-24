import tkinter as tk
from tkinter import messagebox

tasks = []

def load_tasks():
    try:
        with open('tasks.txt', 'r') as file:
            for task in file:
                tasks.append(task.strip())
                tasks_listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

def save_tasks():
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()

def update_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        new_task = task_entry.get()
        if new_task:
            tasks[selected_task_index[0]] = new_task
            tasks_listbox.delete(selected_task_index)
            tasks_listbox.insert(selected_task_index, new_task)
            task_entry.delete(0, tk.END)
            save_tasks()

def delete_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        tasks_listbox.delete(selected_task_index)
        save_tasks()

def mark_task_completed():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        task = tasks[selected_task_index[0]]
        tasks[selected_task_index[0]] = task + " (Completed)"
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(selected_task_index, task + " (Completed)")
        save_tasks()

# Create the main window
schedule_list = tk.Tk()
schedule_list.title("To-Do List")
schedule_list.geometry("500x550")
schedule_list.configure(bg="#E6E6FA")  # Set peach background color for the window

# Task entry widget
name = tk.Label(schedule_list,text = "Write the task to be done and then add task")
name.pack(pady=2)
task_entry = tk.Entry(schedule_list, width=50)
task_entry.pack(pady=10)

# Button styles
button_style_add = {
    "bg": "#FFB6C1",       # Green background color
    "fg": "#ffffff",       # White text color
    "font": ("Helvetica", 10, "bold"),  # Font style
    "relief": "raised",
    "bd": 3,
}

button_style_update = {
    "bg": "#FF34B3",       # Blue background color
    "fg": "#ffffff",       # White text color
    "font": ("Helvetica", 10, "bold"),  # Font style
    "relief": "raised",
    "bd": 3,
}

button_style_delete = {
    "bg": "#8EE5EE",       # Red background color
    "fg": "#ffffff",       # White text color
    "font": ("Helvetica", 10, "bold"),  # Font style
    "relief": "raised",
    "bd": 3,
}

button_style_complete = {
    "bg": "#00FA9A",       # Orange background color
    "fg": "#ffffff",       # White text color
    "font": ("Helvetica", 10, "bold"),  # Font style
    "relief": "raised",
    "bd": 3,
}

# Add task button
add_button = tk.Button(schedule_list, text="Add Task", command=add_task, **button_style_add)
add_button.pack(pady=5)

# Listbox to display tasks
name2 = tk.Label(schedule_list,text = "Schedule List")
name2.pack(pady=7)
tasks_listbox = tk.Listbox(schedule_list, width=50, height=10, bg="#ffffff", fg="#000000")
tasks_listbox.pack(pady=10)

# Update task button
name3 = tk.Label(schedule_list,text = "Select the task press update to make changes in schule list")
name3.pack(pady=2)
update_button = tk.Button(schedule_list, text="Update Task", command=update_task, **button_style_update)
update_button.pack(pady=5)

# Delete task button
name4 = tk.Label(schedule_list,text = "Select the task press delete")
name4.pack(pady=2)
delete_button = tk.Button(schedule_list, text="Delete Task", command=delete_task, **button_style_delete)
delete_button.pack(pady=5)

# Mark task as completed button
name5 = tk.Label(schedule_list,text = "Select the task press Mark as complete")
name5.pack(pady=2)
complete_button = tk.Button(schedule_list, text="Mark as Completed", command=mark_task_completed, **button_style_complete)
complete_button.pack(pady=5)

# Load tasks from file
load_tasks()

# Start the Tkinter event loop
schedule_list.mainloop()
