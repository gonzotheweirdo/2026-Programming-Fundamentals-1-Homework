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
def readData():

    # iterate through each line from the workout data file 
    with open("fitnessData.txt", "r") as fileContents:

        #split the stjring by line and assign to list variable
        dataList = fileContents.read().splitlines()

    return dataList

#validate that data in file are positive integers
def validateIntegers(dataList):
   
    #initialize list variable empty
    displayList = []

    #iterate through list
    for line in dataList:
        try:
            #convert string to integer
            value = int(line)

            #validate positive
            if value < 0:
                print('\t\tERROR: File contains negative data.')
            else:
                displayList.append(value)

        #validate integer
        except ValueError:
            print('\t\tERROR: File contains non-integer data.')

    return displayList

#calculate data
def calculateData(dataList):

    #calculate total number of workout sessions
    totalSessions = len(dataList)

    # calculate the sum of all calories burned
    sumBurned = sum(dataList)

    # Calculate the average calories burned
    avgBurned = sumBurned / totalSessions if totalSessions else 0.0

    # calculate the maximum calorie value
    maxCal = max(dataList) if dataList else 0

    # calculate the minimum calorie value
    minCal = min(dataList) if dataList else 0

    return dataList, totalSessions, sumBurned, avgBurned, maxCal, minCal

#display calculated data
def displayCalcData(displayList, totalSessions, sumBurned, avgBurned, maxCal, minCal):
    
    # Display all calorie values in the list
    print("\tWorkout Number\t\tCalories Burned")
    count = 1
    for item in displayList:
        print(f"\t\t{count}\t\t{item}")
        count += 1

    # Display the total number of workout sessions
    print(f"\nTotal Sessions:\t\t\t{totalSessions}")

    # Display the sum of all calories burned
    print(f"Total Calories Burned:\t\t{sumBurned}")

    # display the average calories burned
    print(f"Average Calories Burned:\t{avgBurned:.2f}")

    # Display the maximum calorie value
    print(f"Maximum calorie value:\t\t{maxCal}") 

    # Display the minimum calorie value 
    print(f"Minimum calorie value:\t\t{minCal}") 

def main(): 
    # Calls function to display the start of project
    projectStart()

    #import data; assign to list variable
    dataList = readData()

    #validate Integers
    displayList = validateIntegers(dataList)

    #calculate data
    displayList, totalSessions, sumBurned, avgBurned, maxCal, minCal = calculateData(displayList)

    #display calculated data
    displayCalcData(displayList, totalSessions, sumBurned, avgBurned, maxCal, minCal)

    # Calls function to display the start of project
    projectEnd()
      
main() # calling the function main()


