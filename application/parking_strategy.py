from abc import ABC, abstractmethod
from domain.vehicle import Vehicle, ElectricVehicle
from domain.parking_lot import ParkingLot
from typing import Optional

class ParkingStrategy(ABC):
    @abstractmethod
    def assign_slot(self, lot: ParkingLot, vehicle: Vehicle) -> Optional[int]:
        """Return assigned slot index or None if full."""
        pass

class RegularParkingStrategy(ParkingStrategy):
    def assign_slot(self, lot: ParkingLot, vehicle: Vehicle) -> Optional[int]:
        if isinstance(vehicle, ElectricVehicle):
            return None
        return lot.get_empty_slot_index()

class ElectricParkingStrategy(ParkingStrategy):
    def assign_slot(self, lot: ParkingLot, vehicle: Vehicle) -> Optional[int]:
        if isinstance(vehicle, ElectricVehicle):
            return lot.get_empty_ev_slot_index()
        return None
