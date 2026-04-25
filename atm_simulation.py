balance = 5000 #current balance
transactions = [] #to store the transaction history
PIN = "1234"  #atm pin


def display_balance():  #function to check balance
    print(f"\n Current Balance: RS {balance}")


def deposit_money():
    global balance
    amount = int(input("Enter the amount to deposit: "))

    if amount > 0:
        balance += amount
        transactions.append(f"Deposited amount : RS {amount}")
        print(f"{amount} deposited successfully")
        print(f"Current balance: RS {balance}")
    else:
        print("Please enter valid amount")


def withdraw_money():
    global balance
    amount= int(input("Enter amount to withdraw: "))
    if amount<= 0:
        print("Please enter valid amount")
    elif amount > balance:
        print("Insufficient balance")
    else:
        balance-= amount
        transactions.append(f"RS {amount} withdrawn")
        print(f"{amount} withdrawn successfully")
        print(f"Current balance: RS {balance}")

    
def statements():
    print("\n Transaction history: ")
    if not transactions:
        print("No transaction yet")
    else:
        for transaction in transactions:
            print(transaction)



def atm():
    attempts = 3

    while attempts > 0:
        entered_pin = input("Enter your pin: ")

        if entered_pin == PIN:
            print("\n Login Successfull")

            while True:
                print("1.  Check Balance")
                print("2.  Deposit Money")
                print("3.  Withdraw Money")
                print("4.  Check Statements")
                print("5.  Exit")

                choice = input("Enter your choice: ")

                if choice == '1':
                    display_balance()
                elif choice == '2':
                    deposit_money()
                elif choice == '3':
                    withdraw_money()
                elif choice == '4':
                    statements()
                elif choice == '5':
                    print("Thank you for using ATM")
                    break
                else:
                    print("Invalid Chice")

            break
        else:
            attempts -= 1
            print("Please enter valid pin")
            print(f"{attempts} attempts left")

    if attempts == 0:
        print("Card blocked. Please contact your bank")



atm()