import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("tkinter 예제 프로그램")
root.geometry("500x400")

# Create a style
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10)
style.configure("TLabel", font=("Helvetica", 14))

# Create a label
label = ttk.Label(root, text="Welcome to the tkinter 예제 GUI!")
label.pack(pady=10)

# Create a button
button1 = ttk.Button(root, text="Button 1")
button1.pack(pady=5)

button2 = ttk.Button(root, text="Button 2")
button2.pack(pady=5)

button3 = ttk.Button(root, text="Button 3")
button3.pack(pady=5)

# Create an entry
entry = ttk.Entry(root)
entry.pack(pady=5)

# Create a combobox
combobox = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
combobox.pack(pady=5)

# Create a checkbutton
checkbutton = ttk.Checkbutton(root, text="Check me")
checkbutton.pack(pady=5)

# Create a radiobutton
radiobutton1 = ttk.Radiobutton(root, text="Radio 1", value=1)
radiobutton1.pack(pady=5)

radiobutton2 = ttk.Radiobutton(root, text="Radio 2", value=2)
radiobutton2.pack(pady=5)

# Create a progressbar
progressbar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progressbar.pack(pady=5)
progressbar["value"] = 50

# Create a scale
scale = ttk.Scale(root, from_=0, to=100, orient="horizontal")
scale.pack(pady=5)

# Run the application
root.mainloop()