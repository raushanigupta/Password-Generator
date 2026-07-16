import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_var.get())
    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digits_var.get()
    use_special = special_var.get()
    if not (use_upper or use_lower or use_digits or use_special):
        messagebox.showwarning("Selection Error", "Please select at least one character type.")
        return
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    if length < 8:
        strength = "Weak"
    elif length < 12:
        strength = "Moderate"
    else:
        strength = "Strong"
    strength_label.config(text=f"Strength: {strength}")

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Copy Error", "No password to copy.")

root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x350")
root.resizable(False, False)

length_var = tk.StringVar(value="12")
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=False)

tk.Label(root, text="Password Length:").pack(anchor="w", padx=10, pady=(10,0))
length_spinbox = tk.Spinbox(root, from_=4, to=64, textvariable=length_var, width=5)
length_spinbox.pack(anchor="w", padx=10)

tk.Label(root, text="Include:").pack(anchor="w", padx=10, pady=(10,0))
tk.Checkbutton(root, text="Uppercase Letters", variable=upper_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Lowercase Letters", variable=lower_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Digits", variable=digits_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Special Characters", variable=special_var).pack(anchor="w", padx=20)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_entry = tk.Entry(root, width=40, font=("Courier", 12))
password_entry.pack(pady=5)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=5)

strength_label = tk.Label(root, text="Strength: ", font=("Arial", 10, "italic"))
strength_label.pack(pady=5)

root.mainloop()