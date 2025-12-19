from typing import List, Optional
from domain.vehicle import Vehicle, ElectricVehicle

class ParkingLot:
    """
    Domain model representing a parking lot level.
    """
    
    def __init__(self, capacity: int, ev_capacity: int, level: int):
        self.level = level
        self.capacity = capacity
        self.ev_capacity = ev_capacity
        
        # None = empty slot
        self.slots: List[Optional[Vehicle]] = [None] * capacity
        self.ev_slots: List[Optional[ElectricVehicle]] = [None] * ev_capacity

    def get_empty_slot_index(self) -> Optional[int]:
        """Return the first empty slot index in regular slots."""
        for i, v in enumerate(self.slots):
            if v is None:
                return i
        return None

    def get_empty_ev_slot_index(self) -> Optional[int]:
        """Return the first empty slot index in EV slots."""
        for i, v in enumerate(self.ev_slots):
            if v is None:
                return i
        return None

    def park_vehicle(self, vehicle: Vehicle, strategy) -> Optional[int]:
        """
        Park a vehicle using a given parking strategy.
        Returns the assigned slot index or None if full.
        """
        if isinstance(vehicle, ElectricVehicle):
            slot_index = strategy.assign_slot(self, vehicle)
            if slot_index is not None:
                self.ev_slots[slot_index] = vehicle
            return slot_index
        else:
            slot_index = strategy.assign_slot(self, vehicle)
            if slot_index is not None:
                self.slots[slot_index] = vehicle
            return slot_index

    def remove_vehicle(self, slot_index: int, is_ev: bool) -> bool:
        """Remove vehicle from a slot."""
        slots_list = self.ev_slots if is_ev else self.slots
        if 0 <= slot_index < len(slots_list) and slots_list[slot_index] is not None:
            slots_list[slot_index] = None
            return True
        return False
