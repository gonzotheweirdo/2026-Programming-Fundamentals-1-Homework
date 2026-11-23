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
    print('\nStart of Project 9')
    print('Written by: Thomas Butler')
    print('Date: 22-11-2026')
    print(squigglyWrap('Thermostat'))

# This function will display the project footer
def projectEnd():
    print(squigglyWrap('End of Project 9'))

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
            print('\n\tERROR:\tThis cannot be left empty\n')

# This function will return an integer input from the user
def getIntegerData(prompt):
    while (True):
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print('\n\tError Message.  Enter numbers ONLY!\n')

# Defining Thermostat class
class Thermostat(object):
    
    # Constructor function
    def __init__(self, brand, yearInstalled, temp):
        
        # Initializes the attributes with the given values
        self.yearInstalled = yearInstalled
        self.brand = brand

        # Sets currentTemp to 72°F
        self.currentTemp = 72
        self.currentTemp = temp

    # Accessor Methods
    def getYearInstalled(self):
        #return year installed
        return self.yearInstalled
    
    def getBrand(self):
        # returns brand name
        return self.brand
    
    def getCurrentTemp(self):
        # returns current temperature
        return self.currentTemp

    # Setter Method
    def setTemperature(self, tempInput):
        
        # allows updating temperature. Temperature must stay within a safe range:
        if tempInput < 60:
            print("[MIN LIMIT REACHED]")
            self.currentTemp = 60
        
        elif tempInput > 85:
            print("[MAX LIMIT REACHED]")
            self.currentTemp = 85

        #if tempInput is in range, set as current temp
        else:
            self.currentTemp = tempInput

    # Method to increase temp
    def increaseTemp(self):
        
        # Increases temperature by 2°F each time it is called
        self.currentTemp += 2
        if self.currentTemp > 85:
            print("\t\t[MAX LIMIT REACHED]")
            self.currentTemp = 85

    # Method to decrease temp
    def decreaseTemp(self):
    
        # Decreases temperature by 2°F each time it is called
        self.currentTemp -= 2
        if self.currentTemp < 60:
            print("\t\t[MIN LIMIT REACHED]")
            self.currentTemp = 60

    # return string version of currentTemp
    def __str__(self, currentTemp):
        stringTemp = str(currentTemp) + "°F"
        return stringTemp


# prompt user for brand
def brandPrompt():
    validBrands = ["HONEYWELL", "NEST", "ECOBEE", "GOOGLE"]
    while(True):
        brand = getStringData("Please enter the thermostat Brand and press \"Enter\"(Nest, Ecobee, Honeywell, Google):\t")
        if brand.upper() in validBrands:
            return brand
        else:
            print("\n\tERROR:\tPlease enter Nest, Honeywell, Ecobee, Google.\t")

# prompt user for year
def yearPrompt():
    while(True):
        yearInstalled = getIntegerData("Please enter the thermostat's year (2015 - 2026):\t")
        
        #integer between 2015 and 2026 
        if yearInstalled >= 2015 and yearInstalled <= 2026:

            # returns installation year
            return yearInstalled

        #else throw error
        else:
            print("\n\tERROR:\tYear must be 2015 - 2026\n")

# prompt user for starting temp
def tempPrompt():
    while(True):
        startingTemp = getIntegerData("Please enter a starting temperature (60-85):\t")
        if startingTemp >= 60 and startingTemp <= 85:
            return startingTemp
        else:
            print("\n\tERROR: Starting temperature must be between 60 and 85!\n")

#prompt the user how many times to increase temp
def qtyIncrease():
    while(True):
        qty = getIntegerData("How many times to increase temperature?\t")
        if qty >= 0:
            return qty
        else:
            print("\tERROR: Number of times cannot be negative.\n")

#prompt the user how many times to decrease temp
def qtyDecrease():
    while(True):
        qty = getIntegerData("How many times to decrease temperature?\t")
        if qty >= 0:
            return qty
        else:
            print("\tERROR: Number of times cannot be negative.\n")

def main(): 
    # Calls function to display the start of project
    projectStart()

    # prompt for brand
    brand = brandPrompt()

    #prompt for year
    year = yearPrompt()

    #prompt for starting Temp
    temp = tempPrompt()

    thermoKing = Thermostat(brand, year, temp)

    thermoKing.setTemperature(temp)
    
    qtyUp = qtyIncrease()
    qtyDown = qtyDecrease()

    i = 1
    while i <= qtyUp:
        thermoKing.increaseTemp()
        tempToPrint = thermoKing.getCurrentTemp()
        print(f"Increase #{i}: +2°F\tCurrent Temp: {tempToPrint}°F")
        i += 1

    i = 1
    while i <= qtyDown:
        thermoKing.decreaseTemp()
        tempToPrint = thermoKing.getCurrentTemp()
        print(f"Decrease #{i}: -2°F\tCurrent Temp: {tempToPrint}°F")
        i += 1

    # Calls function to display the end of project
    projectEnd()

# calling the function main()
main()
