from person import Person

class Driver(Person):
    def __init__(self,full_name, age, driving_experience):
        super().__init__(full_name, age)
        self.driving_experience = driving_experience
