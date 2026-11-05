# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# Name: Thomas Butler
# Date: 08-11-2026
# Project: Project 7
# Status: Production
# Class: COSC 1336 (20)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# Project Objectives
#   
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~


# This function will display the project header
def projectStart():
    print('\nStart of Project 7')
    print('Written by: Thomas Butler')
    print('Date: 08-11-2026')
    print(squigglyWrap('Create Identity'))


# This function will display the project footer
def projectEnd():
    print(squigglyWrap('End of Project 7'))

# This function adds squiggly borders
def squigglyWrap(text):
    squiggly = '~ ' * 25 + '~'
    wrapped = '\n' + squiggly + '\n\t' + text + '\n' + squiggly + '\n'
    
    if text == '':
        return squiggly
    else:
        return wrapped

# This function will return an integer input from the user
def getIntegerData(prompt):
    while (True):
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print('\t\tError Message.  Enter numbers ONLY!')

# This function will return a float input from the user
def getFloatData(prompt):
    while (True):
        try:
            value = float(input(prompt))
            if value < 0:
                print('\t\tERROR:\tPlease enter a number zero or greater.')
            else:
                return value
        except ValueError:
            print('\t\tERROR:\tPlease enter a number zero or greater.')

# This function will return a string input from the user
def getStringData(prompt):
    value = input(prompt)
    return value

# This function will return a string input from the user
def getCharData(prompt):
def getCharData(prompt):

    while (True):
        value = input(prompt)

        value = value.upper()
        if (value in ['W', 'D', 'E']):
            return value

        print('\t\tERROR Message: Wrong selection')

def main(): 
    # Calls function to display project header
    projectStart()

    # Below we start coding

    # Calls function to display the project footer
    projectEnd()

# calling the function main()      
main() 
