
class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._height = value

    def __str__(self) -> str:
        return f"Width: {self.width}, Height: {self.height}"

    @property
    def area(self):
        return self._width * self._height

class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)
    
    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value
    
    @Rectangle.height.setter
    def height(self, value):
        self._height = self._width = value


def use_it(rect):
    w = rect.width # This break's LSP 
    rect.height = 10
    excepted = int(w * 10)
    print(f'Expected an area of {excepted}, got {rect.area}') 

rect = Rectangle(10, 20)
use_it(rect)

sqr = Square(5)
use_it(sqr)