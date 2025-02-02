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
## Date               Description
## ------------------------------
## 2019/02/06         Initial draft, added Variables & Login Interface
## 2019/02/17         Updated variables
## 2019/02/23         Added functions, global variables
##                    Added Main Menu and Account Menu
##                    Added deposit logic
## 2019/02/27         Added receipt logic
##                    Added balance file import/export
##                    Corrected login error
## 2019/03/02         Isolated receipt logic
##
## **************************************************

# Variable Declaration
menuChoice = 0       # User selection of main menu
accountChoice = 0    # User selection of account menu
userWithdraw = 0     # User selected amount to withdraw
userDeposit = 0.0    # User input of deposit amount
# Current balances of...
checkBal = 500.0     # Checking Account
save1Bal = 1500.0    # Savings Account 1
save2Bal = 5000.0    # Savings Account 2
# Starting balances of...
startCheck = 0.0     # Checking Account
startSave1 = 0.0     # Savings Account 1
startSave2 = 0.0     # Savings Account 2
# Ending balances of...
endCheck = 0.0       # Checking Account
endSave1 = 0.0       # Savings Account 1
endSave2 = 0.0       # Savings Account 2
# Total deposits made to...
depositCheck = 0.0   # Checking Account
depositSave1 = 0.0   # Savings Account 1
depositSave2 = 0.0   # Savings Account 2
depositAll = 0.0     # All accounts
# Total withdrawals made from...
withdrawCheck = 0.0  # Checking Account
withdrawSave1 = 0.0  # Savings Account 1
withdrawSave2 = 0.0  # Savings Account 2
withdrawAll = 0.0    # All accounts
# Main Menu - Global Variables
BALANCE = 1  # Check the balance of an account
DEPOSIT = 2  # Deposit funds into an account
WITHDRAW = 3 # Withdraw funds from an account
COMPLETE = 4 # Complete the transaction / exit
# Account Menu - Global Variables
CHECK = 1    # Checking account
SAVE1 = 2    # Savings Account 1
SAVE2 = 3    # Savings Account 2

def main(): # for Iteration 6 only
    global checkBal
    global save1Bal
    global save2Bal
    global startCheck
    global startSave1
    global startSave2
    startCheck = checkBal
    startSave1 = save1Bal
    startSave2 = save2Bal
    receipt()

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

main()
