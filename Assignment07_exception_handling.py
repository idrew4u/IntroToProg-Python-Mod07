#-------------------------------#
# Title: # Title: Assignment07_Exception Handling
# Desc: Using Exception Handling in Python
# Chang Log: (Who, When, What)
# ALi,Dec. 1, 2020,Created File
#-------------------------------#

# intro to program
print("\tWe are going to do some basic math.")
print("\tWhen prompted, please enter a number of your choice.")
input("\tPress Enter to Begin.")
print("\n")

try:
    # asks for numbers from user
    number1 = input("Enter a first number: ")
    number1 = float(number1)
    number2 = input("Enter a second number: ")
    number2 = float(number2)

    # computes the math
    add = number1 + number2
    subtract = number1 - number2
    multiply = number1 * number2
    divide = number1 / number2

    # displays the results back to user
    print("The sum of", number1, "and", number2, "is: ", add)
    print("The difference of", number1, "and", number2, "is: ", subtract)
    print("The product of", number1, "and", number2, "is: ", multiply)
    print("The quotient of", number1, "and", number2, "is: ", divide)

except ValueError as e: # error message when a word or fraction is entered
    print()
    print("Error found.")
    print("Please enter an integer.")

except ZeroDivisionError as e: # error message when second number is 0
    print()
    print("Error found.")
    print("Numbers are not divisible by 0.")
    print("Please do not use 0 as the second number.")

except Exception as e: # error message when error does not meet previous two errors
    print()
    print("Error found.")
    print("Please try again.")

    print("Built-In Pythons error info: ")
    print(e, e.__doc__, type(e), sep="\n")

# ends the program
input("\nPress Enter to End Program")
