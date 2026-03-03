import tkinter as tk
from tkinter import messagebox

# Dashboard Window
def open_dashboard():
    dashboard = tk.Toplevel()
    dashboard.title("Dashboard")
    dashboard.geometry("400x300")
    dashboard.configure(bg="#e6f2ff")

    label = tk.Label(dashboard, text="Welcome to Dashboard!",
                     font=("Arial", 16, "bold"), bg="#e6f2ff")
    label.pack(pady=80)

    # Logout button
    def logout():
        dashboard.destroy()
        window.deiconify()

    btn_logout = tk.Button(dashboard, text="Logout", command=logout, bg="red", fg="white")
    btn_logout.pack(pady=10)


# Login Function
def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "1234":
        messagebox.showinfo("Success", "Login Successful")
        window.withdraw()   # Hide login window
        open_dashboard()
    else:
        messagebox.showerror("Error", "Invalid Username or Password")


# Main Window (Login)
window = tk.Tk()
window.title("Login System")
window.geometry("350x250")
window.configure(bg="#f0f0f0")

# Title
title = tk.Label(window, text="Login Form", font=("Arial", 16, "bold"), bg="#f0f0f0")
title.pack(pady=10)

# Username
tk.Label(window, text="Username:", bg="#f0f0f0").pack()
entry_username = tk.Entry(window)
entry_username.pack(pady=5)

# Password
tk.Label(window, text="Password:", bg="#f0f0f0").pack()
entry_password = tk.Entry(window, show="*")
entry_password.pack(pady=5)

# Login Button
btn_login = tk.Button(window, text="Login", command=login, bg="#4CAF50", fg="white")
btn_login.pack(pady=15)

# Run App
window.mainloop()
