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
print(color.BOLD + color.BLUE + "\n\t\tWelcome to Cook's Financial Planner. \n\nThis program is designed to help determine how much you will need to save for retirement.\n\n" + color.END)

# Prompt the user for questions
print("Please anwser each question with (True) or (False)\n")

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

print("Please anwser each question with a number. (0-99) \n")
localTaxRate = input("What is you local tax rate %? ")
stateTaxRate = input("What is you state tax rate %? ")


# Logistic Questions

#TODO Add Parser to parse anwsers to ouput only int
retirementAge = input("At what age would you like to retire? (Avg 65) ")
futureIncome = input("What is the median salary for that job? ")

# Tax Questions
income = input("What is you projected starting salary? ")
stdDeduction = input("What is your Standard Deduction? ")
perException = input("What is your Peronal exception? ")
ret401k = input("How much are you setting aside in your 401k? ")

# Example Tax Imput
# income = 65000
# stdDeduction = 6350
# perException = 4050
# ret401k = 8500

# Locational Inforamtion
print("\nPlease anwser each question with a word. \n")

field = input("What field do you wish to go into? ")
state = input("What State do you live in? ")
county = input("What is the name of your County? ")

# Retirment Questins
ageExpectancy = input("Your Life Expectancy ")
currentAge = input("Current Age ")
ssIncome = input("Expected Social Security Income ")
otherIncome = input("Other Income After Retirement ")
inflation = 3 # inflation = input("Inflation Rate ")   # Assuming inflation rate of 3%
retirementPercentage = input("Income Needed After Retiremen (70-80% To Maintain Life Style) ")
dependants = input("Do you have any Dependants? ")

##### Calculations for Tax Rate #####

# TODO Calculate Federal Tax Rate
# based on the total amount due based on annual income 
# - 401k Contribution, - Standard deduction - Personal Exception
taxableIncome = (income - stdDeduction - perException - ret401k)

if (taxableIncome < 19050 ):
    federalTax = taxableIncome * .1
elif (taxableIncome < 77,400):
    federalTax = 1,905 + ((taxableIncome-9275) * .12)
elif(taxableIncome < 165000):
    federalTax = 8,907 + ((taxableIncome-37650) * .22)
elif(taxableIncome < 315000):
    federalTax = 28,179 + ((taxableIncome-91150) * .24)
elif(taxableIncome < 400000):
    federalTax = 64,179 + ((taxableIncome-190150) * .32)
elif(taxableIncome < 600000):
    federalTax = 91,379 + ((taxableIncome-413350) * .35)
elif(600001 < taxableIncome):
    federalTax = 161,379 + ((taxableIncome-415050) * .37)

# Local Tax
localTax = income * localTaxRate

# State Tax Rate
stateTax = income * stateTaxRate

##### End of tax calculations #####

print("Income: ", income)
print("taxable income: ", taxableIncome)
print("Federal Tax", federalTax)



##### Calculations for Retirement Age #####

# TODO Calculate the total amount needed per year for retirement
annualRetirementGoal =retirementPercentage * income * inflation             # Total needed per year retirment
totalRetirment = (annualRetirementGoal) * (ageExpectancy - retirementAge)   # Total amount needed to save
savePerYear = totalRetirment / (retirementAge - currentAge)                 # Goal amount to save per year till retirement

##### End of Calculations for Retirement Age #####


##### Printing out Results #####

# TODO import pretty table to format ouput table
# TODO print out all results

##### End of Printing out Results #####

'''Utilized resources: 
https://pittsburghpa.gov/finance/tax-descriptions
https://www.irs.com/articles/2018-federal-tax-rates-personal-exemptions-and-standard-deductions,
https://apps.irs.gov/app/tax-withholding-estimator,
https://www.calculator.net/retirement-calculator.html'''