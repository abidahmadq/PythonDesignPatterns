class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class PersonFactory:
    _id = 0

    @staticmethod
    def create_person(name):
        person = Person(PersonFactory._id, name)
        PersonFactory._id += 1
        return person