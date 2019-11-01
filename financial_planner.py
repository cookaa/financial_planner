#!/usr/bin/env python3
"""financial_planner.py  A program to help people figure out how much to save for retirement."""

__author__      = "Adam Cook"
__date__        = "31 October 2019"

# Welcome Message
print("\n\tWelcome to Cook's Financial Planner. \n\nThis program is designed to help determine how much you will need to save for retirement.\n\n\t Let's begin.\n")

# Prompt the user for questions
print("Please anwser each question with: \n\n\t(True) or (False)\n")

# Ethical Questions
e0 = input("Do you want to retire? ")
e1 = input("Do you want to be financially stable throughout retiremnt? ")
e2 = input("Are you willing to live within your means? ")

#TODO convert e anwsers to Boolean
if (e0 and e1 and e2 == True):
    print("\nWelcome to the program!\n I am glad to help you accomplish your saving goals.\n")
    

# Tax Questions
t0 = input("Will you be filing as \"Single\" on the IRS? \n(True/False) ")
if (t0 == False):
    t1 = input("Will you be filing as \"Married or joined\" on the IRS? \n(True/False) ")

print("Please anwser each question with a number. \n")
t2 = input("What is you local tax rate %? ")
t3 = input("What is you state tax rate %? ")


# Logistic Questions

#TODO Add Parser to parse anwsers to ouput only int
q0 = input("At what age would you like to retire? (Avg 65) ")
q1 = input("What is you projected starting salary? ")
q2 = input("What is the median salary for that job? ")


# Locational Inforamtion
print("Please anwser each question with a word or two. \n")

l0 = input("What field do you wish to go into? ")
l1 = input("What State do you live in? ")
l2 = input("What is the name of your County? ")


# Prints out table of data collected

# Header for the Table
print("\n\t\t\tTable for Data Collected\n")
print("\t+{:-^97}+".format(""))
style_tax  = "| {:^7} | {:^7} | {:^7} |"
print("Tax Rates: ", style_tax.format("Federal","State","Local"))
print("\t\t", style_tax.format(e0,e1,e2))

# Calculations for Retirement Age


main()