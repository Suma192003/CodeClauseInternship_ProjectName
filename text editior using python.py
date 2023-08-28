import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text.delete("1.0", tk.END)

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            text.delete("1.0", tk.END)
            text.insert("1.0", content)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as file:
            content = text.get("1.0", tk.END)
            file.write(content)

def about():
    messagebox.showinfo("About", "A simple text editor created with Python and tkinter.")

root = tk.Tk()
root.title("Simple Text Editor")

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

text = tk.Text(root)
text.pack(fill=tk.BOTH, expand=True)

root.mainloop()