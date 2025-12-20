from abc import ABC, abstractmethod


class ParkingStrategy(ABC):
    @abstractmethod
    def park(self, parking_lot, vehicle):
        pass


class RegularParkingStrategy(ParkingStrategy):
    def park(self, parking_lot, vehicle):
        for i, slot in enumerate(parking_lot.regular_slots):
            if slot is None:
                parking_lot.regular_slots[i] = vehicle
                return i
        return None


class ElectricParkingStrategy(ParkingStrategy):
    def park(self, parking_lot, vehicle):
        for i, slot in enumerate(parking_lot.ev_slots):
            if slot is None:
                parking_lot.ev_slots[i] = vehicle
                return i
        return None
