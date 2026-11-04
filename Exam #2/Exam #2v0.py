# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# Name: Thomas Butler
# Date: 03-11-2026
# Project: EXAM 2
# Status: Production
# Class: COSC 1336 (20)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
# Project Objectives
#   1. Prompt the user to enter an initial account balance.
#   2. Allow the user to enter a series of transactions, one at a time.
#   3. Each transaction must include a transaction type, followed by a transaction amount (if applicable).
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
#• Invalid transaction types (not W, D, or E) should:
# Show an informative error message
# Ignore the transaction and prompt again
# Transaction amounts must be positive numbers greater than zero
# If not, show an error and prompt again
# Overdraft withdrawals are not allowed; display a message if attempted
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

# This function will display the project header
def projectStart():
    print('\nStart of Exam 2')
    print('Written by: Thomas Butler')
    #print('Date: 03-11-2026')
    print(squigglyWrap('Ally Baba Financial Institution'))
    
    # Import date class from datetime module
    from datetime import date

    # Returns current local date
    today = date.today()
    print("Date: ", today)

    print("Account Number: 666")

# This function will display the project footer
def projectEnd():
    print(squigglyWrap('End of Exam 2'))

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

    while (True):
        value = input(prompt)
        transTypes = {'W':'Withdrawal', 'D':'Deposit', 'E':'Exit'}
        value = value.upper()
        if (value in transTypes):
            return transTypes[value]

        print('\t\tERROR Message: Wrong selection')

#prompt user for initial balance
def getFirstBalance():
    return getFloatData('Please enter initial account balance:\t$')

#Prompt for transaction type
def getTransType():
    print(squigglyWrap('Transaction Menu'))
    print('W\tWithdrawal\nD\tDeposit\nE\tExit')
    transType = getCharData('\nPlease enter transaction type (W, D, or E):\t')
    return transType

#prompt for transaction amount
def getTransAmount(transType):
    balanceChange = getFloatData(f'Please enter {transType} amount:\t$')
    print(f'\t\t[Processing {transType} of ${balanceChange:.2f}...]')
    
    #if the transaction type is a withdrawal make balance change negative
    if transType == 'Withdrawal':
        balanceChange = -balanceChange

    return balanceChange

#Update balance and service charges
def processTransaction(transType, balance, balanceChange, serviceCharges):

    transCharge = 0

    #validate for sufficient funds
    if balance + balanceChange < 0:
        transCharge += 40

    #update balance
    else:
        balance += balanceChange

    #transaction charge for withdrawals
    if transType == 'Withdrawal':
        transCharge += 0.25

    #update service charges total
    serviceCharges += transCharge

    return balance, balanceChange, serviceCharges, transCharge

#display transaction summary
def transactionSummary(transType, balance,  balanceChange, transCharge, serviceCharges):

    #in the case of overdraft
    if balance + balanceChange < 0:
        print(f'\n\tOverdraft: Insufficient funds. Overdraft Fee of $40.00 applied. transaction declined.\n')

    #in the case of a valid transaction
    else:
        print(f'\n\t\t[Processed {transType} of ${abs(balanceChange):.2f}]')

    #display current balance
    print(f'Current Balance:\t\t${balance:.2f}')

    #for withdrawals, display the transaction charge
    if transType == 'Withdrawal':
        print(f'Service Charge:\t\t\t${transCharge:.2f}')

    #display accrued service charges    
    print(f'Acrued Service Charges:\t\t${serviceCharges:.2f}')

#Display results at the end
def sessionSummary(balance, serviceCharges):
    print(squigglyWrap('Session Summary'))
    print(f'Current Balance:\t\t${balance:.2f}')
    print(f'Total Service Charges:\t\t${serviceCharges:.2f}\n')
    print(f'Final Balance:\t\t\t${balance - serviceCharges:.2f}')
    return None

def main(): 
    # Calls function to display the start of project
    projectStart()

    balance = getFirstBalance()
    serviceCharges = 0

    #begin loop until user selects "Exit"
    while True:
        
        #Prompt for and validate transaction type
        transType = getTransType()

        #sentry for while loop to continue until user selects "Exit"
        if transType == 'Exit':
            #exit option
            print('\tExiting...')
            break

        else:

            balanceChange = getTransAmount(transType)
        
            #Update balance and service charges
            balance, balanceChange, serviceCharges, transCharge = processTransaction(transType, balance, balanceChange, serviceCharges)

            #display transaction summary
            transactionSummary(transType, balance, balanceChange, transCharge, serviceCharges)

    #Display results at the end
    sessionSummary(balance, serviceCharges)

    # Calls function to display project footer
    projectEnd()

# call the function main()
main() 
