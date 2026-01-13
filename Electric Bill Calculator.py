# ELECTRIC BILL CALCULATOR WITH APPLIANCE MENU
import time

# APPLIANCES
appliances = { #COMMON APPLIANCE IN HOUSEHOLDS in Watts (W)
    "1": ("Air Conditioner (1 HP, non-inverter)", 850),
    "2": ("Electric Kettle", 1400),
    "3": ("Electric Fan (Stand)", 65),
    "4": ("Electric Heater", 1000),
    "5": ("Microwave Oven", 1100),
    "6": ("Desktop Computer", 220),
    "7": ("Laptop", 55),
    "8": ("Refrigerator (Non-inverter)", 100),
    "9": ("Television (LED, 32–43\")", 90),
    "10": ("Washing Machine", 350),
    "11": ("LED Light Bulb", 9)
}

#DISPLAY
def message(): #INTRODUCTORY MESSAGE IN CONSOLE
    print("\nWelcome to Electric Bill Calculator")
    time.sleep(1)
    print("------------------------------------")
    time.sleep(1)
    print("Select appliances and usage details")

#INPUT VALIDATION
def inputVald(prompt):
    while True:
        value = input(prompt)
        if value.replace('.', '', 1).isdigit():
            return float(value)
        else:
            print("Please enter a valid number.")

#APPLIANCE CALCULATOR
def appliance_calculator():
    total_kWh = 0 #Initial Value

    while True:
        print("\nAvailable Appliances:")
        for key, value in appliances.items():
            print(f"{key}. {value[0]} ({value[1]} W)")

        choice = input("Choose appliance number: ")

        if choice not in appliances:
            print("Invalid choice.")
            continue

        name, power = appliances[choice]
        hours = inputVald("Hours used per day: ") #using a validation input instead of float()
        days = inputVald("Number of days used: ") #using a validation input instead of float()

        energy = (power * hours * days) / 1000
        total_kWh += energy

        print(f"{name} consumption: {round(energy, 3)} kWh")

        again = input("Add another appliance? (y/n): ").lower()
        if again == 'n':
            break

    print(f"\nTotal Energy Consumption: {round(total_kWh, 3)} kWh")
    return total_kWh

#BILL CALCULATOR
def electric_bill(kWh):
    price = inputVald("\nEnter price per kWh (₱): ") #in PH, it is around P12-P14/kWh
    vat = inputVald("Enter VAT percentage (%): ") #in PH, it is 12% Value Added Tax

    base = round(kWh * price, 3)
    vat_value = round(base * vat / 100, 3)
    total = round(base + vat_value, 3)

    print("\nElectric Bill Summary")
    print("----------------------")
    print("Total kWh:", round(kWh, 3))
    print("Base Charge: ₱", base)
    print("VAT: ₱", vat_value)
    print("Total Bill: ₱", total)

#MAIN PROGRAM
def main():
    message()
    time.sleep(1)
    kWh = appliance_calculator()
    electric_bill(kWh)
    print("\nThank you for using the Electric Bill Calculator!")
main()
