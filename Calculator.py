import tkinter as tk
from tkinter import ttk
import math


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Calculator")
        self.root.geometry("300x400")
        self.root.configure(bg="#9ED33C")
        
        # Entry field for display
        self.display = tk.Entry(root, font=('Arial', 20), justify='right', bg="#34495E", fg="white")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        
        # Button style
        style = ttk.Style()
        style.configure('Calc.TButton', font=('Arial', 12), padding=10)
        
        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', '√', '^2', 'DEL'
        ]
        
        # Create and place buttons
        row = 1
        col = 0
        for button in buttons:
            btn = ttk.Button(root, text=button, style='Calc.TButton', 
                           command=lambda x=button: self.button_click(x))
            btn.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Configure grid weights
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
    
    def button_click(self, value):
        current = self.display.get()
        
        if value == 'C':
            self.display.delete(0, tk.END)
        elif value == 'DEL':
            self.display.delete(len(current)-1)
        elif value == '=':
            try:
                result = eval(current)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif value == '√':
            try:
                result = math.sqrt(float(current))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif value == '^2':
            try:
                result = float(current) ** 2
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            self.display.insert(tk.END, value)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()