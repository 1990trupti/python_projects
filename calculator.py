
from simple_calculator_program import *

while True:
    print("What do you want to do?")
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Division")
    print("Enter Q to Exit")

    choice = input("Enter your choice: ")
    if choice == 'q' or choice =='Q':
        break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Emter the second number: "))

    if choice == '1':
        addition(num1,num2)
    elif choice == '2':
        subtraction(num1,num2)
    elif choice == '3':
        multiplication(num1,num2)
    elif choice == '4':
        division(num1,num2)
    else:
        print("Invalid choice")

    print("\n")
