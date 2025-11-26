import math

def byMaterial(mu, turns, area, length):
    """
    mu: permeability of the core (H/m)
    turns: number of turns N
    area: cross-sectional area (m^2)
    length: length of coil (m)
    """
    inductance = (mu * turns**2 * area) / length
    print(f"Inductance of coil: {inductance} H")
    return inductance

# Inductance using flux and current: L = Φ / I
def byFlux(flux, current):
    inductance = flux / current
    print(f"Inductance by flux/current: {inductance} H")
    return inductance

# Inductor voltage: V = L * dI/dt
def byVoltage(inductance, di_dt):
    voltage = inductance * di_dt
    print(f"Inductor voltage: {voltage} V")
    return voltage

# Inductive reactance: Xl = 2 * pi * f * L
def byReactance(frequency, inductance):
    reactance = 2 * math.pi * frequency * inductance
    print(f"Inductive reactance: {reactance} Ω")
    return reactance



def get_inductive_reactance(frequency, inductance):
    reactance = 2 * math.pi * frequency * inductance
    print("Inductive reactance is: " + str(reactance) + " ohms")
    return reactance

# Example usage
if __name__ == "__main__":
    get_inductive_reactance(frequency=1000, inductance=0.00025)