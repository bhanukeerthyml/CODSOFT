import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        
        self.tasks = []

        
        self.task_input = tk.Entry(root, width=50)
        self.task_input.grid(row=0, column=0, padx=10, pady=10)

        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.delete_task_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.grid(row=2, column=0, padx=10, pady=10)

        self.clear_task_button = tk.Button(root, text="Clear All Tasks", command=self.clear_tasks)
        self.clear_task_button.grid(row=2, column=1, padx=10, pady=10)

    def add_task(self):
        task = self.task_input.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_input.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def clear_tasks(self):
        self.tasks = []
        self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
