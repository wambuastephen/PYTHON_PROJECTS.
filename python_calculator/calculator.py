#!/usr/bin/env python3
#simple python calc.
#addition functions.
def add(num1, num2):
    return num1 + num2

#subtraction fuction.
def subtraction(num1, num2):
    return num1 - num2

#multiplication fuction.
def multiply(num1, num2):
    return num1 * num2

#division function
def divide(num1, num2):
    return num1 / num2
#modulus function
def modulu(num1,num2):
    return num1 % num2
print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtraction\n" \
        "3. Multiply\n" \
        "4. Divide\n" \
        "5. Modulu\n")
#prompt user to give input
select = int(input("Select operations from 1, 2, 3, 4, 5 :"))
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
if select == 1:
    print(number_1, "+", number_2, "=",
            add(number_1, number_2))

elif select == 2:
    print(number_1, "-", number_2, "=",
            subtraction(number_1, number_2))

elif select == 3:
    print(number_1, "*", number_2, "=",
            multiply(number_1, number_2))

elif select == 4:
    print(number_1, "/", number_2, "=",
            divide(number_1, number_2))

elif select == 5:
    print(number_1, "%", number_2, "=",
            modulu(number_1, number_2))
else:
    print("Select from given arithmetic operations")
