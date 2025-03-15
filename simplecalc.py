# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 22:58:29 2025

@author: hp
"""

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return"invalid, divide by 0 cant possible"
    return a/b
while True:
    print("---Simple Calculator---")
    print("1.Add")
    print("1.subtract")
    print("1.multiply")
    print("1.divide")
    print("1.Exit")
    choice = input("Enter your choice: ")
    if choice == "5":
        print("bye!")
        break
    if choice in ("1","2","3","4"):
        try:
            num1 = float(input("Enter 1st no: "))
            num2 = float(input("Enter 2nd no : "))
            if choice =="1":
                print("Result: ",add(num1,num2))
            elif choice =="2":
                print("Result: ",sub(num1,num2))
            elif choice =="3":
                print("Result: ",multi(num1,num2))
            elif choice =="4":
                print("Result: ",divide(num1,num2))
        except ValueError:
            print("Invalid input")
    else:
        print("Invalid choice")