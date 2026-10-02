# ---------------------------------------------
# Name: Thomas Butler
# Date: 01-October-2026
# Project: Project 3
# Status: WIP
# Class: COSC 1336 (20)
# ---------------------------------------------
# Project Objectives
# Description

#A local delivery company, AllyBaba Express, charges customers based on the weight of packages shipped during the month.
#The company uses the following monthly shipping rate structure:
# $2.00 per package for fewer than 10 packages  
# $1.75 per package for 10–24 packages  
# $1.50 per package for 25–49 packages  
# $1.25 per package for 50 or more packages  
#In addition, every customer pays a flat monthly service fee of $15.00.
#-----------------
#1. Prompts the user to enter:  
#       Customer name  
#       Number of packages shipped during the month  
#2. Calculates:  
#       Shipping charges  
#       Total monthly charges  
#3. Displays a formatted summary showing:  
#       Customer name  
#       Number of packages shipped  
#       Shipping rate used  
#       Total monthly charges  
# ---------------------------------------------
#Your program must validate the input.
#       If the user enters a negative number for packages shipped, display the following message:  
#               ERROR: Number of packages cannot be negative.
#       The program should not perform any calculations when invalid input is entered.  

# This function will display the start of the project
def main():
    # Calls function to display the start of project
    projectStart()

    # Call and function to ask user name and number of packages. assign returned data to variable so it can pass to calculate function
    cusName, qty = promptUser()

    # Call function to calculate shipping rate and total monthly charges. assign to variables to be passed to display function
    shipRate, totMonCharges = calculateCharges(qty)

    # Call function to display a formatted summary showing Customer name, Number of packages shipped, Shipping rate used Total monthly charges
    displayResults(cusName, qty, shipRate, totMonCharges)

    # Calls function to display the end of project
    projectEnd()
   
def projectStart():
    print('Start of Project 3')
    print('Written by: Thomas Butler')
    print('Date: 01-10-2026')
    print(squigglyWrap('Bank Fees'))

# This function will display the start of the project
def projectEnd():
    print(squigglyWrap('End of Project 3'))

# This function will return an integer input from the user
def getIntegerData(prompt):
    # Error validation
    while(True):
        value = int(input(prompt))
       
        # Throw error for negative input
        if value < 0:
            print('ERROR: Number of packages cannot be negative.')
       
        # Return valid input
        else:
            return value

# This function will return a float input from the user
#def getFloatData(prompt):
    #value = float(input(prompt))
    #return value

# This function will return a string input from the user
def getStringData(prompt):
    value = input(prompt)
    return value

# This function will print 51-character squiggly borders above and below the string parameter
def squigglyWrap(text):
    squiggly = '\n' + '~ ' * 25 + '~\n'
    wrapped = squiggly + '\t' + text + squiggly
    return wrapped

def promptUser():
    name = getStringData('\nPlease enter customer name:\t')
    numPkgs = getIntegerData('\nPlease enter number of packages shipped during the month:\t')
    return name, numPkgs

def calculateCharges(numPkgs):
    if numPkgs < 10:
        rate = 2
    elif 10 <= numPkgs <= 24:
        rate = 1.7
    elif 25 <= numPkgs <= 49:
        rate = 1.5
    elif 50 <= numPkgs:
        rate = 1.25
    return rate, 15 + rate * numPkgs

def displayResults(cusName, qty, shipRate, totMonCharges):

    print('Customer Name:\t\t', cusName)
    print('Number of Packages Shipped this month:\t', qty)
    print('Shipping Rate per Packacge:\t', shipRate)
    print('Total Monthly Charges:\t', totMonCharges)
    return None

main() # calling the function main()




