#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 18:49:07 2023

@author: shrutika
"""
import random
your_choice=input("enter your choice (Rock,Paper,Scissors)\n")

option=["Rock","Paper","Scissors"]
system_choice=random.choice(option)

print("You have choosen:\n",your_choice)
print("System has choosen:\n",system_choice)


###if else function to find which move to be playe dand what result 
#will come out

if your_choice==system_choice:
    print(f"its is a tire has both of you have choosen the same move{system_choice}")
elif your_choice=="Rock":
    if system_choice == "Paper":
        print("You lose system wins as Paper covers Rock")
    else:
        print("You win , as Rock Hits Scissors")
elif your_choice == "Paper":
    if system_choice =="Scissors":
        print("You lose system wins as Scissors cuts Paper")
    else:
        print("You win,as Paper covers Rock.")
elif your_choice == "Scissors":
    if system_choice == "Rock":
        print("You lose system wins as  Rock hits Scissors")
    else:
        print("You win, as Scissors cuts Paper.")

             
        
    