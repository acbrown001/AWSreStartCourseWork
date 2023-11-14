from .Car import Car #importing Car class from Car.py

class ElectricCar(Car): #Electric_Car inherits from Car
    def __init__(self,brand,mileage_km,range):
         super().__init__(brand,mileage_km)
         self.range = range

#Need to define drive


    