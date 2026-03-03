#PAD X AND Y
import tkinter as tk

root = tk.Tk()
root.title("Tkinter Example")
root.geometry("300x200")

def greet():
    label.config(text="Button Clicked!", fg="green")

label = tk.Label(root, text="Welcome Uzair",
                 fg="blue", bg="lightgray",
                 padx=20, pady=10)

label.pack(pady=10)

button = tk.Button(root, text="Click Me",
                   width=15,
                   command=greet)

button.pack(pady=10)

root.mainloop()
