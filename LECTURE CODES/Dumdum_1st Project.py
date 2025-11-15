# ELECTRIC BILL CHECKER
import time

def message():
    print("Welcome to electric bill calculator")
    time.sleep(1)
    print("------------------------------------")
    time.sleep(1)
    print("Please enter the following parameters:")

def electricbill():
    while True:
        try:
            PpW = float(input("Enter price per kWh (₱): ")) # PRICE PER kWh
            kWh = float(input("Enter your electricity consumption (kWh): ")) # AMOUNT OF kWh
            nVAT = float(input("Enter VAT percentage (%): ")) # VALUE ADDED TAAX PERCENTAGE

            base = round(kWh * PpW, 3)  # total electric bill
            VAT = round(base * nVAT / 100, 3)  # Value added tax
            total = round(base + VAT, 3)  # total bill

            print("Base Charge: ₱", str(base))
            print("VAT: ₱", str(VAT))
            print("Total Bill: ₱", str(total))

            choice = input("Do you want to calculate another bill? (y/n): ").lower()
            if choice == 'n':
                print("Thank you for using the electric bill calculator!")
                quit()
            elif choice != 'y':
                print("very very stupid")

        except ValueError:
            print("Please enter valid numbers.")


def test():
    while True:
        message()
        time.sleep(1)
        electricbill()

test()