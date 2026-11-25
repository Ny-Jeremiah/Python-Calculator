# Python-based calculator project
This is a calculator that was built with python. It comes with two interfaces, a Command Line Interface (CLI) and Graphical User Interface (GUI).

# The files
- calculator_functions.py - The CLI version of the program. This file also plays the role as the backend for the GUI.
- calculator_gui.py - The Graphical user interface that is built on top of the backend file (calculator_functions.py)

# How to run the program
1. Install the requirements:
```
pip install -r requirements.txt
```
2. Run the GUI version:
```
python calculator_gui.py
```
Or run the CLI version:
```
python calculator_functions.py
```

# Things I have learned
Honestly, for my first project I have learned a lot. Here is a list:
1. To use Python to its fullest potential, you'll have to treat it like Linux. Install packages. This project in particular uses 2 (tkinter and customtkinter)
2. Make sure to implement safeguards for your programming. 
3. With multiple files, the backend needs `if __name__ == "__main__":` so its CLI code doesn't run when the GUI imports it.

I'm going to try to make a project every semester, as not only does it help me apply my knowledge in a real world environment, but it also helps me build my skills at a very fast pace!