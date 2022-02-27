# circle square
# Two implementations of drawing -> vector raster

# Normal Approach
# 4 classes VectorCirle VectorSquare RasterCircle RasterSquare
from abc import ABC

# This breaks open-close principle as we will keep on having to add functions.
class Renderer(ABC):
    def render_circle(self, radius):
        pass
    

class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing a circle of radius {radius}')
    
class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing pixels for a circle of radius {radius}')

# Adding a parameter of one hiearchy to another is Bridge pattern
class Shape:
    def __init__(self, renderer):
        self.renderer = renderer
    
    def draw(self):
        pass

    def resize(self, factor):
        pass

class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius
    
    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor

if __name__ == '__main__':
    raster = RasterRenderer()
    vector = VectorRenderer()
    circle = Circle(raster, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()