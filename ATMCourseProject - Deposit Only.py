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
## Date          Description
## -------------------------
## 02/06         Initial draft, added Variables & Login Interface
## 02/17         Updated variables
## 02/23         Added functions, global variables
##               Added Main Menu and Account Menu
##               Added deposit logic
##
## **************************************************

# Variable Declaration
checkBal = 500.0     # Current balance of checking account
save1Bal = 1500.0    # Current balance of first savings account
save2Bal = 5000.0    # Current balance of second savings account
menuChoice = 0       # User selection of main menu
accountChoice = 0    # User selection of account menu
userWithdraw = 0.0   # User selected amount to withdraw
userDeposit = 0.0    # User input of deposit amount
endCheck = 0.0       # Ending balance of checking account
endSave1 = 0.0       # Ending balance of first savings account
endSave2 = 0.0       # Ending balance of second savings account
depositCheck = 0.0   # Total deposits made to the checking account
depositSave1 = 0.0   # Total deposits made to the first savings account
depositSave2 = 0.0   # Total deposits made to the second savings account
depositAll = 0.0     # Total of all deposits made during the transaction
withdrawCheck = 0.0  # Total withdrawals made from the checking account
withdrawSave1 = 0.0  # Total withdrawals made from the first savings account
withdrawSave2 = 0.0  # Total withdrawals made from the second savings account
withdrawAll = 0.0    # Total of all withdrawals made during the transaction

# Main Menu - Global Variables
BALANCE = 1  # Check the balance of an account
DEPOSIT = 2  # Deposit funds into an account
WITHDRAW = 3 # Withdraw funds from an account
COMPLETE = 4 # Complete the transaction
# Account Menu - Global Variables
CHECK = 1    # Checking account
SAVE1 = 2    # Savings Account 1
SAVE2 = 3    # Savings Account 2

def main():
    # Import Menu Options
    global FUND
    global DEPOSIT
    global WITHDRAW
    global COMPLETE

    welcome()
    menuChoice = 0
    while menuChoice != COMPLETE:
        menuChoice = mainMenu()
        if menuChoice == BALANCE:
            print('ERROR: Only deposit currently available.')
        elif menuChoice == DEPOSIT:
            accountChoice = accountMenu()
            deposit(accountChoice)
        elif menuChoice == WITHDRAW:
            print('ERROR: Only deposit currently available.')
    else:
        complete()

def welcome():
    # Welcome Message
    print("Welcome to Pierre Bank!")

def login():
    # Login Variables
    accountNum = 123456  # User’s account number
    pin = 9999           # User’s Personal Identification Number (PIN)
    userAccount = 0      # User input of account number
    userPIN = 0          # User input of PIN
    # User Login Interface
    userAccount = int(input("Please enter your Account Number: "))
    userPIN = int(input("Please enter your PIN: "))
    if userAccount == accountNum and userPIN == pin:
        print("Login Successful.")
        return True
    else:
        print ("Login Failed.")
        return False

def mainMenu():
    print('\n   MAIN MENU')
    print('1) Fund Balance Inquiry')
    print('2) Deposit')
    print('3) Withdraw')
    print('4) Exit')
    menuChoice = int(input('\nPlease make a menu selection: '))
    if menuChoice == 1 or menuChoice == 2 or menuChoice == 3 or menuChoice == 4:
        return menuChoice
    else:
        print('ERROR: Invalid Selection.')

def accountMenu():
    print('\n   ACCOUNT MENU')
    print('1) Checking Account')
    print('2) Savings Account 1')
    print('3) Savings Account 2')
    menuChoice = int(input('\nSelect an account: '))
    if menuChoice == 1 or menuChoice == 2 or menuChoice == 3:
        return menuChoice
    else:
        print('ERROR: Invalid Selection.')

def fund():
    ### TO DO ###
    print('Coming Soon')
    
def deposit(accountChoice):
    global checkBal
    global save1Bal
    global save2Bal
    global depositAll
    # Checking Account Deposit
    if accountChoice == 1:
        userDeposit = input('Enter deposit amount: ')
        if validDeposit(userDeposit):
            checkBal += float(userDeposit)
            depositAll += float(userDeposit)
            print('Deposit accepted. Balance updated.')
            print('Thank you for your deposit.')
        else:
            print('ERROR: Deposit must be a number between 1-1000.')
            print('No deposit has been made.')
    # Savings Account 1 Deposit
    elif accountChoice == 2:
        userDeposit = input('Enter deposit amount: ')
        if validDeposit(userDeposit):
            save1Bal += float(userDeposit)
            depositAll += float(userDeposit)
            print('Deposit accepted. Balance updated.')
            print('Thank you for your deposit.')
        else:
            print('ERROR: Deposit must be a number between 1-1000.')
            print('No deposit has been made.')
    # Savings Account 2 Deposit
    elif accountChoice == 3:
        userDeposit = input('Enter deposit amount: ')
        if validDeposit(userDeposit):
            save2Bal += float(userDeposit)
            depositAll += float(userDeposit)
            print('Deposit accepted. Balance updated.')
            print('Thank you for your deposit.')
            #print('Current balance for Savings Account 2: $', format(save2Bal, '.2f')) # TEST LINE ONLY
        else:
            print('ERROR: Deposit must be a number between 1-1000.')
            print('No deposit has been made.')

def validDeposit(userDeposit):
    # Checking Account Deposit Validation
    if userDeposit.isnumeric():
        userDeposit = float(userDeposit)
        if userDeposit > 0 and userDeposit <= 1000:
            return True
    else:
        return False

def withdraw():
    ### TO DO ### 
    print('Coming Soon')

def validWithdraw():
    ### TO DO ###
    print('Coming Soon')

def complete():
    ### TO DO ###
    print('Goodbye.')

main()
