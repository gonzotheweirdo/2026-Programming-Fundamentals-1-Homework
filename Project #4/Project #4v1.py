# ---------------------------------------------
# 
# Name:     Thomas Butler
# ACCeID:   t1095073
# Date:     16-October-2026
# Project:  Project 4
# Status:   Production
# Class:    COSC 1336 - 020
# 
# ---------------------------------------------
# 
# Project Objectives:
#   0   Prompt the user to enter a positive integer representing the maximum
#   1   The program should validate the input using a loop to ensure the user enters a value greater than 
#   2   Once a valid number is entered, the program should display all odd-numbered milestones from 1 up to and including the entered number, along with the total sum of those odd numbers.
# 
# ---------------------------------------------

# Function to display project header
def projectStart():
    print('\nStart of Project 4')
    print('Written by: Thomas Butler')
    print('Date: 09-10-2026')
    print(squigglyWrap('Odd-Numbered Milestone Calculator'))

# This function will display the project footer
def projectEnd():
    print(squigglyWrap('End of Project 4'))

# This function will print 51-character squiggly borders above and below the string parameter or just border if string is empty
def squigglyWrap(text):
    squiggly = '\n' + '~ ' * 25 + '~\n'
    wrapped = squiggly + '\t' + text + squiggly
    
    if text == '':
        return squiggly
    else:
        return wrapped

# This function will return an integer input from the user
def getPosInt(prompt):
    while (True):
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print('\t\tError Message.  Please enter positive whole numbers ONLY!')
        except ValueError:
            print('\t\tError Message.  Please enter positive whole numbers ONLY!')

# This function will return a float input from the user
def getFloatData(prompt):
    while (True):
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print('\t\tError Message.  Please enter numbers ONLY!')


# Define function to calculate odd-numbered milestones and sum thereof
def calcMileSum(userInput):

    # Initialize empty list
    odds = []

    # List numbers 0 to userInput
    for x in range (userInput + 1):
        if x % 2 != 0:
            odds.append(x)

    # Sum the Odds and assign to second return variable
    oddSum = sum(odds)

    # Return Variables
    return odds, oddSum
    
# Define function to display list of milestones and their sum
def displayAll(stoneList, oddSum):

    print('\nOdd-numbered milestones:')
    print(*stoneList)
    print(f'\nThe sum of these milestones is\t\t\t{oddSum}')
    
    # return
    return None

# Calling function main
def main(): 
    
    # Calls function to display project header
    projectStart()

    # Below we start coding
    posInt = getPosInt('Please enter the farthest milestone walked:\t')

    # Calculate Odd-Numbered Milestones and sum thereof. Assign to variables
    milestones, sumOf = calcMileSum(posInt)

    # Display list of milestones and their sum
    displayAll(milestones, sumOf)

    # Calls function to display project footer
    projectEnd()
      
main() # calling the function main()
