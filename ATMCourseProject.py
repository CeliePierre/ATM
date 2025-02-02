## **************************************************
##
## Program: ATM Project
## Language: Python 3.7.2
##
## Description: ATM Project for Intro to Computer Programming I
##
## College: Husson University
## Course: IT 261 I7-1
## Author: Célie Pierre
##
## Change Log:
## Date         Description
## ------------------------------
## 2019/02/06   Initial draft, added Variables & Login Interface
## 2019/02/17   Updated variables
## 2019/02/23   Added functions, global variables
##              Added Main Menu and Account Menu
##              Added deposit logic
## 2019/02/27   Added receipt logic
##              Added balance file import/export
##              Corrected login error
## 2019/03/02   Cleaned up comments
##              Added withdraw logic
##              Simplified deposit logic
##              Tested for errors
##              Added exception handling
## 2019/03/06   Error testing
##              Code cleanup
##
## **************************************************

# Variable Declaration
menuChoice = 0        # User selection of main menu
accountChoice = 0     # User selection of account menu
userWithdraw = 0      # User input of withdraw amount
userDeposit = 0.0     # User input of deposit amount
# Current balances of...
checkBal = 500.0      # Checking Account
save1Bal = 1500.0     # Savings Account 1
save2Bal = 5000.0     # Savings Account 2
# Starting balances of...
startCheck = 0.0      # Checking Account
startSave1 = 0.0      # Savings Account 1
startSave2 = 0.0      # Savings Account 2
# Ending balances of...
endCheck = 0.0        # Checking Account
endSave1 = 0.0        # Savings Account 1
endSave2 = 0.0        # Savings Account 2
# Total deposits made to...
depositCheck = 0.0    # Checking Account
depositSave1 = 0.0    # Savings Account 1
depositSave2 = 0.0    # Savings Account 2
depositAll = 0.0      # All accounts
# Total withdrawals made from...
withdrawCheck = 0.0   # Checking Account
withdrawSave1 = 0.0   # Savings Account 1
withdrawSave2 = 0.0   # Savings Account 2
withdrawAll = 0.0     # All accounts
# Business rules
withdrawRule1 = 300   # Single account withdraw limit
withdrawRuleAll = 750 # Total account withdraw limit
depositMin = 0        # Minimum deposit limit
depositMax = 1000     # Maximum deposit limit
# Main Menu - Global Variables
BALANCE = 1           # Fund balance inquiry
DEPOSIT = 2           # Deposit funds
WITHDRAW = 3          # Withdraw funds
COMPLETE = 4          # Exit
# Account Menu - Global Variables
CHECK = 1             # Checking account
SAVE1 = 2             # Savings Account 1
SAVE2 = 3             # Savings Account 2

def main():
    # Import menu options
    global BALANCE
    global DEPOSIT
    global WITHDRAW
    global COMPLETE
    # Import current balance
    importBal()
    global checkBal
    global save1Bal
    global save2Bal
    global startCheck
    global startSave1
    global startSave2
    # Initialize starting balance
    startCheck = checkBal
    startSave1 = save1Bal
    startSave2 = save2Bal

    welcome()

    if login(): # User login
        menuChoice = 0 # Menu loop
        while menuChoice != COMPLETE:
            menuChoice = mainMenu()
            if menuChoice == BALANCE:
                accountChoice = accountMenu()
                if accountChoice != 0:
                    balance(accountChoice)
            elif menuChoice == DEPOSIT:
                accountChoice = accountMenu()
                if accountChoice != 0:
                    deposit(accountChoice)
            elif menuChoice == WITHDRAW:
                accountChoice = accountMenu()
                if accountChoice != 0:
                    withdraw(accountChoice)
        else:
            complete()
            # If this else is indented once more, the menu will work unless
            # an invalid selection is made, then it will display the receipt.
            # Keeping the else indented here catches that error.

    else: # Login failure
        print('\nLogin failed.')
        print('Goodbye.')

def welcome(): # Welcome Message
    print("Welcome to the Pierre Bank ATM!\n")

def login():
    # Login (local) variables
    accountNum = 123456  # User’s account number
    pin = 9999           # User’s Personal Identification Number (PIN)
    userAccount = 0      # User input of account number
    userPIN = 0          # User input of PIN

    try: # User login interface
        userAccount = int(input("Please enter your Account Number: "))
        userPIN = int(input("Please enter your PIN: "))
        if userAccount == accountNum and userPIN == pin:
            print("Login Successful.")
            return True
        else:
            return False
    except:
        return False

def mainMenu():
    print('\n   MAIN MENU')
    print('1) Fund Balance Inquiry')
    print('2) Deposit')
    print('3) Withdraw')
    print('4) Exit')
    
    try:
        menuChoice = int(input('\nPlease make a menu selection: '))
        if menuChoice == 1 or menuChoice == 2 or \
           menuChoice == 3 or menuChoice == 4:
            return menuChoice
        else: 
            print('ERROR: Invalid Selection.')
            print('Please select from the menu numbers provided.')
            menuChoice = 0
            return menuChoice
    except:
        print('ERROR: Invalid Selection.')
        print('Please select from the menu numbers provided.')
        menuChoice = 0
        return menuChoice

def accountMenu():
    print('\n   ACCOUNT MENU')
    print('1) Checking Account')
    print('2) Savings Account 1')
    print('3) Savings Account 2')
    
    try:
        menuChoice = int(input('\nSelect an account: '))
        if menuChoice == 1 or menuChoice == 2 or menuChoice == 3:
            return menuChoice
        else:
            print('ERROR: Invalid Selection.')
            print('You must select from the menu numbers provided.')
            print('Returning to the Main Menu.')
            menuChoice = 0
            return menuChoice
    except:
        print('ERROR: Invalid Selection.')
        print('You must select from the menu numbers provided.')
        print('Returning to the Main Menu.')
        menuChoice = 0
        return menuChoice

def balance(accountChoice):
    global checkBal
    global save1Bal
    global save2Bal
    
    if accountChoice == 1:
        print('Checking Account Balance: $', format(checkBal, '.2f'), sep='')
    if accountChoice == 2:
        print('Savings Account 1 Balance: $', format(save1Bal, '.2f'), sep='')
    if accountChoice == 3:
        print('Savings Account 2 Balance: $', format(save2Bal, '.2f'), sep='')

def deposit(accountChoice):
    global checkBal
    global save1Bal
    global save2Bal
    global depositCheck
    global depositSave1
    global depositSave2
    global depositAll

    try:
        userDeposit = validDeposit()
        if accountChoice == 1: # Checking Account Deposit
            checkBal += float(userDeposit)
            depositCheck += float(userDeposit)
            depositAll += float(userDeposit)
            print('Deposit accepted. Balance updated.')
            print('Thank you for your deposit.')
        elif accountChoice == 2: # Savings Account 1 Deposit
            save1Bal += float(userDeposit)
            depositSave1 += float(userDeposit)
            depositAll += float(userDeposit)
            print('Deposit accepted. Balance updated.')
            print('Thank you for your deposit.')
        elif accountChoice == 3: # Savings Account 2 Deposit
            save2Bal += float(userDeposit)
            depositSave2 += float(userDeposit)
            depositAll += float(userDeposit)
            print('Deposit accepted. Balance updated.')
            print('Thank you for your deposit.')
    except:
        userDeposit = 0.0

def validDeposit():
    global depositMin
    global depositMax

    try: # Deposit Validation
        userDeposit = float(input('Enter deposit amount: '))
        if userDeposit > depositMin and userDeposit <= depositMax:
            return userDeposit
        else:
            print('ERROR: Deposit must be between ', \
                  depositMin, ' - ', depositMax, '.', sep='')
            print('No deposit has been made.')
    except:
        print('ERROR: Deposit must be a number between ', \
              depositMin, ' - ', depositMax, '.', sep='')
        print('No deposit has been made.')

def withdraw(accountChoice):
    global checkBal
    global save1Bal
    global save2Bal
    global withdrawCheck
    global withdrawSave1
    global withdrawSave2
    global withdrawAll

    try:
        userWithdraw = validUserWithdraw()
        if validWithdraw(accountChoice, userWithdraw):
            if accountChoice == 1: # Checking Account Withdraw
                checkBal -= float(userWithdraw)
                withdrawCheck += float(userWithdraw)
                withdrawAll += float(userWithdraw)
                print('Withdraw accepted. Balance updated.')
                print('Thank you for your deposit.')
            elif accountChoice == 2: # Savings Account 1 Withdraw
                save1Bal -= float(userWithdraw)
                withdrawSave1 += float(userWithdraw)
                withdrawAll += float(userWithdraw)
                print('Withdraw accepted. Balance updated.')
                print('Thank you for your deposit.')
            elif accountChoice == 3: # Savings Account 2 Withdraw
                save2Bal -= float(userWithdraw)
                withdrawSave2 += float(userWithdraw)
                withdrawAll += float(userWithdraw)
                print('Withdraw accepted. Balance updated.')
                print('Thank you for your deposit.')
    except:
        userWithdraw = 0.0


def validUserWithdraw(): # Withdraw user input validation
    try:
        userWithdraw = float(input('\nEnter withdraw amount '\
                                   '(20, 40, 60, 80, 100): '))
        if userWithdraw == 20 or userWithdraw == 40 or userWithdraw == 60 or \
           userWithdraw == 80 or userWithdraw == 100:
            return userWithdraw
        else:
            print('\nERROR: Invalid Selection. ' \
                  'Enter only 20, 40, 60, 80, or 100.')
            print('No withdrawal has been made.')
    except:
        print('\nERROR: Invalid Selection. ' \
              'Enter only numbers 20, 40, 60, 80, or 100.')
        print('No withdrawal has been made.')

def validWithdraw(accountChoice, userWithdraw): # Withdraw account validation
    global checkBal
    global save1Bal
    global save2Bal
    global withdrawCheck
    global withdrawSave1
    global withdrawSave2
    global withdrawAll

    # Initiate local variables for testing
    if accountChoice == 1: # Checking Account
        accountBal = checkBal
        withdrawAccount = withdrawCheck + userWithdraw
    elif accountChoice == 2: # Checking Account
        accountBal = save1Bal
        withdrawAccount = withdrawSave1 + userWithdraw
    elif accountChoice == 3: # Checking Account
        accountBal = save2Bal
        withdrawAccount = withdrawSave2 + userWithdraw
    withdrawAllTest = withdrawAll + userWithdraw

    if userWithdraw <= accountBal: # Validate: Available funds
        if withdrawAccount > withdrawRule1: # Validate: Single account limit
            print('ERROR: Cannot exceed single account withdraw limit.')
            print('Single account withdraw limit: $', withdrawRule1, sep='')
            print('No withdraw has been made.')
            return False
        elif withdrawAllTest > withdrawRuleAll: # Validate: Total account limit
            print('ERROR: Cannot exceed total account withdraw limit.')
            print('Total accounts withdraw limit: $', withdrawRuleAll, sep='')
            print('No withdraw has been made.')
            return False
        else:
            return True
    elif userWithdraw > accountBal:
        print('ERROR: Cannot withdraw more than current balance.')
        print('No withdrawal has been made.')
        return False

def receipt():
    global checkBal
    global save1Bal
    global save2Bal
    global startCheck
    global startSave1
    global startSave2
    global endCheck
    global endSave1
    global endSave2
    global depositAll
    global withdrawAll

    print('\n   RECEIPT')
    print('\nChecking Account')
    print('-------------------')
    print('Starting Balance: $', format(startCheck, '.2f'))
    print('Total Deposits:   $', format(depositCheck, '.2f'))
    print('Total Withdraws:  $', format(withdrawCheck, '.2f'))
    print('Ending Balance:   $', format(endCheck, '.2f'))
    print('\nSavings Account 1')
    print('-------------------')
    print('Starting Balance: $', format(startSave1, '.2f'))
    print('Total Deposits:   $', format(depositSave1, '.2f'))
    print('Total Withdraws:  $', format(withdrawSave1, '.2f'))
    print('Ending Balance:   $', format(endSave1, '.2f'))
    print('\nSavings Account 2')
    print('-------------------')
    print('Starting Balance: $', format(startSave2, '.2f'))
    print('Total Deposits:   $', format(depositSave2, '.2f'))
    print('Total Withdraws:  $', format(withdrawSave2, '.2f'))
    print('Ending Balance:   $', format(endSave2, '.2f'))
    print('\nAll Accounts')
    print('-------------------')
    print('Total Deposits:   $', format(depositAll, '.2f'))
    print('Total Withdraws:  $', format(withdrawAll, '.2f'))

def importBal(): # Import current account balances
    global checkBal
    global save1Bal
    global save2Bal

    try:
        startBal = open('bankBalances.txt', 'r')
        checkBal = float(startBal.readline())
        save1Bal = float(startBal.readline())
        save2Bal = float(startBal.readline())
        startBal.close()
    except IOError:
        print('ERROR: File does not exist.')
    except:
        print('ERROR: An unknown error has occurred.')

def exportBal():
    # Finalize totals
    global checkBal
    global save1Bal
    global save2Bal
    global endCheck
    global endSave1
    global endSave2
    endCheck = startCheck + depositCheck - withdrawCheck
    endSave1 = startSave1 + depositSave1 - withdrawSave1
    endSave2 = startSave2 + depositSave2 - withdrawSave2

    receipt() # Display receipt

    # Update balances
    checkBal = endCheck
    save1Bal = endSave1
    save2Bal = endSave2

    # Export final balances to file
    # BONUS: I thought it'd be fun to keep track of the running balance
    # even after the program is closed.
    try:
        finalBal = open('bankBalances.txt', 'w')
        finalBal.write(str(checkBal) + '\n')
        finalBal.write(str(save1Bal) + '\n')
        finalBal.write(str(save2Bal) + '\n')
        finalBal.close()
    except IOError:
        print('ERROR: File does not exist.')
    except:
        print('ERROR: An unknown error has occurred.')
    
def complete():
    exportBal()
    print('\nThank you for using the Pierre Bank ATM!')
    print('Goodbye.')

main()
