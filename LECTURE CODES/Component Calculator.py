import sys
import time

sys.path.append(r"C:\path\to\LECTURE CODES\Component Packages")

import Capacitance
import Inductance
import Resistance


def message():
    print("Welcome to Passive Component Calculator")
    time.sleep(1)
    print("----------------------------------------")


def components():
    while True:
        time.sleep(1)
        selector = input(
            "Choose component (Capacitance / Inductance / Resistance): ").upper()

        match selector:

            # --------------------- CAPACITANCE -----------------------
            case "CAPACITANCE":
                print("\nCapacitance Calculator")
                capCal = input("Choose calculation (BYMAT/BYCV/BYCURRENT/BYREACTANCE): ").upper()

                match capCal:

                    case "BYMAT":
                        print("Capacitance by material selected")
                        dielectric = float(input("Enter dielectric constant: "))
                        area = float(input("Enter area (m^2): "))
                        distance = float(input("Enter distance (m): "))
                        result = Capacitance.byMaterial(dielectric, area, distance)
                        print("Capacitance =", result, "F")
                        return

                    case "BYCV":
                        print("Capacitance by Q/V selected")
                        charge = float(input("Enter charge (C): "))
                        voltage = float(input("Enter voltage (V): "))
                        result = Capacitance.byCV(charge, voltage)
                        print("Capacitance =", result, "F")
                        return

                    case "BYCURRENT":
                        print("Capacitance by current selected")
                        capacitance = float(input("Enter capacitance (F): "))
                        dv_dt = float(input("Enter dv/dt (V/s): "))
                        result = Capacitance.byCurrent(capacitance, dv_dt)
                        print("Current =", result, "A")
                        return

                    case "BYREACTANCE":
                        print("Capacitance by reactance selected")
                        frequency = float(input("Enter frequency (Hz): "))
                        capacitance = float(input("Enter capacitance (F): "))
                        result = Capacitance.byReactance(frequency, capacitance)
                        print("Reactance =", result, "Ω")
                        return

                    case _:
                        print("Invalid Capacitance option.")
                        return

            # --------------------- INDUCTANCE -----------------------
            case "INDUCTANCE":
                print("\nInductance Calculator")
                inCal = input("Choose calculation (BYMAT/BYFLUX/BYVOLTAGE/BYREACTANCE): ").upper()

                match inCal:

                    case "BYMAT":
                        print("Inductance by material selected")
                        permeability = float(input("Enter permeability: "))
                        turns = int(input("Enter number of turns: "))
                        length = float(input("Enter core length (m): "))
                        area = float(input("Enter core area (m²): "))
                        result = Inductance.byMaterial(permeability, turns, length, area)
                        print("Inductance =", result, "H")
                        return

                    case "BYFLUX":
                        print("Inductance by flux selected")
                        flux = float(input("Enter magnetic flux (Wb): "))
                        current = float(input("Enter current (A): "))
                        result = Inductance.byFlux(flux, current)
                        print("Inductance =", result, "H")
                        return

                    case "BYVOLTAGE":
                        print("Inductance by voltage selected")
                        voltage = float(input("Enter voltage (V): "))
                        di_dt = float(input("Enter di/dt (A/s): "))
                        result = Inductance.byVoltage(voltage, di_dt)
                        print("Inductance =", result, "H")
                        return

                    case "BYREACTANCE":
                        print("Inductance by reactance selected")
                        frequency = float(input("Enter frequency (Hz): "))
                        inductance = float(input("Enter inductance (H): "))
                        result = Inductance.byReactance(frequency, inductance)
                        print("Reactance =", result, "Ω")
                        return

                    case _:
                        print("Invalid Inductance option.")
                        return

            # --------------------- RESISTANCE -----------------------
            case "RESISTANCE":
                print("\nResistance Calculator")
                resCal = input("Choose calculation (BYMAT/BYVI/BYVOLTAGE/BYPOWER): ").upper()

                match resCal:

                    case "BYMAT":
                        print("Resistance by material selected")
                        resistivity = float(input("Enter resistivity (Ω·m): "))
                        length = float(input("Enter length (m): "))
                        area = float(input("Enter area (m²): "))
                        result = Resistance.byMaterial(resistivity, length, area)
                        print("Resistance =", result, "Ω")
                        return

                    case "BYVI":
                        print("Resistance by V/I selected")
                        voltage = float(input("Enter voltage (V): "))
                        current = float(input("Enter current (A): "))
                        result = Resistance.byVI(voltage, current)
                        print("Resistance =", result, "Ω")
                        return

                    case "BYVOLTAGE":
                        print("Resistance from voltage and power")
                        voltage = float(input("Enter voltage (V): "))
                        power = float(input("Enter power (W): "))
                        result = Resistance.byVoltage(voltage, power)
                        print("Resistance =", result, "Ω")
                        return

                    case "BYPOWER":
                        print("Resistance from power and current")
                        power = float(input("Enter power (W): "))
                        current = float(input("Enter current (A): "))
                        result = Resistance.byPower(power, current)
                        print("Resistance =", result, "Ω")
                        return

                    case _:
                        print("Invalid Resistance option.")
                        return

            # --------------------- INVALID MAIN MENU -----------------------
            case _:
                print("Invalid component type. Please try again.\n")

message()
components()