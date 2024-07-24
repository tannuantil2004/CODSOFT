import random
import string
import tkinter as tk
from tkinter import ttk

def gen_password(length, complexity):
    if complexity == 1:
        characters = string.ascii_lowercase
    elif complexity == 2:
        characters = string.ascii_letters
    elif complexity == 3:
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def generate():
    try:
        length = int(length_var.get())
        complexity = complexity_var.get()
        password = gen_password(length, complexity)
        result.set(password)
    except ValueError:
        result.set("Invalid input!")

password = tk.Tk()
password.title("Password Generator")
password.configure(bg="#e0f7fa")

ttk.Label(password, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
length_var = tk.StringVar()
ttk.Entry(password, textvariable=length_var).grid(row=0, column=1, padx=10, pady=10)

ttk.Label(password, text="Complexity:").grid(row=1, column=0, padx=10, pady=10)
complexity_var = tk.IntVar()
complexity_options = [
    ("If you want pass in Lowercase", 1),
    ("If you want pass in Letters", 2),
    ("If you want pass in Letters & Digits", 3),
    ("If you want pass in Letters, Digits & Symbols", 4)
]
for text, value in complexity_options:
    ttk.Radiobutton(password, text=text, variable=complexity_var, value=value).grid(row=value, column=1, sticky=tk.W)

ttk.Button(password, text="Generate Password", command=generate).grid(row=5, column=0, columnspan=2, pady=10)

result = tk.StringVar()
ttk.Entry(password, textvariable=result).grid(row=6, column=0, columnspan=2, pady=10)

password.mainloop()
