from domain.parking_lot import ParkingLot
from domain.vehicle import ElectricVehicle
from application.parking_strategy import (
    RegularParkingStrategy,
    ElectricParkingStrategy,
)
from application.vehicle_factory import VehicleFactory


class ParkingService:
    def __init__(self, capacity: int, ev_capacity: int, level: int):
        self.parking_lot = ParkingLot(capacity, ev_capacity, level)
        self.regular_strategy = RegularParkingStrategy()
        self.ev_strategy = ElectricParkingStrategy()

    def park_vehicle(
        self,
        reg_num: str,
        make: str,
        model: str,
        color: str,
        is_electric: bool,
        is_motorcycle: bool,
    ):
        vehicle = VehicleFactory.create_vehicle(
            reg_num,
            make,
            model,
            color,
            is_electric,
            is_motorcycle,
        )

        strategy = (
            self.ev_strategy
            if isinstance(vehicle, ElectricVehicle)
            else self.regular_strategy
        )

        return self.parking_lot.park_vehicle(vehicle, strategy)

    def remove_vehicle(self, slot_index: int, is_ev: bool) -> bool:
        return self.parking_lot.remove_vehicle(slot_index, is_ev)
