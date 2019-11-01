#!/usr/bin/env python3
"""financial_planner.py  A program to help people figure out how much to save for retirement."""

__author__      = "Adam Cook"
__date__        = "31 October 2019"

# Adding a few color and emphisis options for text
class color:
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# Welcome Message
print(color.BOLD + color.BLUE + "\n\tWelcome to Cook's Financial Planner. \n\nThis program is designed to help determine how much you will need to save for retirement.\n\n\t Let's begin.\n" + color.END)

# Prompt the user for questions
print("Please anwser each question with: \n\n\t(True) or (False)\n")

# Ethical Questions
e0 = input("Do you want to retire? ")
e1 = input("Do you want to be financially stable throughout retiremnt? ")
e2 = input("Are you willing to live within your means? ")

#TODO convert e anwsers to Boolean so check can funcion correctly
if (e0 and e1 and e2 == True):
    print("\nWelcome to the program!\n I am glad to help you accomplish your saving goals.\n")
    

# Tax Questions
t0 = input("\nWill you be filing as \"Single\" on the IRS? (True/False) ")
if (t0 == False):
    t1 = input("Will you be filing as \"Married or joined\" on the IRS? (True/False) ")

print("Please anwser each question with a number. \n")
t2 = input("What is you local tax rate %? ")
t3 = input("What is you state tax rate %? ")


# Logistic Questions

#TODO Add Parser to parse anwsers to ouput only int
retirementAge = input("At what age would you like to retire? (Avg 65) ")
futureIncome = input("What is the median salary for that job? ")

# Tax Questions
income = input("What is you projected starting salary? ")
stdDeduction = input("What is your Standard Deduction? ")
perException = input("What is your Peronal exception? ")
ret401k = input("How much are you setting aside in your 401k? ")


# Locational Inforamtion
print("\nPlease anwser each question with a word or two. \n")

l0 = input("What field do you wish to go into? ")
l1 = input("What State do you live in? ")
l2 = input("What is the name of your County? ")


# Prints out table of data collected

# Header for the Table
print(color.BOLD + "\n\t\t\tTable for Data Collected\n" + color.END)
print("\t+{:-^97}+".format(""))
style_tax  = "| {:^7} | {:^7} | {:^7} |"
print("Tax Rates: ", style_tax.format("Federal","State","Local"))
print("\t\t", style_tax.format(e0,e1,e2))

# Calculations for Tax Rate
income = 65000
stdDeduction = 6350
perException = 4050
ret401k = 8500

# TODO Calculate Federal Tax Rate
# based on the total amount due based on annual income 
# - 401k Contribution, - Standard deduction - Personal Exception
taxableIncome = (income - stdDeduction - perException - ret401k)

if (taxableIncome < 9275 ):
    federalTax = taxableIncome * .1
elif (taxableIncome < 37650):
    federalTax = 927.50 + ((taxableIncome-9275) * .15)
elif(taxableIncome < 91150):
    federalTax = 5183.75 + ((taxableIncome-37650) * .25)
elif(taxableIncome < 190150):
    federalTax = 18558.75 + ((taxableIncome-91150) * .28)
elif(taxableIncome < 413350):
    federalTax = 46278.75 + ((taxableIncome-190150) * .33)
elif(taxableIncome < 415050):
    federalTax = 119934.75 + ((taxableIncome-413350) * .35)
elif(415051 < taxableIncome):
    federalTax = 120529.75 + ((taxableIncome-415050) * .396)

print("Income: ", income)
print("taxable income: ", taxableIncome)
print("Federal Tax", federalTax)
# Calculations for Retirement Age

