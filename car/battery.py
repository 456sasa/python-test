class Battery:
    def __init__(self,battery_size):
        self.battery_size=battery_size    
    def descriptive_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery")


battery= Battery(1000)
print(battery.battery_size)
battery.descriptive_battery()