import math

# Capacitance using material properties: C = (εr * ε0 * A) / d
def byMaterial(dielectric, area, distance):
    epsilon_0 = 8.854e-12  # F/m, vacuum permittivity
    capacitance = (dielectric * epsilon_0 * area) / distance
    print(f"Capacitance of material: {capacitance} F")
    return capacitance

# Capacitance using charge and voltage: C = Q / V
def byCV(charge, voltage):
    capacitance = charge / voltage
    print(f"Capacitance by Q/V: {capacitance} F")
    return capacitance

# Capacitor current: I = C * dV/dt
def byCurrent(capacitance, dv_dt):
    current = capacitance * dv_dt
    print(f"Capacitor current: {current} A")
    return current

# Capacitive reactance: Xc = 1 / (2 * pi * f * C)
def byReactance(frequency, capacitance):
    reactance = 1 / (2 * math.pi * frequency * capacitance)
    print(f"Capacitive reactance: {reactance} Ω")
    return reactance

if __name__ == "__main__":
    charge = float(input("Enter charge (Coulombs): "))
    voltage = float(input("Enter voltage (Volts): "))

    capacitance = get_capacitance_by_CV(charge, voltage)
    print(f"Capacitance: {capacitance} F")
