from enum import Enum
from os import P_ALL

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self, name, color, size) -> None:
        self.name = name
        self.color = color
        self.size = size

# OCP = open for extenion, closed for modification

'''
This is not a scalable method.
2 parameter --> 3
3 parameter --> 7

class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p
    
    def filter_by_color(self, products, size):
        for p in products:
            if p.size == size:
                yield p
    
    def filter_by_color(self, products, color, size):
        for p in products:
            if p.color == color and p.size == size:
                yield p
'''

# There are enterprise patterns ie specification 

class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    def filter(self, items, spec):
        pass

class ColorSpecification(Specification):
    def __init__(self, color) -> None:
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpecification(Specification):
    def __init__(self, size) -> None:
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item

class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args
    
    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))

if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)
    product = [apple, tree, house]
    bf = BetterFilter()

    print('Printing Green products')
    green = ColorSpecification(Color.GREEN)

    for p in bf.filter(product, green):
        print(p.name)
    
    large = SizeSpecification(Size.LARGE)

    for p in bf.filter(product, large):
        print(p.name)

    
    print('Large Blue Item')
    # large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
    large_blue = large & ColorSpecification(Color.BLUE)
    for p in bf.filter(product, large_blue):
        print(p.name)