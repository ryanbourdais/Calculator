#Simple Calculator for understanding how to switch between multiple functions in python

def Addition():
    print("Addition")
    n = float(input("Enter first number: "))
    ans = 0
    while n != 0:
        m = float(input("Enter second number to calculate:  "))
        ans = m + n
        print("{} + {} = {}".format(n, m, ans))
        return ans

def Subtraction():
    print("Subtraction")
    n = float(input("Enter first number: "))
    ans =  0
    while n != 0:
        m = float(input("Enter second number to calculate: "))
        ans = n - m
        print("{} - {} = {}".format(n, m, ans))
        return ans

def Multiplication():
    print("Multiplication")
    n = float(input("Enter first number: "))
    ans = 0
    while n != 0:
        m = float(input("Enter second number to calculate: "))
        ans = n * m
        print("{} * {} =  {}".format(n, m, ans))
        return ans

def Division():
    print("Division")
    n = float(input("Enter first number: "))
    ans = 0
    while n != 0:
        m = float(input("Enter second number to calculate: "))
        ans = n / m
        print("{} / {} =  {}".format(n, m, ans))
        return ans
Division()