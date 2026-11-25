# getting the functions from the calculate file and import python's gui functions
from calculator_functions import calculate
import tkinter as tk
import customtkinter as ctk
import re
num_style = {"width": 60, "height": 60, "corner_radius": 0, "font": ("Helvetica", 22), "fg_color": "#FDFDFD", "hover_color": "#9F9F9F", "text_color":"#000000"}
op_style = {"width": 60, "height": 60, "corner_radius": 0, "font": ("Helvetica", 22), "fg_color": "#0004FF", "hover_color": "#9F9F9F", "text_color":"#FFFFFF"}

gui_window = ctk.CTk()
gui_window.title("Calculator :D")
display = ctk.CTkEntry(gui_window, height=50, font=("Arial", 20), fg_color="#1E1E1E", text_color="#FFFFFF")
display.grid(row=0, column=1, columnspan=4, sticky="ew")
def press(value):
    display.insert(tk.END, value)


# making the functions for the math symbols
def clear():
    display.delete(0, tk.END)     

def equals():
    text = display.get().replace("÷", "/")
    try:
        operators = [char for char in text if char in "+-*/"]
        numbers = [float(var) for var in re.split(r"[+\-*/]", text)]
        result = numbers[0]

        for i in range(len(operators)):
            result = calculate(result, numbers[i + 1], operators[i])

        clear ()
        display.insert(tk.END, result)

    except ValueError:
        clear()
        display.insert(tk.END, "Error")

    except ZeroDivisionError:
        clear()
        display.insert(tk.END, "You can't divide by zero")




    

# row 1

# button 7 
button_7 = ctk.CTkButton(gui_window, text="7", command=lambda: press(7), **num_style)
button_7.grid(row=1, column=1)

# button 8 
button_8 = ctk.CTkButton(gui_window, text="8", command=lambda: press(8), **num_style)
button_8.grid(row=1, column=2)

# button 9
button_9 = ctk.CTkButton(gui_window, text="9", command=lambda: press(9), **num_style)
button_9.grid(row=1, column=3) 

# button / (division)
button_division = ctk.CTkButton(gui_window, text="÷", command=lambda: press("÷"), **op_style)
button_division.grid(row=1, column=4)

# row 2

# button 4
button_4 = ctk.CTkButton(gui_window, text="4", command=lambda: press(4), **num_style)
button_4.grid(row=2, column=1)

# button 5
button_5 = ctk.CTkButton(gui_window, text="5", command=lambda: press(5), **num_style)
button_5.grid(row=2, column=2)

# button 6
button_6 = ctk.CTkButton(gui_window, text="6", command=lambda: press(6), **num_style)
button_6.grid(row=2, column=3)

# button * (multiply)
button_multiply = ctk.CTkButton(gui_window, text="x", command=lambda: press("*"), **op_style)
button_multiply.grid(row=2, column=4)

# row 3

# button 1
button_1 = ctk.CTkButton(gui_window, text="1", command=lambda: press(1), **num_style)
button_1.grid(row=3, column=1)

# button 2
button_2 = ctk.CTkButton(gui_window, text="2", command=lambda: press(2), **num_style)
button_2.grid(row=3, column=2)

# button 3
button_3 = ctk.CTkButton(gui_window, text="3", command=lambda: press(3), **num_style)
button_3.grid(row=3, column=3)

# button - (subtration)
button_subtraction = ctk.CTkButton(gui_window, text="-", command=lambda: press("-"), **op_style)
button_subtraction.grid(row=3, column=4) 

# row 4

# button 0
button_0 = ctk.CTkButton(gui_window, text="0", command=lambda: press(0), **num_style)
button_0.grid(row=4, column=1)

# button C (clear)
button_clear = ctk.CTkButton(gui_window, text="c", command=clear, **op_style)
button_clear.grid(row=4, column=2)

# button = (equals)
button_equals = ctk.CTkButton(gui_window, text="=", command=equals, **op_style)
button_equals.grid(row=4, column=3)

# button + (addition)
button_addition = ctk.CTkButton(gui_window, text="+", command=lambda: press("+"), **op_style)
button_addition.grid(row=4, column=4)

gui_window.mainloop()



