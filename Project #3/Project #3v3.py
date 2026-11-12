# ---------------------------------------------
# Name: Thomas Butler
# Date: 01-October-2026
# Project: Project 3
# Status: Production
# Class: COSC 1336 (20)
# ---------------------------------------------
# Program Prompts the user to enter Customer name and Number of packages shipped during the month  
# It Calculates per-package Shipping rate based on package quantity shipped monthly and Total monthly charges  
# Then it Displays a formatted summary showing Customer name number of packages shipped Shipping rate used and Total monthly charges  
# Input validation is included for negative package quantities
# ---------------------------------------------

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

# Define function to display project header
def projectStart():
    print('\nStart of Project 3')
    print('Written by: Thomas Butler')
    print('Date: 01-10-2026')
    print(squigglyWrap('Shipping Fee Calculator'))

# This function will display the end of the project
def projectEnd():
    print(squigglyWrap('End of Project 3'))

# This function will return a positive integer input from the user and throw an error for negative input
def getPositiveInteger(prompt):
    # Error validation
    while(True):
        value = int(input(prompt))
       
        # Throw error for negative input
        if value < 0:
            print('ERROR: Number of packages cannot be negative.')
       
        # Return valid input
        else:
            return value

# This function will return a string input from the user
def getStringData(prompt):
    value = input(prompt)
    return value

# This function will print 51-character squiggly borders above and below the string parameter or just border if string is empty
def squigglyWrap(text):
    squiggly = '\n' + '~ ' * 25 + '~\n'
    wrapped = squiggly + '\t' + text + squiggly
    
    if text == '':
        return squiggly
    else:
        return wrapped

def promptUser():
    name = getStringData('\nPlease enter customer name:\t')
    numPkgs = getPositiveInteger('\nPlease enter number of packages shipped during the month:\t')
    return name, numPkgs

# Define functino to calculate shipping charges by number of packages.
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
    print(squigglyWrap(''))
    print(f'Customer Name:\t\t\t\t {cusName}')
    print('Number of Packages Shipped this month:\t', qty)
    print(f'Shipping Rate per Package:\t\t${shipRate:.2f}')
    print(f'Total Monthly Charges:\t\t\t${totMonCharges:.2f}')
    return None

main() # calling the function main()




