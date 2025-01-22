class Car:

    def __init__(self, new_brand, new_fuel_capacity, new_model, new_fuel_consumption):
        self.__brand = new_brand
        self.model = new_model
        self.__fuel_capacity = new_fuel_capacity
        self.fuel_consumption = new_fuel_consumption
        self.fuel_amount = 0.0
    
    def fill_tank(self):
        self.fuel_amout = self.__fuel_capacity

    def get_fuel_amount(self):
         return self.fuel_amount

    def get_brand(self):
            return self.__brand
    