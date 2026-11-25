# Adding an import systems to close to program
import sys

# Making a manual function for the gui 
def calculate(answer_1, answer_2, math_operator):
 if math_operator == "+":
     return answer_1 + answer_2
 elif math_operator == "-":
     return answer_1 - answer_2
 elif math_operator == "*":
     return answer_1 * answer_2
 elif math_operator == "/":
     return answer_1 / answer_2
 elif math_operator == "//":
     return answer_1 // answer_2
 elif math_operator == "%":
     return answer_1 % answer_2

# This file's label
if __name__ == "__main__": 

    # Base input
    print("Hello user, enter two numbers please. Make sure you use ',' in your input: ") 
    

    # Using the While loop and try and except as safe gaurds
    while True:
        user_input = input()
        
        # to let the user quit out of the calculator
        if user_input.strip().lower() == "quit":
            print("Quitting the calculator, good day!")
            sys.exit()

        # Another safe guard in place for an invalid input from the user
        try:
         var_list = [
            float(value.strip()) for value in user_input.split(",") if value.strip()
            ]
        except ValueError:
         print("Please enter number, like 1, 2.")
         continue

        if len(var_list) != 2:
         print("Please enter exactly two numbers.")
         continue

        break
        

    # Final base answers
    answer_1 = var_list[0]
    answer_2 = var_list[1]

    print(
    F"The first number is: '{answer_1}' "
    F"\nThe second number is: '{answer_2}' "
    )

    # using math operator with the cleaned inputs from the user

    # Using while loop and continue as safeguards so that the program doesn't crash
    while True:
     print("Choose a math operator: ")
     math_operator = input().strip()

     if math_operator == "":
        print("You didn't type anything, please try again: ")
        continue

     if math_operator not in ("+", "-", "*", "/", "//", "%"):
        print(F" {math_operator} is not a math operator. please try again: ")
        continue

     if math_operator in ("/", "//", "%") and answer_2 == 0:
        print("You can't divide by zero, please try again: ")
        continue

     break


    # Finalization of the data
    print("Result:", calculate(answer_1, answer_2, math_operator))





 
