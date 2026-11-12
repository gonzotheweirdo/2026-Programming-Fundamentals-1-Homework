# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# Name: Thomas Butler
# Date: 08-11-2026
# Project: Project 7
# Status: Production
# Class: COSC 1336 (20)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
#       Project Objectives
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# Program will ask the user to enter the employee’s first name, last name, Social Security Number (SSN), number of emergency contacts, hourly wage, and employee badge ID.
# The program will then generate and display the following information:
#       1. Employee initials
# First letter of the first name + first letter of the last name
#       2. Employee email address in the format:
# <first initial><lastname>@cityhospital.com
#       Example:
# Maria Lopez → mlopez@cityhospital.com
#       3. The last 4 digits of the employee’s SSN
#       4. Hourly wage formatted with:
# A dollar sign ($)
# Two decimal places
#       5. Validation that the number of emergency contacts is between 0 and 5 inclusive
#       6. Employee badge username using:
# Last name
# A period (.)
# Last 4 digits of SSN
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
            if 0 <= value <=5:
                return value
            else:
                print('\t\tERROR:\tNumber must be between 0 and 5 inclusive.')
        except ValueError:
            print('\t\tError Message.  Enter numbers ONLYprint(f'')]\t{}')

# This function will return a float input from the user
def getFloatData(prompt):
    while (True):
        try:
            value = float(input(prompt))
            if value <= 0:
                print('\t\tERROR:\tPlease enter a number greater than zero.')
            else:
                return value
        except ValueError:
            print('\t\tERROR:\tPlease enter a number greater than zero.')

# This function will return a string input from the user
def getStringData(prompt):
    value = input(prompt)
    while(True):
        if value != '':
            return value
        else:
            print('ERROR:\tThis item cannot be left empty')

#prompt user for all the data
def promptUser():
    fName = getStringData('Please enter employee first name:\t\t')
    lName = getStringData('Please enter employee last name:\t\t')
    uselessBoolean, ssn, lastFour = validateSSN('Please enter employee social security number:\t')
    eContacts = getIntegerData('Please enter number of Emergency Contacts (0-5):\t')
    hourWage = getFloatData('Please enter the employee\'s hourly wage:\t$')
    badgeId = getStringData('Please enter employee badge ID:\t')
    return fName, lName, uselessBoolean, ssn, lastFour, eContacts, hourWage

#process data to make initials
def makeInitial(name):
    splitName = list(name)
    return splitName[0]

#process data to make email
def makeEmail(fName, lName, hospDomain):
    email = makeInitial(fName) + lName + '@' + hospDomain + '.com'
    return email

#process data to make badge ID
def makeUsername(lName, lastFour):
    username = lName + '.' + str(lastFour)
    return username

# Function displays all results
def displayResult(initials, email, lastFour, hourWage, eContacts, username, uselessBoolean):
    print(squigglyWrap('Employee Registration Summary'))
    print(f'Employee Initials:\t{initials}')
    print(f'Employee Email:\t\t{email}')
    print(f'Last 4 Digits of SSN:\t{lastFour}')
    print(f'Hourly Wage:\t\t${hourWage:.2f}')
    print(f'Emergency Contacts:\t{eContacts}')
    print(f'Badge Username:\t\t{username}')
    print(f'SSN Validation Returns:\t{uselessBoolean}')

# Function valdates SSN
def validateSSN(prompt):
    while (True):
        ssn = input(prompt)
        ssnList = list(ssn)
        if len(ssnList) == 11:
            if ssnList[3] == '-' and ssnList[6] == '-':
                ssnList.pop(2)
                ssnList.pop(5)
                for each in ssnList:
                    try:
                        num = int(each)
                    except ValueError: break
                lastFour = [ssnList[5], ssnList[6], ssnList[7], ssnList[8]]
                noGap = "".join(lastFour)
                return True, ssn, noGap
        else:
            print('\t\tERROR:\tPlease enter numbers ONLY in the format xxx-xx-xxxx')

def main(): 
    #store hospital name as constant
    hospDomain = "brokenridge"
    
    # Calls function to display project header
    projectStart()

    # prompt user for first name, last name, SSN, number of emergency contacts, hourly wage, badge ID.
    fName, lName, uselessBoolean, ssn, lastFour, eContacts, hourWage = promptUser() # not badgeId

    #store initials
    initials = makeInitial(fName) + makeInitial(lName)

    #process data to make email
    email = makeEmail(fName, lName, hospDomain)

    #process data to make badge username
    username = makeUsername(lName, lastFour)

    #display all employee info
    displayResult(initials, email, lastFour, hourWage, eContacts, username, uselessBoolean)

    # Calls function to display the project footer
    projectEnd()

# calling the function main()      
main() 
