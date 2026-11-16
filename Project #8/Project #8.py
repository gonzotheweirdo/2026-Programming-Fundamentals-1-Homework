# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# Name: Thomas Butler
# Date: 15-11-2026
# Project: Project 8
# Status: Production
# Class: COSC 1336 (20)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
#       Project Objectives
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# Program creates and manages a product inventory database for a grocery store using a dictionary.
# The dictionary will use the product code as the key and the product name as the value.
# 
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

# This function will display the project header
def projectStart():
    print('\nStart of Project 8')
    print('Written by: Thomas Butler')
    print('Date: 15-11-2026')
    print(squigglyWrap('Inventory Database'))

# This function will display the project footer
def projectEnd():
    print(squigglyWrap('End of Project 8'))

# This function adds squiggly borders
def squigglyWrap(text):
    squiggly = '~ ' * 25 + '~'
    wrapped = '\n' + squiggly + '\n\t' + text + '\n' + squiggly + '\n'
    if text == '':
        return squiggly
    else:
        return wrapped

# This function will return a string input from the user, validated to be non-empty and converted to uppercase
def getStringData(prompt):
    while(True):
        value = input(prompt)
        if value != '':
            return value.upper()
        else:
            print('\tERROR:\tThis cannot be left empty\n')

def readData():
    # Opens and reads the file
    file = open("inventoryData.txt")
    data = file.read()

    # Parses each line
    lines = data.split('\n')
    file.close()

    # Populates the dictionary
    inventory = {}
    for line in lines:
        if line == '':
            break
        splitLine = line.split(',')
        code = splitLine[0]
        name = splitLine[1]
        inventory.update({code: name})

    # Returns the completed dictionary
    return inventory

def displayResult(productCode, productName):
    # Accepts the product code and corresponding product name (or error message). Displays the result in a formatted manner.
    print(squigglyWrap(f'\nProduct Code:\t{productCode}\nProduct Name:\t{productName}\n'))

def validateContinue():
    # Prompt user to continue or exit
    userChoice = getStringData('Would you like to search for another product? (Y/N):\t')

    #loop until Y or N
    while(True):

        # validate user input as 'Y' or 'N'
        if userChoice in ['N', 'Y']:
            return userChoice
    
        else:
           userChoice = getStringData('\tERROR:\tPlease enter Y or N:\t')

def main(): 
    
    # Calls function to display the start of project
    projectStart()

    # Populate dictionary with contents of inventoryData.txt
    inventory = readData()

    # Loop defaults to continue until user decides to exit
    continueLoop = 'Y'

    while continueLoop == 'Y':
        # Prompt user for product code
        productCode = getStringData('Please enter a product code:\t')
        productName = inventory.get(productCode, 'Product Not Found.')

        # Display the result
        displayResult(productCode, productName)
        continueLoop = validateContinue()

    # Calls function to display the start of project
    projectEnd()
      
main() # calling the function main()
