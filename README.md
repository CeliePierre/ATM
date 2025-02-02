# ATM Prototype Project

![ATM Prototype](atm-cat3.jpeg)

![Python](https://img.shields.io/badge/Python-3.7.2-blue.svg)

## Project Overview
This project is an **Automated Teller Machine (ATM) Prototype** developed in Python as part of an *Introduction to Computer Programming* course. The goal of this project is to simulate ATM functionality, including user authentication, balance inquiries, deposits, and withdrawals, while adhering to a set of business requirements.

## Features
- **User Account and PIN Verification**
  - Users must enter a valid account number and a 4-digit PIN to access the ATM functions.
  - The program verifies the credentials against a statically assigned dummy account.
  - If invalid credentials are entered, access is denied with an informative message.
- **ATM Transactions**
  - **Fund Balance Inquiry**: View available balance for each account.
  - **Deposit**: Add funds to any account with a limit of $1,000 per deposit.
  - **Withdraw**: Withdraw fixed amounts ($20, $40, $60, $80, or $100) while following business rules.
  - **Exit**: Display a summary of the session before exiting.
- **File Handling**
  - The program reads account balances from `bankBalances.txt` at startup.
  - Account balances are updated and saved back to `bankBalances.txt` upon exit.
- **Receipt Generation**
  - A transaction receipt is displayed upon exiting, summarizing deposits, withdrawals, and final balances for all accounts.
- **Error Handling**
  - Handles invalid menu selections and non-numeric input gracefully.
  - Ensures deposits and withdrawals follow predefined limits.

## Business Rules
- Users have three accounts:
  - Checking: **$500**
  - Savings 1: **$1,500**
  - Savings 2: **$5,000**
- **Withdrawal Restrictions**:
  - Cannot withdraw more than the available balance.
  - Maximum withdrawal per account: **$300** per session.
  - Maximum withdrawal across all accounts: **$750** per session.
- **Deposit Restrictions**:
  - Deposit amounts must be **greater than $0** and **less than or equal to $1,000**.
- Users can process multiple transactions in one session.

## Transaction Summary Upon Exit
After exiting, the program displays a summary for each account:
1. **Starting Fund Balance**
2. **Total Deposits**
3. **Total Withdrawals**
4. **Ending Fund Balance**

Additionally, it shows:
- **Total Deposits** across all accounts
- **Total Withdrawals** across all accounts

## Installation & Usage
### Prerequisites
- Python 3.7.2 must be installed on your system.

### Running the Program
1. Clone the repository:
   ```bash
   git clone https://github.com/CeliePierre/ATM.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ATM
   ```
3. Ensure `bankBalances.txt` is present with initial balances:
   ```
   500.0
   1500.0
   5000.0
   ```
4. Run the ATM program:
   ```bash
   python ATMCourseProject.py
   ```

## License
This project is for educational purposes and does not require a license.
