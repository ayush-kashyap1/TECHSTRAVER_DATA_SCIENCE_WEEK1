import random
import string
import tkinter as tk
from tkinter import messagebox


# Function to generate password
def generate_password(length, min_uppercase, min_digits, min_symbols, include_symbols):
    if length < min_uppercase + min_digits + min_symbols:
        raise ValueError("Length is too short for the specified minimum counts.")

    all_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    if include_symbols:
        all_characters += string.punctuation

    password = []

    password += random.choices(string.ascii_uppercase, k=min_uppercase)
    password += random.choices(string.digits, k=min_digits)
    if include_symbols:
        password += random.choices(string.punctuation, k=min_symbols)

    remaining_length = length - len(password)
    password += random.choices(all_characters, k=remaining_length)

    random.shuffle(password)

    return ''.join(password)


# CLI part
def run_cli():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                raise ValueError("Password length should be a positive number.")
            break
        except ValueError as e:
            print(e)

    min_uppercase = int(input("Enter the minimum number of uppercase letters: "))
    min_digits = int(input("Enter the minimum number of digits: "))
    min_symbols = int(input("Enter the minimum number of symbols: "))
    include_symbols = input("Include symbols (yes/no)? ").strip().lower() == 'yes'

    try:
        password = generate_password(length, min_uppercase, min_digits, min_symbols, include_symbols)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)


# GUI part
def run_gui():
    def generate():
        try:
            length = int(length_entry.get())
            min_uppercase = int(min_uppercase_entry.get())
            min_digits = int(min_digits_entry.get())
            min_symbols = int(min_symbols_entry.get())
            include_symbols = include_symbols_var.get()

            password = generate_password(length, min_uppercase, min_digits, min_symbols, include_symbols)
            result_label.config(text=f"Generated password: {password}", fg="green")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    root = tk.Tk()
    root.title("Password Generator")
    root.geometry("400x400")
    root.configure(bg="#F0F0F0")

    tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"), bg="#F0F0F0").pack(pady=10)

    frame = tk.Frame(root, bg="#F0F0F0")
    frame.pack(pady=10)

    tk.Label(frame, text="Password Length:", font=("Helvetica", 12), bg="#F0F0F0").grid(row=0, column=0, sticky="w",
                                                                                        pady=5)
    length_entry = tk.Entry(frame, font=("Helvetica", 12), width=10)
    length_entry.grid(row=0, column=1, pady=5)

    tk.Label(frame, text="Min Uppercase Letters:", font=("Helvetica", 12), bg="#F0F0F0").grid(row=1, column=0,
                                                                                              sticky="w", pady=5)
    min_uppercase_entry = tk.Entry(frame, font=("Helvetica", 12), width=10)
    min_uppercase_entry.grid(row=1, column=1, pady=5)

    tk.Label(frame, text="Min Digits:", font=("Helvetica", 12), bg="#F0F0F0").grid(row=2, column=0, sticky="w", pady=5)
    min_digits_entry = tk.Entry(frame, font=("Helvetica", 12), width=10)
    min_digits_entry.grid(row=2, column=1, pady=5)

    tk.Label(frame, text="Min Symbols:", font=("Helvetica", 12), bg="#F0F0F0").grid(row=3, column=0, sticky="w", pady=5)
    min_symbols_entry = tk.Entry(frame, font=("Helvetica", 12), width=10)
    min_symbols_entry.grid(row=3, column=1, pady=5)

    include_symbols_var = tk.BooleanVar()
    tk.Checkbutton(root, text="Include Symbols", variable=include_symbols_var, font=("Helvetica", 12),
                   bg="#F0F0F0").pack(pady=5)

    generate_button = tk.Button(root, text="Generate", command=generate, font=("Helvetica", 12), bg="#4CAF50",
                                fg="white")
    generate_button.pack(pady=20)

    result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#F0F0F0")
    result_label.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    mode = input("Select mode: 1 for CLI, 2 for GUI: ").strip()
    if mode == '1':
        run_cli()
    elif mode == '2':
        run_gui()
    else:
        print("Invalid mode selected.")
