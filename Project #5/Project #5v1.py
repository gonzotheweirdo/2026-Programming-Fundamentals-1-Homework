# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# Name: Thomas Butler
# Date: 25-10-2026
# Project: Project 5
# Status: Production
# Class: COSC 1336(20)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# Prompt the user to enter the speed (in mph) of the delivery van.
# Prompt the user to enter the time (in hours) the van traveled.
# Reject with an error message any non-integer input, any speed input greater than 100 mph and any time input greater than 10 hours.
# Calculate the distance traveled for each hour of the trip and display the results in a formatted table.
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

# This function will display the project header
def projectStart():
    print('\nStart of Project 5')
    print('Written by: Thomas Butler')
    print('Date: 25-10-2026')
    print(squigglyWrap('Delivery Van Distance Calculator'))

# This function will display the project footer
def projectEnd():
    print(squigglyWrap('End of Project 5'))

# This function will print 51-character squiggly borders above and below the string parameter or just border if string is empty
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
            print('\t\tERROR: Please enter whole numbers only.')


# Get user input for speed and hours
def getSpeedAndHours():
    while True:
        speed = getIntegerData('Please enter the speed (in miles per hour) of the delivery van:\t')
        if 1 > speed or speed > 100:
            print('\t\tERROR: Speed must be between 1 and 100 miles per hour.')
        else:
            break

    while True:
        hours = getIntegerData('Please enter the time (in hours) the van traveled:\t')
        if 1 > hours or hours > 10:
            print('\t\tERROR: Time must be between 1 and 10 hours.')
        else:
            break
    return speed, hours

# Display the results
def displayResults(speed, hours):
    print(f'\nHours\t\tDistance Traveled')
    print(squigglyWrap(''))
    for hour in range(1, hours + 1):
        distance = speed * hour
        print(f'{hour}\t\t{distance}')
    return None

# Main function to run the program
def main(): 
    # Calls function to display the start of project
    projectStart()

    # Prompt the user to enter the speed (in mph) of the delivery van and the time (in hours) the van traveled. assign the returned values to variables speed and hours
    speed, hours = getSpeedAndHours()

    # Display results table
    displayResults(speed, hours)

    # Calls function to display the end of project
    projectEnd()

# Call the function main()
main() 
