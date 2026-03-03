import tkinter as tk

# Create window
window = tk.Tk()
window.title("Simple Form")
window.geometry("400x200")

# Labels
label_name = tk.Label(window, text="Name:", font=("Arial", 12))
label_email = tk.Label(window, text="Email:", font=("Arial", 12))

# Entry fields
entry_name = tk.Entry(window, width=30)
entry_email = tk.Entry(window, width=30)

# Button function
def submit():
    name = entry_name.get()
    email = entry_email.get()
    print("Name:", name)
    print("Email:", email)

# Submit button
submit_btn = tk.Button(window, text="Submit", command=submit)

# Using grid layout
label_name.grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_name.grid(row=0, column=1, padx=10, pady=10)

label_email.grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_email.grid(row=1, column=1, padx=10, pady=10)

submit_btn.grid(row=2, column=0, columnspan=2, pady=20)

# Run application
window.mainloop()