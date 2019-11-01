#!/usr/bin/env python3
"""taxRateCalculator.py  A program to calculate tax rate."""

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