from ElectricCar import ElectricCar
from battery import Battery

new_battery = Battery(15000)
new_electricCar=ElectricCar("BYD","汉",2020,new_battery)
new_electricCar.battery.descriptive_battery()
print(new_electricCar.descriptive_name())