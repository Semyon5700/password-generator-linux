#!/usr/bin/env python3

"""
Password Generator GUI Application
Author: Semyon5700
License: GPL-3.0
"""

import tkinter as tk
from tkinter import messagebox
import random
import string
import subprocess
import os

class PasswordGenerator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Password Generator")
        self.root.geometry("500x300")
        self.root.resizable(False, False)
        self.setup_ui()
    
    def setup_ui(self):
        main_frame = tk.Frame(self.root, padx=25, pady=25)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(main_frame, text="Password Length:", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=8)
        
        self.length_var = tk.StringVar(value="16")
        length_entry = tk.Entry(main_frame, textvariable=self.length_var, width=8, font=("Arial", 10))
        length_entry.grid(row=0, column=1, sticky="w", pady=8, padx=(10,0))
        
        self.use_uppercase = tk.BooleanVar(value=True)
        self.use_lowercase = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_special = tk.BooleanVar(value=True)
        
        tk.Checkbutton(main_frame, text="A-Z", variable=self.use_uppercase, font=("Arial", 9)).grid(row=1, column=0, sticky="w", pady=3)
        tk.Checkbutton(main_frame, text="a-z", variable=self.use_lowercase, font=("Arial", 9)).grid(row=1, column=1, sticky="w", pady=3)
        tk.Checkbutton(main_frame, text="0-9", variable=self.use_digits, font=("Arial", 9)).grid(row=2, column=0, sticky="w", pady=3)
        tk.Checkbutton(main_frame, text="!@#$%", variable=self.use_special, font=("Arial", 9)).grid(row=2, column=1, sticky="w", pady=3)
        
        tk.Label(main_frame, text="Generated Password:", font=("Arial", 10)).grid(row=3, column=0, columnspan=2, sticky="w", pady=(15,5))
        
        self.password_var = tk.StringVar()
        password_entry = tk.Entry(main_frame, textvariable=self.password_var, font=("Courier", 12, "bold"), state='readonly', width=35)
        password_entry.grid(row=4, column=0, columnspan=2, sticky="we", pady=8)
        
        button_frame = tk.Frame(main_frame)
        button_frame.grid(row=5, column=0, columnspan=2, pady=20)
        
        generate_btn = tk.Button(button_frame, text="Generate Password", command=self.generate_password, width=18, height=2, font=("Arial", 10, "bold"), bg="#4CAF50", fg="white")
        generate_btn.pack(side=tk.LEFT, padx=8)
        
        copy_btn = tk.Button(button_frame, text="Copy Password", command=self.copy_password, width=18, height=2, font=("Arial", 10, "bold"), bg="#2196F3", fg="white")
        copy_btn.pack(side=tk.LEFT, padx=8)
        
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
    
    def generate_password(self):
        try:
            length = int(self.length_var.get())
            if length < 4 or length > 64:
                messagebox.showerror("Error", "Password length must be between 4 and 64 characters")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
            return
        
        characters = ""
        if self.use_uppercase.get():
            characters += string.ascii_uppercase
        if self.use_lowercase.get():
            characters += string.ascii_lowercase
        if self.use_digits.get():
            characters += string.digits
        if self.use_special.get():
            characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        if not characters:
            messagebox.showerror("Error", "Please select at least one character type")
            return
        
        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_var.set(password)
    
    def copy_password(self):
        password = self.password_var.get()
        if not password:
            messagebox.showwarning("Warning", "Please generate a password first")
            return
        
        try:
            process = subprocess.Popen(['xclip', '-selection', 'clipboard'], stdin=subprocess.PIPE)
            process.communicate(input=password.encode('utf-8'))
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            self.root.update()
            messagebox.showinfo("Success", "Password copied to clipboard!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to copy password: {str(e)}")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = PasswordGenerator()
    app.run()
