from domain.vehicle import (
    Car,
    Motorcycle,
    ElectricCar,
    ElectricMotorcycle,
)


class VehicleFactory:
    @staticmethod
    def create_vehicle(
        reg_num: str,
        make: str,
        model: str,
        color: str,
        is_electric: bool,
        is_motorcycle: bool,
    ):
        if is_electric:
            if is_motorcycle:
                return ElectricMotorcycle(reg_num, make, model, color)
            return ElectricCar(reg_num, make, model, color)

        if is_motorcycle:
            return Motorcycle(reg_num, make, model, color)

        return Car(reg_num, make, model, color)
