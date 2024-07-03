import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        
        # UI Elements
        self.first_number_label = tk.Label(root, text="First Number:")
        self.first_number_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.first_number_entry = tk.Entry(root)
        self.first_number_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.second_number_label = tk.Label(root, text="Second Number:")
        self.second_number_label.grid(row=1, column=0, padx=10, pady=10)
        
        self.second_number_entry = tk.Entry(root)
        self.second_number_entry.grid(row=1, column=1, padx=10, pady=10)
        
        self.operation_label = tk.Label(root, text="Operation (+, -, *, /):")
        self.operation_label.grid(row=2, column=0, padx=10, pady=10)
        
        self.operation_entry = tk.Entry(root)
        self.operation_entry.grid(row=2, column=1, padx=10, pady=10)
        
        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        
        self.result_label = tk.Label(root, text="Result:")
        self.result_label.grid(row=4, column=0, padx=10, pady=10)
        
        self.result_display = tk.Label(root, text="")
        self.result_display.grid(row=4, column=1, padx=10, pady=10)
    
    def calculate(self):
        try:
            first_number = float(self.first_number_entry.get())
            second_number = float(self.second_number_entry.get())
            operation = self.operation_entry.get().strip()
            
            if operation == "+":
                result = first_number + second_number
            elif operation == "-":
                result = first_number - second_number
            elif operation == "*":
                result = first_number * second_number
            elif operation == "/":
                if second_number != 0:
                    result = first_number / second_number
                else:
                    raise ZeroDivisionError("Cannot divide by zero")
            else:
                raise ValueError("Invalid operation. Use +, -, *, or /")
            
            self.result_display.config(text=str(result))
        except ValueError as ve:
            messagebox.showerror("Error", f"Value Error: {ve}")
        except ZeroDivisionError as zde:
            messagebox.showerror("Error", f"Zero Division Error: {zde}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
