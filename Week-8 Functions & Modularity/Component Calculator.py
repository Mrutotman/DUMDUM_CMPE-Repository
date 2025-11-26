import sys
import time

sys.path.append(r"C:\path\to\LECTURE CODES\Component Packages")  # folder containing Capacitance.py

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
            "Please choose the type of calculation you want to perform (Capacitance/Inductance/Resistance): ").upper()

        match selector:
            case "CAPACITANCE":
                print("Capacitance Calculator")
                capCal = input("Please choose the calculation (BYMAT/BYCV/BYCURRENT/BYREACTANCE): ").upper()
                match capCal:
                    case "BYMAT": #(dielectric, area, distance)
                        print("Capacitance by material selected")
                        dielectric = float(input("Please choose the dielectric constant of the material calculation: "))
                        area = float(input("Please choose the area of the material calculation: "))
                        distance = float(input("Please choose the length of the material calculation: "))
                        capCalbyMat = Capacitance.byMaterial(dielectric, area, distance)
                        print(capCalbyMat)
                        break

                    case "BYCV": #(charge, voltage)
                        print("Capacitance by CV selected")
                        # Capacitance.byCV(...)
                        break
                    case "BYCURRENT": #(capacitance, dv_dt)
                        print("Capacitance by current selected")
                        # Capacitance.byCurrent(...)
                        break
                    case "BYREACTANCE": #(frequency, capacitance)
                        print("Capacitance by reactance selected")
                        # Capacitance.byReactance(...)
                        break
                    case _:
                        print("Invalid selection for Capacitance")
                        break
                break

            case "INDUCTANCE":
                print("Inductance Calculator")
                inCal = input("Please choose the calculation (BYMAT/BYFLUX/BYVOLTAGE/BYREACTANCE): ").upper()
                match inCal:
                    case "BYMAT":
                        print("Inductance by material selected")
                        break
                    case "BYFLUX":
                        print("Inductance by flux selected")
                        break
                    case "BYVOLTAGE":
                        print("Inductance by voltage selected")
                        break
                    case "BYREACTANCE":
                        print("Inductance by reactance selected")
                        break
                    case _:
                        print("Invalid selection for Inductance")
                        break
                break

            case "RESISTANCE":
                print("Resistance Calculator")
                resCal = input("Please choose the calculation (BYMAT/BYVI/BYVOLTAGE/BYPOWER): ").upper()
                match resCal:
                    case "BYMAT":
                        print("Resistance by material selected")
                        break
                    case "BYVI":
                        print("Resistance by VI selected")
                        break
                    case "BYVOLTAGE":
                        print("Resistance by voltage selected")
                        break
                    case "BYPOWER":
                        print("Resistance by power selected")
                        break
                    case _:
                        print("Invalid selection for Resistance")
                        break

            case _:
                print("Invalid component type. Please try again.")
                break


# Run the program
message()
components()