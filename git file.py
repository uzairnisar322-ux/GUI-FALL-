import tkinter as tk
window=tk.Tk()
window.title("My GUI")
window.geometry("500x500")
lable_userName=tk.Label(window,text="UserName",font=("Arial",20),bg="green",fg="red")
lable_userName.pack()
def button_Click():
    print("jamal")
button=tk.Button(window,text="Click me",command=button_Click)
button.pack()


window.mainloop()