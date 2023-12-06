from car import Car
class SportCar(Car):
    def __init__(self, mark, car_class, weight, driver, engine, speed):
        super().__init__(mark=mark, car_class=car_class, weight=weight, driver=driver, engine=engine)
        self.speed = speed

    def __str__(self):
        print(f'Марка:{self.mark}, Класс:{self.car_class}, Вес:{self.weight}, Водитель:{self.driver.full_name}, '
              f'Стаж вождения:{self.driver.driving_experience}, Мотор:{self.engine.power} л.с., '
              f'Производитель:{self.engine.company}, Предельная скорость:{self.speed} км/ч')