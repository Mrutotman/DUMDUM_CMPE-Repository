import time

amount = 0
balance = 1000
PIN = "1232"

def welcome_message():
    print("Welcome to BSECE 1-4 Bank of the Philippines")
    time.sleep(1)
    print("-------------------------")
    time.sleep(1)
    print("Please enter your card")


def card_reader(isCardInserted):
    if isCardInserted == "y":
        print("Card is inserted")
        return True
    else:
        print("Card is not inserted properly")
        return False


def valid():
    for i in range(4):
        if i == 3:
            print("Your Card is Blocked")
            quit()
        inPIN = input("Enter your PIN: ")
        if inPIN == PIN:
            return True
        else:
            print("Invalid PIN")


def transaction_selection():
    return input("Please select your transaction (withdraw/balance): ").lower()


def transaction_validation(amount, balance):
    if balance >= amount:
        return True
    else:
        print("Insufficient Balance")
        return False


def card_ejection():
    print("Card is ejected. Please get your card")
    quit()


def receipt(amount, balance):
    time.sleep(1)
    print("Printing Receipt")
    time.sleep(1)
    print("-----------------")
    print("Your transaction details:")
    print("Amount:", str(amount))
    print("Balance:", str(balance))
    print("-----------------")
    time.sleep(1)


# ========================
#       MAIN PROGRAM
# ========================

while True:
    welcome_message()

    isCardInserted = input("Is Card Inserted? (y/n): ").lower()
    if not card_reader(isCardInserted):
        continue

    time.sleep(1)

    print("INPUT YOUR PIN NUMBER")
    if not valid():
        continue

    print("-------------")
    time.sleep(1)

    while True:  # loop for balance inquiry
        transaction = transaction_selection()

        if transaction == "withdraw":
            amount = int(input("Please enter your amount: "))

            if transaction_validation(amount, balance):
                balance -= amount
                print("Withdraw Operation Successful. New Balance:", str(balance))
                receipt(amount, balance)
                time.sleep(1)
                card_ejection()  # eject card ONLY after withdrawal
            else:
                print("Transaction failed due to insufficient balance.")
                break

        elif transaction == "balance":
            print("------------------")
            print("Your current balance:", str(balance))
            print("------------------")
            receipt(0, balance)
            print("You may continue your transaction.")
            print("--------------------------------")
            time.sleep(1)
            # Does NOT eject card — loops back to transaction menu

        else:
            print("Invalid transaction")
