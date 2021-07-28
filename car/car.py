
class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=500

    def descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self,mile):
        if mile >= self.odometer_reading:
            self.odometer_reading=mile
        else:
            print("can't roll back")

    def increment_odometer(self,miles):
        self.odometer_reading += miles
# my_new_car=Car("audi",'ad',2019)
# my_new_car.update_odometer(300)

# my_new_car.increment_odometer(1000)
# my_new_car.read_odometer()




