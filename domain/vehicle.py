from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, reg_num: str, make: str, model: str, color: str):
        self.reg_num = reg_num
        self.make = make
        self.model = model
        self.color = color

    @abstractmethod
    def get_type(self) -> str:
        pass


class Car(Vehicle):
    def get_type(self) -> str:
        return "Car"


class Motorcycle(Vehicle):
    def get_type(self) -> str:
        return "Motorcycle"


class ElectricVehicle(Vehicle):
    def __init__(self, reg_num: str, make: str, model: str, color: str):
        super().__init__(reg_num, make, model, color)
        self.charge = 100


class ElectricCar(ElectricVehicle):
    def get_type(self) -> str:
        return "Electric Car"


class ElectricMotorcycle(ElectricVehicle):
    def get_type(self) -> str:
        return "Electric Motorcycle"
