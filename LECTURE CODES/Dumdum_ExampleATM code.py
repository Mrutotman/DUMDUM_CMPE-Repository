import time
amount = 0
balance = -1
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
    transaction = input("Please select your transaction (withdraw/balance): ").lower()
    return transaction

def transaction_validation(amount, balance):
    if balance >= amount:
        return True
    else:
        print("Insufficient Balance")
        return False


def card_ejection():
    # call driver for card ejection mechanism
    print("Card is ejected. Please get your card")
    quit()

def receipt():
    time.sleep(1)
    print("Printing Receipt")
    time.sleep(1)
    print("-----------------")
    time.sleep(1)
    print("Your transaction details:")
    print("Amount:", str(amount))
    print("Balance:", str(balance))
    print("-----------------")
    time.sleep(1)



while True:
    welcome_message()
    isCardInserted = input("Is Card Inserted? (y/n): ").lower()  # SENSOR
    if not card_reader(isCardInserted):  # FALSE
        continue

    time.sleep(1)

    print("INPUT YOUR PIN NUMBER")
    if not valid():  # FALSE
        continue

    print("-------------")

    time.sleep(1)

    transaction = transaction_selection()

    if transaction == "withdraw":
        amount = int(input("Please enter your amount: "))
        if transaction_validation(amount, balance):
            balance -= amount  # decrease the balance
            print("Withdraw Operation Successful. New Balance:", str(balance))
            receipt = receipt()
            time.sleep(1)
        else:
            print("Transaction failed due to insufficient balance.")
            break

    elif transaction == "balance":
            print("------------------")
            time.sleep(1)
            print("Your current balance:", str(balance))
            print("------------------")
            time.sleep(1)
            receipt()
    else:
        print("Invalid transaction")

    card_ejection()



