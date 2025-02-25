import tkinter as tk
from tkinter import ttk


class SimpleGui(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Set up the window
        self.title("Ai Coach")
        self.geometry("400x300")

        # Label widget
        self.label = ttk.Label(self, text="Hello, Tkinter!", font=("Arial", 18))
        self.label.pack(pady=20)

        # Entry widget for input
        self.entry = ttk.Entry(self, width=20)
        self.entry.pack(pady=10)

        # Button to update label text
        self.button = ttk.Button(self, text="Update Text", command=self.update_label)
        self.button.pack(pady=10)

    def update_label(self):
        # Update the label with the content of the entry field
        new_text = self.entry.get()
        self.label.config(text=new_text)
