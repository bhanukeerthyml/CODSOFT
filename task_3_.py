import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        
        # UI Elements
        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.length_entry = tk.Entry(root)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
        self.result_label = tk.Label(root, text="Generated Password:")
        self.result_label.grid(row=2, column=0, padx=10, pady=10)
        
        self.result_display = tk.Entry(root, state='readonly')
        self.result_display.grid(row=2, column=1, padx=10, pady=10)
    
    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 1:
                raise ValueError("Password length must be at least 1.")
            
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for i in range(length))
            
            self.result_display.config(state='normal')
            self.result_display.delete(0, tk.END)
            self.result_display.insert(0, password)
            self.result_display.config(state='readonly')
        except ValueError as ve:
            messagebox.showerror("Error", f"Value Error: {ve}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
