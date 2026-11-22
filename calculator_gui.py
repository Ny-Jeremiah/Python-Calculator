# getting the functions from the calculate file and import python's gui functions
from calculator_functions import calculate
import tkinter as tk

gui_window = tk.Tk()
gui_window.title("Calculator")
gui_window.geometry("300x400")
display = tk.Entry(gui_window)
display.grid(row=0, column=1, columnspan=4)

# row 1

# button 7 
button_7 = tk.Button(gui_window, text="7")
button_7.grid(row=1, column=1)

# button 8 
button_8 = tk.Button(gui_window, text="8")
button_8.grid(row=1, column=2)

# button 9
button_9 = tk.Button(gui_window, text="9")
button_9.grid(row=1, column=3) 

# button / (division)
button_division = tk.Button(gui_window, text="/")
button_division.grid(row=1, column=4)

# row 2

# button 4
button_4 = tk.Button(gui_window, text="4")
button_4.grid(row=2, column=1)

# button 5
button_5 = tk.Button(gui_window, text="5")
button_5.grid(row=2, column=2)

# button 6
button_6 = tk.Button(gui_window, text="6")
button_6.grid(row=2, column=3)

# button * (multiply)
button_multiply = tk.Button(gui_window, text="*")
button_multiply.grid(row=2, column=4)

# row 3

# button 1
button_1 = tk.Button(gui_window, text="1")
button_1.grid(row=3, column=1)

# button 2
button_2 = tk.Button(gui_window, text="2")
button_2.grid(row=3, column=2)

# button 3
button_3 = tk.Button(gui_window, text="3")
button_3.grid(row=3, column=3)

# button - (subtration)
button_subtraction = tk.Button(gui_window, text="-")
button_subtraction.grid(row=3, column=4)

# row 4

# button 0
button_0 = tk.Button(gui_window, text="0")
button_0.grid(row=4, column=1)

# button C (clear)
button_clear = tk.Button(gui_window, text="c")
button_clear.grid(row=4, column=2 )

# button = (equals)
button_equals = tk.Button(gui_window, text="=")
button_equals.grid(row=4, column=3)

# button + (addition)
button_addition = tk.Button(gui_window, text="+")
button_addition.grid(row=4, column=4)









gui_window.mainloop()



