#Simple Calculator for understanding how to switch between multiple functions in python

import math

def Addition():
    print("Addition")
    n = int(input("Enter first number: "))
    ans = 0
    while n != None:
        m = int(input("Enter second number to calculate:  "))
        ans = m + n
        print("{} + {} = {}".format(n, m, ans))
        return ans

def Subtraction():
    print("Subtraction")
    n = float(input("Enter first number: "))
    ans =  0    
    while n != None:
        m = float(input("Enter second number to calculate: "))
        ans = n - m
        print("{} - {} = {}".format(n, m, ans))
        return ans

def Multiplication():
    print("Multiplication")
    n = float(input("Enter first number: "))
    ans = 0
    while n != None:
        m = float(input("Enter second number to calculate: "))
        ans = n * m
        print("{} * {} =  {}".format(n, m, ans))
        return ans

def Division():
    print("Division")
    n = float(input("Enter first number: "))
    ans = 0
    while n != None:
        m = float(input("Enter second number to calculate: "))
        ans = n / m
        print("{} / {} =  {}".format(n, m, ans))
        return ans

def Exponents():
    print("Exponents")
    n = float(input("Enter first number: "))
    m = float(input("Enter power: "))
    if n != None:
        ans = math.pow(n,m)
        print("{} ^ {} = {}".format(n, m, ans))

def Eulers():
    print("Eulers Constant")
    n = float(input("Enter power to raise e: "))
    ans = math.exp(n)
    print("e^ {} = {}".format(n, ans))

def Factorial():
    print("Factorial")
    n = int(input("Enter value to factor: "))
    ans = math.factorial(n)
    print("{}! = {}".format(n, ans))

def Start_Calc():
    Start = input("Would you like to perform a calculation? (Yes, No) ")
    while Start == "Yes":

        print("What type of calculation would you like to use?")
        function = input("(Addition, Subtraction, Multiplication, Division, Exponents, Eulers, Factorial) " )
        if function == "Addition":
            Addition()
            Start = input("Would you like to perform another calculation? (Yes, No) ")
        elif function == "Subtraction":
            Subtraction()
            Start = input("Would you like to perform another calculation? (Yes, No) ")
        elif function == "Multiplication":
            Multiplication()
            Start = input("Would you like to perform another calculation? (Yes, No) ")
        elif function == "Exponents":
            Exponents()
            Start = input("Would you like to perform another calculation? (Yes, No) ")
        elif function == "Eulers":
            Eulers()
            Start = input("Would you like to perform another calculation? (Yes, No) ")
        elif function == "Factorial":
            Factorial()
            Start = input("Would you like to perform another calculation? (Yes, No) ")

    else:
        print("Have a good day!")
Start_Calc()