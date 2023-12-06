from car import Car
from driver import Driver
from engine import Engine
from lorry import Lorry
from sport_car import SportCar

driver_ivan = Driver('Иван Иванов',35,10)
engine_camry = Engine(300, 'Toyota')
toyota = Car("Toyota Camry", "Седан", 1500, driver_ivan, engine_camry)
print('Информация о седане:')
toyota.__str__()

print('\n')

driver_petr = Driver('Петр Петров', 38, 15)
engine_lorry = Engine(300,"Volvo")
lorry_volvo = Lorry('Volvo FH', 'Грузовик', 8000, driver_petr,engine_lorry,5000)
print('Информация о грузовике:')
lorry_volvo.__str__()

print('\n')

driver_anna = Driver('Анна Сидорова', 20,2)
engine_sport_car = Engine(400,'Ferrari')
sport_car_ferrari = SportCar('Ferrari 488','Спроткар', 1500, driver_anna, engine_sport_car,300)
sport_car_ferrari.__str__()