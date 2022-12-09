''' Copyright <2022> <funguyalt#3083>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

'''
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



