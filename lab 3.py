import tkinter as tk
from tkinter import messagebox

# Function for login button
def login_button_click():
    username = entry_username.get()
    password = entry_password.get()

    if username == "uzair" and password == "123":
        messagebox.showinfo("Login Status", "Login Successful ✅")
    else:
        messagebox.showerror("Login Status", "Login Failed ❌")

# Create window
window = tk.Tk()
window.title("Login Page")
window.geometry("350x250")
window.config(bg="lightyellow")

# Heading
label_title = tk.Label(window, text="Login Page!",
                       font=("Arial", 18, "bold"),
                       bg="blue", fg="white")
label_title.pack(pady=10)

# Username Label & Entry
label_username = tk.Label(window, text="Username:", bg="lightyellow")
label_username.pack()

entry_username = tk.Entry(window)
entry_username.pack(pady=5)

# Password Label & Entry
label_password = tk.Label(window, text="Password:", bg="lightyellow")
label_password.pack()

entry_password = tk.Entry(window, show="*")
entry_password.pack(pady=5)

# Login Button
login_button = tk.Button(window, text="Login",
                         command=login_button_click)
login_button.pack(pady=15)

# Run window
window.mainloop()