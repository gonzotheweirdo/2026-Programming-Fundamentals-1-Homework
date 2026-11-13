# ---------------------------------------------
# Name: Your Name
# Date: Date of sunmission
# Project: Project 9
# Status: WIP
# Class: COSC 1336
# ---------------------------------------------
# Project Objectives
#   Here you write the project decription
# ---------------------------------------------

# This function will display the start of the project
def projectStart():
    print('Start of Project  9')
    print('Written by: Your Name')
    print('Date: Enter date ')
    print('-' * 50 )
    print('\tHere your write project information')
    print('-' * 50 + '\n')

# This function will display the start of the project
def projectEnd():
    print('-' * 50)
    print('End of Project 9')

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
            return value
        except ValueError:
            print('\t\tError Message.  Enter numbers ONLY!')

# This function will return a string input from the user
def getStringData(prompt):
    value = input(prompt)
    return value

# This function will return a string input from the user
def getCharData(prompt):

    while (True):
        value = input(prompt)

        value = value.upper()
        if (value in ['W', 'D', 'E']):
            return value

        print('\t\tERROR Message: Wrong selection')

#       1. Constructor
# Accepts yearInstalled and brand as arguments
# Initializes the attributes with the given values
# Sets currentTemp to 72°F
#       2. Accessor Methods
# getYearInstalled() → returns installation year
# getBrand() → returns brand name
# getCurrentTemp() → returns current temperature
#       3. Setter Method
# setTemperature() → allows updating temperature
# Temperature must stay within a safe range:
# Minimum: 60°F
# Maximum: 85°F
#       4. increaseTemp() Method
# Increases temperature by 2°F each time it is called
#       5. decreaseTemp() Method
# Decreases temperature by 2°F each time it is called
# Temperature cannot go below 60°F

def main(): 
    # Calls function to display the start of project
    projectStart()

    # Below we start coding

    # Calls function to display the start of project
    projectEnd()
      
main() # calling the function main()


