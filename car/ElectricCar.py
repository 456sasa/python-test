from car import Car

class ElectricCar(Car):
    def __init__(self, make, model, year,Battery):
        super().__init__(make, model, year)
        self.battery = Battery

    def descriptive_name(self):
        long_name = f"electricCar {self.year} {self.make} {self.model}"
        return long_name.title()

