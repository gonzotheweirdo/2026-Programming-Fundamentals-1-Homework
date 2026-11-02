# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# Name: Thomas Butler
# Date: 01-11-2026
# Project: Project 6
# Status: Production
# Class: COSC 1336 (20)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
#       Program Objectives
# Display all calorie values in the list
# Display the total number of workout sessions
# Display the sum of all calories burned
# Calculate and display the average calories burned
# Display the maximum calorie value
# Display the minimum calorie value
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

# This function will display the project header
def projectStart():
    print('\nStart of Project 6')
    print('Written by: Thomas Butler')
    print('Date: 01-11-2026')
    print(squigglyWrap('Workout Statistics'))

# This function will display the project footer
def projectEnd():
    print(squigglyWrap('End of Project 6'))

# This function will print 51-character squiggly borders above and below the string parameter or just border if string is empty
def squigglyWrap(text):
    squiggly = '~ ' * 25 + '~'
    wrapped = '\n' + squiggly + '\n\t' + text + '\n' + squiggly + '\n'
    
    if text == '':
        return squiggly
    else:
        return wrapped

# read data
def fileDataToList():
    
    # Open in read mode
    contents = open(fitnessData.txt, "r")

    # Read contents and assign to variable
    dataList = getData(contents)

    # Close the file
    contents.close()

    return dataList

#get data from file and assign to list
def getData(contents):
    
    #initialize list variable
    dataList = []

    #iterate through file 
    for line in contents:

        #call function to validate data
        datum = validateInteger(line)

        #apend valdated data to list 
        dataList.append(datum)

    return dataList

#validate that data in file are positive integers
def validateInteger(datum):
    try:
        value = int(input(datum))
        
        #validate positive
        if value < 0:
            print('\t\tERROR: File contains negative data.')

        return value

    #validate ingeter
    except ValueError:
        print('\t\tERROR: File contains non-integer data.')

#calculate data
def calculateData(dataList):

    #calculate total number of workout sessions
    totalSessions = len(dataList) + 1

    # calculate the sum of all calories burned
    sumBurned = sum(dataList)

    # Calculate the average calories burned
    avgBurned = sum(dataList) / (len(dataList) + 1)

    # calculate the maximum calorie value
    maxCal = max(dataList)

    # calculate the minimum calorie value
    minCal = min(dataList) 

    return dataList, totalSessions, sumBurned, avgBurned, maxCal, minCal

#display calculated data
def displayCalcData(displayList, totalSessions, sumBurned, avgBurned, maxCal, minCal):
    
    # Display all calorie values in the list
    print("Workout Session Data:")
    print(displayList)

    # Display the total number of workout sessions
    print(f"Total Sessions:\t\t{totalSessions}")

    # Display the sum of all calories burned
    print(f"Total Calories Burned:\t{sumBurned}")

    # display the average calories burned
    print(f"Average Calories Burned:\t{avgBurned:.2f}")

    # Display the maximum calorie value
    print(f"Maximum calorie value:\t{maxCal}") 

    # Display the minimum calorie value 
    print(f"Minimum calorie value:\t{minCal}") 

def main(): 
    # Calls function to display the start of project
    projectStart()

    #import data; assign to list variable
    dataList = fileDataToList()

    #calculate data
    displayList, totalSessions, sumBurned, avgBurned, maxCal, minCal = calculateData(dataList)

    #display calculated data
    displayCalcData(displayList, totalSessions, sumBurned, avgBurned, maxCal, minCal)

    # Calls function to display the start of project
    projectEnd()
      
main() # calling the function main()


