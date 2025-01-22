from car import Car


def test_some_cars():
    car1 = Car("Volvo", 5.3, 1, 1)
    print(car1.__brand)
    print(car1.get_fuel_level())
    car1.fill_tank()
    print(car1.get_fuel_level())

test_some_cars()
