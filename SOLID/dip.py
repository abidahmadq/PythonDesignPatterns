from enum import Enum
from abc import abstractmethod
class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name) -> None:
        self.name = name

class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        pass

# IS low level module
class Relationships(RelationshipBrowser):
    def __init__(self):
        self.relations = [] # What if we change this to be a database

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name
        


# Is a high level module
class Research:
    # def __init__(self, relationships):
    #     relations = relationships.relations # ----> What if this is not a dictionary in the future?
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f'John has a child called {r[2].name}')

    def __init__(self, browser):
        for p in browser.find_all_children_of('John'):
            print(f'John has a child called {p}')

# Research should not be depend on a concrete implementation

parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

relationships = Relationships()

relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)