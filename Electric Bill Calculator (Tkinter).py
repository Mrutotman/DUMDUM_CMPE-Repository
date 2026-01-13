import tkinter as tk
from tkinter import ttk, messagebox

# APPLIANCES (Watts)
appliances = {
    "Air Conditioner (1 HP, non-inverter)": 850,
    "Electric Kettle": 1400,
    "Electric Fan (Stand)": 65,
    "Electric Heater": 1000,
    "Microwave Oven": 1100,
    "Desktop Computer": 220,
    "Laptop": 55,
    "Refrigerator (Non-inverter)": 100,
    "Television (LED, 32–43\")": 90,
    "Washing Machine": 350,
    "LED Light Bulb": 9
}

total_kWh = 0.0
entries = []  # store (description, energy)

# ---------------- FUNCTIONS ---------------- #

def add_appliance():
    global total_kWh

    try:
        appliance = appliance_var.get()
        if appliance == "":
            raise ValueError

        power = appliances[appliance]
        hours = float(hours_entry.get())
        days = float(days_entry.get())

        energy = (power * hours * days) / 1000
        total_kWh += energy

        entry_text = f"{appliance} → {round(energy, 3)} kWh"
        consumption_list.insert(tk.END, entry_text)
        entries.append(energy)

        total_label.config(text=f"Total Energy: {round(total_kWh, 3)} kWh")

        # clear inputs
        hours_entry.delete(0, tk.END)
        days_entry.delete(0, tk.END)

    except:
        messagebox.showerror("Input Error", "Please enter valid values.")

def remove_appliance():
    global total_kWh

    try:
        index = consumption_list.curselection()[0]
        energy = entries.pop(index)

        total_kWh -= energy
        consumption_list.delete(index)

        total_label.config(text=f"Total Energy: {round(total_kWh, 3)} kWh")

    except:
        messagebox.showerror("Selection Error", "Please select an item to remove.")

def calculate_bill():
    try:
        price = float(price_entry.get())
        vat = float(vat_entry.get())

        base = total_kWh * price
        vat_value = base * vat / 100
        total = base + vat_value

        result_label.config(
            text=(
                f"Base Charge: ₱{round(base, 2)}\n"
                f"VAT: ₱{round(vat_value, 2)}\n"
                f"Total Bill: ₱{round(total, 2)}"
            )
        )
    except:
        messagebox.showerror("Input Error", "Enter valid price and VAT.")

# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Electric Bill Calculator")
root.geometry("520x560")

tk.Label(root, text="Electric Bill Calculator", font=("Arial", 16, "bold")).pack(pady=10)

# Appliance dropdown
appliance_var = tk.StringVar()
appliance_box = ttk.Combobox(
    root, textvariable=appliance_var,
    values=list(appliances.keys()), state="readonly", width=45
)
appliance_box.pack(pady=5)

# Usage inputs
frame1 = tk.Frame(root)
frame1.pack(pady=10)

tk.Label(frame1, text="Hours/day").grid(row=0, column=0)
hours_entry = tk.Entry(frame1, width=10)
hours_entry.grid(row=0, column=1, padx=5)

tk.Label(frame1, text="Days").grid(row=0, column=2)
days_entry = tk.Entry(frame1, width=10)
days_entry.grid(row=0, column=3, padx=5)

tk.Button(root, text="Add Appliance", command=add_appliance).pack(pady=5)

# Consumption list
tk.Label(root, text="Added Appliances").pack()
consumption_list = tk.Listbox(root, width=60, height=7)
consumption_list.pack(pady=5)

tk.Button(root, text="Remove Selected Appliance", command=remove_appliance).pack(pady=5)

total_label = tk.Label(root, text="Total Energy: 0.0 kWh", font=("Arial", 11, "bold"))
total_label.pack(pady=5)

# Billing section
frame2 = tk.Frame(root)
frame2.pack(pady=10)

tk.Label(frame2, text="Price per kWh (₱)").grid(row=0, column=0)
price_entry = tk.Entry(frame2, width=10)
price_entry.grid(row=0, column=1, padx=5)

tk.Label(frame2, text="VAT (%)").grid(row=0, column=2)
vat_entry = tk.Entry(frame2, width=10)
vat_entry.grid(row=0, column=3, padx=5)

tk.Button(root, text="Calculate Bill", command=calculate_bill).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 11))
result_label.pack()

root.mainloop()
