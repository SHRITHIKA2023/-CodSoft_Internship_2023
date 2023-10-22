#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 00:29:14 2023

@author: shrutika
"""

a = input("Enter the First number:")
b = input("Enter the Second number:")
print("Please select operation which should be performed : \n" \
        "1. Addtion\n" \
        "2. Subtraction\n" \
        "3. Multiplication\n" \
        "4. Division\n")
 
 
# Take input from the user
choice = int(input("Select operations form 1, 2, 3, 4 :"))

if choice == 1:
        add = int(a) + int(b)
        print("The Sum of two numbers is:", add)
elif choice == 2:
        sub = int(a) - int(b)
        print("The Difference of two numbers is:", sub)
elif choice == 3:
        mul = int(a) * int(b)
        print("The Product of two numbers is:", mul)
elif choice == 4:
 if int(b) == 0:
            print("Cannot divide by zero")
 else:
            div = int(a) / int(b)
            print("The division of two numbers is:", div)
else:
        print('Invalid choice')
 
    

        

    


