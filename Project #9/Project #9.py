# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# Name: Thomas Butler
# Date: 19-11-2026
# Project: Project 9
# Status: Production
# Class: COSC 1336 (20)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
#       Project Objectives
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
#
#
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


# Defining Thermostat class
class Thermostat:
    
    # Constructor function
    def constructor(yearInstalled, brand):

# Initializes the attributes with the given values
        __init__
# Sets currentTemp to 72°F

    # Accessor Methods
    def getYearInstalled()
        #integer between 2015 and 2026 

        # returns installation year
    
    def getBrand()
        # returns brand name
    
    def getCurrentTemp()
        # returns current temperature

    # Setter Method
    def setTemperature()
    
        # allows updating temperature

        # Temperature must stay within a safe range:
        # Minimum: 60°F
        # Maximum: 85°F

    # Method to increase temp
    def increaseTemp():
    
        # Increases temperature by 2°F each time it is called

    # Method to decrease temp
    def decreaseTemp():
    
        # Decreases temperature by 2°F each time it is called
        # Temperature cannot go below 60°F

def main(): 
    # Calls function to display the start of project
    projectStart()

    # 

    # Calls function to display the end of project
    projectEnd()

# calling the function main()
main()
