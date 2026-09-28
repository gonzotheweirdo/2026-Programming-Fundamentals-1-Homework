# ---------------------------------------------
# Name: Thomas Butler
# Date: September 26th, 2026
# Project: Exam 1 Project
# Status: Done I think
# Class: COSC 1336
# ---------------------------------------------
# Description
# This program calculates and summarizes the tenant’s total monthly payment, including any late fees based on the day rent is paid
# The program displays a clear and detailed summary including tenant’s name, Month and year, Payment day, Number of days late, Base rent amount ($1,850.00), Utility fees, Late fees, Total amount due
# All monetary values are formatted with Two decimal places and Comma separators for thousands (e.g., $1,850.00)
# ---------------------------------------------

# Defining the main function which organizes and calls the other functions
def main():

    # Calls function to display the project header
    projectStart()

    # Call function to get input and assign returned list to variable
    userInput = getInput()

    # Call function to calculate fees with user input as param, assign to variable returned list
    outputData = calculateFees(userInput)

    # Call function to diksplay all output
    displayAll(outputData)

    # Calls function to display the project footer
    projectEnd()
     
# This function will display the project footer
def projectStart():
    print('Start of Exam 1 Project ')
    print('Written by: Thomas Butler')
    print('Date: September 26th, 2026\n')
    print(squigglyWrap('A Project to calculate and display rent billing data'))

# Function to get user inputs
def getInput():
    tenantName = input('Please enter your full name:\t')
    month = input('\nPlease enter the month for which you\'re paying:\t')
    year = input('\nPlease enter the year for the month whose rent you\'re paying:\t')
    paymentDay = getDatePaid(month)
    utilities = getUtilityFees(month)
    allInputs = {'name': tenantName, 'billPeriod': month + ' ' + year, 'paymentDay': paymentDay, 'utilityFees': utilities}

    # Return inputs as dictionary
    return allInputs


# This function will print 51-character squiggly borders above and below string parameter
def squigglyWrap(text):
    squiggly = '~ ' * 25 + '~\n'
    wrapped = squiggly + '\t' + text + '\n' + squiggly
    return wrapped

# This function will return a float input from the user
def getFloatData(prompt):
    while (True):
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print('\t\tERROR: That is not a number.')

# Define function to error check date paid and call function to categorize potential lateness
def getDatePaid(month):
    
    while (True):
        try:
            # Development Requirements require input validataion for Payment da to be between 1 and 31
            value = int(input(f'\nPlease enter what day of {month} are you paying as a positive whole number between 1 and 31:\t'))
            if 1 <= value <= 31:
                return value
            else:
                print('\t\tERROR: That is not a positive whole number between 1 and 31.')
        except ValueError:
            print('\t\tERROR: That is not a positive whole number between 1 and 31.')

# Define function to take and validate (as non-negative float) input from user
def getUtilityFees(month):
    while (True):
            try:
                fees = float(input(f'\nPlease enter your total utility fees for {month}?\t$'))
                if 0 <= fees:
                    return fees
                else:
                    print('\t\tERROR: That is negative or not a number.')
            except ValueError:
                print('\t\tERROR: That is negative or not a number.')

# Define function to concatenate date and calculate late fees
def calculateFees(inputData):

    # Calculate and assign potential late fees based on payment day
    if inputData['paymentDay'] < 5:

        # All 3 "late" sub-conditions set daysLate item to paymentDay minus 5 
        inputData['lateFees'] = 0

        # Rent not late so zero late fee
        inputData['daysLate'] = 0

    else:

        # All 3 "late" sub-conditions set daysLate item to paymentDay minus 5 
        inputData['daysLate'] = inputData['paymentDay'] - 5

        # Then lateFees are set based on categories in Requirements
        if inputData['paymentDay'] < 25:
            inputData['lateFees'] = (inputData['paymentDay'] - 5) * 15

        elif inputData['paymentDay'] < 30:
            inputData['lateFees'] = 500

        else:
            inputData['lateFees'] = 1200

    # Assign to totalDue variable the sum of base rent, late fees and utilty fees
    inputData['totalDue'] = sum([1850, inputData['lateFees'], inputData['utilityFees']])
    return inputData
    

# Function to display all data
def displayAll(dataDict):
    print('\n')
    print(squigglyWrap('AllyBaba Rentals - Monthly statement'))
    print(f'Tenant: \t\t{dataDict['name']}\n')
    print(f'Billing Period: \t{dataDict['billPeriod']}\n')
    print(f'Payment Day: \t\t{dataDict['paymentDay']}\n')
    print(f'Days Late: \t\t{dataDict['daysLate']}\n')
    print('\n\nBase Rent: \t\t$1,850.00\n')
    print(f'Utility Fees: \t\t${dataDict['utilityFees']:,.2f}\n')
    print(f'Late Fees: \t\t${dataDict['lateFees']:,.2f}\n')
    print(f'\n\nTOTAL AMOUNT DUE: \t${dataDict['totalDue']:,.2f}\n')

# This function will display the project footer
def projectEnd():
    print(squigglyWrap('\tEnd of Exam 1 Project'))

main() # calling the function main()
