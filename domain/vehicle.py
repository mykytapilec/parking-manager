from abc import ABC, abstractmethod


class Vehicle(ABC):
    """
    Abstract base class representing a vehicle in the parking system.
    """

    def __init__(self, registration_number: str, make: str, model: str, color: str):
        self.registration_number = registration_number
        self.make = make
        self.model = model
        self.color = color

    @abstractmethod
    def get_type(self) -> str:
        """Return the type of the vehicle."""
        pass


class Car(Vehicle):
    def get_type(self) -> str:
        return "Car"


class Motorcycle(Vehicle):
    def get_type(self) -> str:
        return "Motorcycle"


class ElectricVehicle(Vehicle):
    """
    Base class for electric vehicles.
    """

    def __init__(
        self,
        registration_number: str,
        make: str,
        model: str,
        color: str,
        charge_level: int = 0,
    ):
        super().__init__(registration_number, make, model, color)
        self.charge_level = charge_level

    def get_type(self) -> str:
        return "Electric"


class ElectricCar(ElectricVehicle):
    def get_type(self) -> str:
        return "ElectricCar"


class ElectricMotorcycle(ElectricVehicle):
    def get_type(self) -> str:
        return "ElectricMotorcycle"
