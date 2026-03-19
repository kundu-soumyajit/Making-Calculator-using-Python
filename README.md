🧠 Overall Idea

This program creates a modern GUI calculator using Tkinter in Python. It supports basic arithmetic operations along with square root, square, clear, and delete functions.

🧩 Structure of the Code

1. Imports

Python
import tkinter as tk
from tkinter import ttk
import math

●tkinter → for GUI

●ttk → for styled buttons

●math → for advanced operations like square root

2. Class: Calculator

●Encapsulates the whole calculator logic

●Uses OOP (Object-Oriented Programming)

3. Constructor __init__

●Sets window title, size, and background color

●Creates display entry box for input/output

●Defines button styles using ttk.Style()

●Creates calculator buttons dynamically using a loop

●Uses grid layout for proper alignment

4. Buttons Layout

Includes:

●Numbers: 0–9

●Operators: + - * /

●Special:

   ○ C → Clear screen

   ○ DEL → Delete last character

   ○ = → Evaluate expression

   ○ √ → Square root

   ○ ^2 → Square

5. Method: button_click(self, value)
Handles all button actions:

●C → clears display

●DEL → deletes last character

●= → evaluates expression using eval()

●√ → calculates square root using math.sqrt()

●^2 → squares the number

●Else → appends value to display

👉 Uses try-except to handle errors safely

6. Grid Configuration

Python
self.root.grid_rowconfigure(i, weight=1)
self.root.grid_columnconfigure
(i, weight=1)

●Makes UI responsive and properly spaced

7. Main Block

Python
if __name__ == "__main__":

●Starts the application
●Creates window and runs main loop

⚡ Key Concepts Used

GUI Programming (Tkinter)
OOP (Class & Methods)
Event Handling (Button Clicks)
Exception Handling (try-except)
Dynamic Button Creation (loop)