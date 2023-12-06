class Person:
    def __init__(self, full_name, age):
        self.__age = age
        self.full_name = full_name

    def __str__(self):
        print(f"{self.full_name}, {self.__age} лет")