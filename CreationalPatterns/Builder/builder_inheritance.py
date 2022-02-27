
class Person:
    def __init__(self) -> None:
        self.name = None
        self.position = None
        self.date_of_birth = None
    
    def __str__(self) -> str:
        return f'{self.name} born on {self.date_of_birth}' + \
            f'works as {self.position}'
    
    @staticmethod
    def new():
        return PersonBuilder()
    
class PersonBuilder:
    def __init__(self):
        self.person = Person()
    
    def build(self):
        return self.person

def PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self

def PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        self.person.position = position
        return self

def PersonBirthDateBuilder(PersonJobBuilder):
    def born(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self

# Abov pattern follow open=close principple
pb = PersonBirthDateBuilder()
me = pb\
    .called('Abid')\
    .works_as_a('Quant')\
    .
    