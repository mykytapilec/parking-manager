class ParkingLot:
    def __init__(self, capacity: int, ev_capacity: int, level: int):
        self.capacity = capacity
        self.ev_capacity = ev_capacity
        self.level = level

        self.regular_slots = [None] * capacity
        self.ev_slots = [None] * ev_capacity

    def park_vehicle(self, vehicle, strategy):
        return strategy.park(self, vehicle)

    def remove_vehicle(self, slot_index: int, is_ev: bool) -> bool:
        slots = self.ev_slots if is_ev else self.regular_slots

        if 0 <= slot_index < len(slots) and slots[slot_index] is not None:
            slots[slot_index] = None
            return True

        return False
