import math

# Resistance using material properties: R = ρ * L / A
def byMaterial(resistivity, length, area):
    """
    resistivity: material resistivity (ohm·m)
    length: length of conductor (m)
    area: cross-sectional area (m^2)
    """
    resistance = resistivity * length / area
    print(f"Resistance of material: {resistance} Ω")
    return resistance

# Resistance using voltage and current: R = V / I
def byVI(voltage, current):
    resistance = voltage / current
    print(f"Resistance by V/I: {resistance} Ω")
    return resistance

# Voltage across a resistor: V = I * R
def byVoltage(current, resistance):
    voltage = current * resistance
    print(f"Voltage across resistor: {voltage} V")
    return voltage

# Power dissipated in resistor: P = I^2 * R
def byPower(current, resistance):
    power = current**2 * resistance
    print(f"Power dissipated: {power} W")
    return power