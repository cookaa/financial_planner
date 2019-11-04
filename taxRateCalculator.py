#!/usr/bin/env python3
"""taxRateCalculator.py  A program to calculate tax rate."""

# Imports
from prettytable import PrettyTable


__author__      = "Adam Cook"
__date__        = "1 November 2019"


# Calculations for Tax Rate
income = 65000
stdDeduction = 6350
perException = 4050
ret401k = 8500

# TODO Calculate Federal Tax Rate
# based on the total amount due based on annual income 
# - 401k Contribution, - Standard deduction - Personal Exception
taxableIncome = (income - stdDeduction - perException - ret401k)

# 2016
# if (taxableIncome < 9275 ):
#     federalTax = taxableIncome * .1
# elif (taxableIncome < 37650):
#     federalTax = 927.50 + ((taxableIncome-9275) * .15)
# elif(taxableIncome < 91150):
#     federalTax = 5183.75 + ((taxableIncome-37650) * .25)
# elif(taxableIncome < 190150):
#     federalTax = 18558.75 + ((taxableIncome-91150) * .28)
# elif(taxableIncome < 413350):
#     federalTax = 46278.75 + ((taxableIncome-190150) * .33)
# elif(taxableIncome < 415050):
#     federalTax = 119934.75 + ((taxableIncome-413350) * .35)
# elif(415051 < taxableIncome):
#     federalTax = 120529.75 + ((taxableIncome-415050) * .396)

# 2018
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


##### Printing out table
x = PrettyTable()

x.field_names = ["Tax Rate %", "Taxable Income @ Rate $", "Federal Income Tax $"]

income = 66000
percentA = 10
percentB = 12
percentC = 22
percentD = 24
percentE = 32
percentF = 25
percentG = 37

taxedIncomeA = income * percentA
x.add_row([percentA, 9275, 9275*taxedIncomeA])
x.add_row([percentB, income-37650, 9275*percentB])
x.add_row([percentC, income, income - (income-37650)*percentC])

x.add_row(["Total:","",""])

print(x)


print("Income: ", income)
print("taxable income: ", taxableIncome)
print("Federal Tax", federalTax)