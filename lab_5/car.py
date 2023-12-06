
class Car:
    def __init__(self,mark ,car_class ,weight , driver, engine):
        self.mark = mark
        self.car_class = car_class
        self.weight = weight
        self.driver = driver
        self.engine = engine

    def start(self):
        print('Поехали')

    def stop(self):
        print('Останавливаемся')

    def turn_right(self):
        print('Поворот направо')

    def turn_left(self):
        print('Поворот налево')

    def __str__(self):
        print(f'Марка:{self.mark}, Класс:{self.car_class}, Вес:{self.weight}, Водитель:{self.driver.full_name}, '
              f'Стаж вождения:{self.driver.driving_experience}, Мотор:{self.engine.power} л.с., '
              f'Производитель:{self.engine.company}')
