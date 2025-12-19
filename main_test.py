# main_test.py
# Test script for ParkingLot domain and parking strategies

from domain.vehicle import Car, Motorcycle, ElectricCar, ElectricMotorcycle
from domain.parking_lot import ParkingLot
from application.parking_strategy import RegularParkingStrategy, ElectricParkingStrategy

def main():
    # Create a parking lot
    lot = ParkingLot(capacity=5, ev_capacity=2, level=1)

    # Create vehicles
    car1 = Car("ABC123", "Toyota", "Corolla", "Red")
    bike1 = Motorcycle("BIKE01", "Yamaha", "R15", "Blue")
    ev_car1 = ElectricCar("EV001", "Tesla", "Model 3", "Black")
    ev_bike1 = ElectricMotorcycle("EVBIKE1", "Zero", "SR/F", "White")

    # Create strategies
    regular_strategy = RegularParkingStrategy()
    ev_strategy = ElectricParkingStrategy()

    # Park vehicles
    slot_car = lot.park_vehicle(car1, regular_strategy)
    slot_bike = lot.park_vehicle(bike1, regular_strategy)
    slot_ev_car = lot.park_vehicle(ev_car1, ev_strategy)
    slot_ev_bike = lot.park_vehicle(ev_bike1, ev_strategy)

    # Print results
    print("Regular Car assigned slot:", slot_car)
    print("Motorcycle assigned slot:", slot_bike)
    print("EV Car assigned slot:", slot_ev_car)
    print("EV Motorcycle assigned slot:", slot_ev_bike)

    # Remove a vehicle
    removed = lot.remove_vehicle(slot_car, is_ev=False)
    print(f"Removed Regular Car from slot {slot_car}:", removed)

if __name__ == "__main__":
    main()
