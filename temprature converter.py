import tkinter as tk
from tkinter import messagebox

# Create window
window = tk.Tk()
window.title("Temperature Converter")
window.geometry("400x300")
window.configure(bg="#f0f0f0")

# Functions
def celsius_to_fahrenheit():
    try:
        c = float(entry_temp.get())
        f = (c * 9/5) + 32
        result_label.config(text=f"Fahrenheit: {f:.2f} °F")
    except:
        messagebox.showerror("Error", "Please enter a valid number")

def fahrenheit_to_celsius():
    try:
        f = float(entry_temp.get())
        c = (f - 32) * 5/9
        result_label.config(text=f"Celsius: {c:.2f} °C")
    except:
        messagebox.showerror("Error", "Please enter a valid number")

def clear():
    entry_temp.delete(0, tk.END)
    result_label.config(text="Result will appear here")

# Title Label
title_label = tk.Label(window, text="Temperature Converter",
                       font=("Arial", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Entry
entry_temp = tk.Entry(window, font=("Arial", 14), justify="center")
entry_temp.pack(pady=10)

# Buttons
btn_c_to_f = tk.Button(window, text="Celsius → Fahrenheit",
                       command=celsius_to_fahrenheit, bg="#4CAF50", fg="white")
btn_c_to_f.pack(pady=5)

btn_f_to_c = tk.Button(window, text="Fahrenheit → Celsius",
                       command=fahrenheit_to_celsius, bg="#2196F3", fg="white")
btn_f_to_c.pack(pady=5)

btn_clear = tk.Button(window, text="Clear",
                      command=clear, bg="#f44336", fg="white")
btn_clear.pack(pady=5)

# Result Label
result_label = tk.Label(window, text="Result will appear here",
                        font=("Arial", 12), bg="#f0f0f0")
result_label.pack(pady=15)

# Run application
window.mainloop()