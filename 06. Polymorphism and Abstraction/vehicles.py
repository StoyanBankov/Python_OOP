from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    air_conditioning = 0.9

    def drive(self, distance):
        consumption = (self.fuel_consumption + 0.9)*distance

        if consumption <= self.fuel_quantity:
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    air_conditioning = 1.6

    def drive(self, distance):
        consumption = (self.fuel_consumption+  1.6)*distance

        if consumption <= self.fuel_quantity:
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        given_fuel = 0.95 * fuel
        self.fuel_quantity += given_fuel
