from .Car import Car #importing Car class from Car.py

class IceCar(Car): #ICE_Car inherits from Car
    def __init__(self,brand,mileage_km,fuel_consumption, fuel_level):
         super().__init__(brand,mileage_km)
         self.fuel_consumption = fuel_consumption
         self.fuel_level = fuel_level
