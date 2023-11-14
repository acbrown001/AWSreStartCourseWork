from classes import IceCar, ElectricCar

def main():
    my_ev = ElectricCar("Tesla", 90000, 500)
    my_ev.drive(distance_km=100)

    my_ice = IceCar("Toyota", 990000, 1000, 30)
    my_ice.drive(distance_km=9999)

    print(my_ice.__dict__)
    print(my_ev.__dict__)

if __name__ == "__main__":
    main()
