import tkinter as tk
from tkinter import messagebox
import random

class RPSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors")
        
        # UI Elements
        self.choice_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
        self.choice_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        
        self.rock_btn = tk.Button(root, text="Rock", command=lambda: self.play("Rock"))
        self.rock_btn.grid(row=1, column=0, padx=10, pady=10)
        
        self.paper_btn = tk.Button(root, text="Paper", command=lambda: self.play("Paper"))
        self.paper_btn.grid(row=1, column=1, padx=10, pady=10)
        
        self.scissors_btn = tk.Button(root, text="Scissors", command=lambda: self.play("Scissors"))
        self.scissors_btn.grid(row=1, column=2, padx=10, pady=10)
        
        self.result_label = tk.Label(root, text="Result:")
        self.result_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
        
        self.result_display = tk.Label(root, text="")
        self.result_display.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
    
    def play(self, user_choice):
        choices = ["Rock", "Paper", "Scissors"]
        comp_choice = random.choice(choices)
        
        if user_choice == comp_choice:
            result = "It's a tie!"
        elif (user_choice == "Rock" and comp_choice == "Scissors") or \
             (user_choice == "Paper" and comp_choice == "Rock") or \
             (user_choice == "Scissors" and comp_choice == "Paper"):
            result = f"You win! Computer chose {comp_choice}."
        else:
            result = f"You lose! Computer chose {comp_choice}."
        
        self.result_display.config(text=result)

if __name__ == "__main__":
    root = tk.Tk()
    app = RPSApp(root)
    root.mainloop()
