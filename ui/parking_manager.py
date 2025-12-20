import tkinter as tk
from application.parking_service import ParkingService


parking_service = None

root = tk.Tk()
root.geometry("650x700")
root.title("Parking Lot Manager")

num_value = tk.StringVar()
ev_value = tk.StringVar()
level_value = tk.StringVar(value="1")

make_value = tk.StringVar()
model_value = tk.StringVar()
color_value = tk.StringVar()
reg_value = tk.StringVar()

ev_car_value = tk.IntVar()
motor_value = tk.IntVar()

slot_value = tk.StringVar()
ev_remove_value = tk.IntVar()

output = tk.Text(root, width=70, height=15)
output.grid(row=20, column=0, columnspan=4, padx=10, pady=10)


def create_lot():
    global parking_service
    parking_service = ParkingService(
        capacity=int(num_value.get()),
        ev_capacity=int(ev_value.get()),
        level=int(level_value.get()),
    )
    output.insert(tk.END, "Parking lot created\n")


def park_vehicle():
    if not parking_service:
        output.insert(tk.END, "Create parking lot first\n")
        return

    slot = parking_service.park_vehicle(
        reg_num=reg_value.get(),
        make=make_value.get(),
        model=model_value.get(),
        color=color_value.get(),
        is_electric=ev_car_value.get() == 1,
        is_motorcycle=motor_value.get() == 1,
    )

    if slot is None:
        output.insert(tk.END, "No available slot\n")
    else:
        output.insert(tk.END, f"Vehicle parked at slot {slot}\n")


def remove_vehicle():
    if not parking_service:
        output.insert(tk.END, "Create parking lot first\n")
        return

    success = parking_service.remove_vehicle(
        slot_index=int(slot_value.get()),
        is_ev=ev_remove_value.get() == 1,
    )

    if success:
        output.insert(tk.END, "Vehicle removed\n")
    else:
        output.insert(tk.END, "Failed to remove vehicle\n")


# UI layout
tk.Label(root, text="Regular slots").grid(row=0, column=0)
tk.Entry(root, textvariable=num_value).grid(row=0, column=1)

tk.Label(root, text="EV slots").grid(row=1, column=0)
tk.Entry(root, textvariable=ev_value).grid(row=1, column=1)

tk.Label(root, text="Level").grid(row=2, column=0)
tk.Entry(root, textvariable=level_value).grid(row=2, column=1)

tk.Button(root, text="Create Parking Lot", command=create_lot).grid(row=3, column=0)

tk.Label(root, text="Make").grid(row=4, column=0)
tk.Entry(root, textvariable=make_value).grid(row=4, column=1)

tk.Label(root, text="Model").grid(row=5, column=0)
tk.Entry(root, textvariable=model_value).grid(row=5, column=1)

tk.Label(root, text="Color").grid(row=6, column=0)
tk.Entry(root, textvariable=color_value).grid(row=6, column=1)

tk.Label(root, text="Registration").grid(row=7, column=0)
tk.Entry(root, textvariable=reg_value).grid(row=7, column=1)

tk.Checkbutton(root, text="Electric", variable=ev_car_value).grid(row=8, column=0)
tk.Checkbutton(root, text="Motorcycle", variable=motor_value).grid(row=8, column=1)

tk.Button(root, text="Park Vehicle", command=park_vehicle).grid(row=9, column=0)

tk.Label(root, text="Slot").grid(row=10, column=0)
tk.Entry(root, textvariable=slot_value).grid(row=10, column=1)

tk.Checkbutton(root, text="EV Slot", variable=ev_remove_value).grid(row=11, column=0)

tk.Button(root, text="Remove Vehicle", command=remove_vehicle).grid(row=12, column=0)

root.mainloop()
