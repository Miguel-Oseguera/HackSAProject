import tkinter as tk
root = tk.Tk()

root.geometry("800x500")
root.title("My first GUI")

label = tk.Label(root, text="HelloWorld!",font=('Arial', 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, font=('Arial', 18))
textbox.pack()

root.mainloop()