import turtle, math
import TurtleUtils
from FigureExceptions import FigureAngleError
t = turtle
tu = TurtleUtils.TurtleHepler(t)
tu.set_screensize()

class Circle:
    def __init__(self, x:int, y:int, d:float|int):
        self.x = x
        self.y = y
        self.d = d

        tu.check_figure_arguments(self.x, self.y, self.d)

    def get_area(self):
        return math.pi * (self.d/2)**2
    
    def get_perimetr(self):
        return 2 * math.pi * (self.d/2)
    
    def drawing_figure(self, line_color:str, fill_color:str):
        tu.set_coords(self.x, self.y)
        tu.set_color(line_color, fill_color)
        t.begin_fill()
        t.circle(self.d/2)
        t.end_fill()

class Square:
    def __init__(self, x:int, y:int, size:int|float):
        self.x = x
        self.y = y
        self.size = size

        tu.check_figure_arguments(self.x, self.y, self.size)

    def get_area(self):
        return self.size ** 2
    
    def get_perimetr(self):
        return 4 * self.size
    
    def drawing_figure(self, line_color:str, fill_color:str):
        tu.set_coords(self.x, self.y)
        tu.set_color(line_color, fill_color)
        t.begin_fill()
        for i in range(4):
            t.forward(self.size)
            t.left(90)
        t.end_fill()
    
class Rectangle:
    def __init__(self, x:int, y:int, size_x:int|float, size_y:int|float):
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y

        tu.check_figure_arguments(self.x, self.y, self.size_x, self.size_y)
    
    def get_area(self):
        return self.size_x * self.size_y
    
    def get_perimetr(self):
        return 2*(self.size_x + self.size_y)
    
    def drawing_figure(self, line_color:str, fill_color:str):
        tu.set_coords(self.x, self.y)
        tu.set_color(line_color, fill_color)
        t.begin_fill()
        for i in range(4):
            t.forward(self.size_x) if i % 2 == 0 else t.forward(self.size_y)
            t.left(90)
        t.end_fill()

class Triangle:
    def __init__(self, x:int, y:int, size_a:int|float, size_b:int|float, angle:int|float):
        self.x = x
        self.y = y
        self.size_a = size_a
        self.size_b = size_b
        self.angle = angle

        tu.check_figure_arguments(self.x, self.y, self.size_a, self.size_b)
        if self.angle > 179:
            raise FigureAngleError('The angle between the sides should be less than 180 degrees')
        self.__size_c = math.sqrt(self.size_a ** 2 + self.size_b ** 2 - 2 * self.size_a * self.size_b * math.cos(math.radians(self.angle)))
        self.__angels = 180 - math.degrees(math.acos((self.size_b ** 2 + self.__size_c ** 2 - self.size_a ** 2) / (2 * self.size_b * self.__size_c)))
        
    def get_area(self):
        return 0.5 * self.size_a * self.size_b * math.sin(math.radians(self.angle))
    
    def get_perimetr(self):
        return self.size_a + self.size_b + self.__size_c

    def drawing_figure(self, line_color:str, fill_color:str):
        tu.set_coords(self.x, self.y)
        tu.set_color(line_color, fill_color)
        t.begin_fill()
        t.forward(self.size_a)
        t.left(180 - self.angle)
        t.forward(self.size_b)
        t.left(self.__angels)
        t.forward(self.__size_c)
        t.end_fill()

class Pentagon:
    def __init__(self, x:int, y:int, side:int|float):
        self.x = x
        self.y = y
        self.side = side

        tu.check_figure_arguments(self.x, self.y, self.side)
        self.__angels = 360 / 5

    def get_area(self):
        return ((self.side ** 2) * 5) / (4 * (math.tan(math.pi / 5)))
    
    def get_perimetr(self):
        return self.side * 5
    
    def drawing_figure(self, line_color:str, fill_color:str):
        tu.set_coords(self.x, self.y)
        tu.set_color(line_color, fill_color)
        t.begin_fill()
        for i in range(5):
            t.forward(self.side)
            t.left(self.__angels)
        t.end_fill()

class Hexagon:
    def __init__(self, x:int, y:int, side:int|float):
        self.x = x
        self.y = y
        self.side = side

        tu.check_figure_arguments(self.x, self.y, self.side)
        self.__angels = 360 / 6
    
    def get_area(self):
        return (3 * math.sqrt(3) * self.side ** 2) / 2
    
    def get_perimetr(self):
        return self.side * 6
    
    def drawing_figure(self, line_color:str, fill_color:str):
        tu.set_coords(self.x, self.y)
        tu.set_color(line_color, fill_color)
        t.begin_fill()
        for i in range(6):
            t.forward(self.side)
            t.left(self.__angels)
        t.end_fill()

class Elipse:
    def __init__(self, x:int, y:int, r1:int|float, r2:int|float):
        self.x = x
        self.y = y
        self.r1 = r1
        self.r2 = r2

        tu.check_figure_arguments(self.x, self.y, self.r1, self.r2)

    def get_area(self):
        return math.pi * self.r1 * self.r2
    
    def get_perimetr(self):
        self.__h = ((self.r1 - self.r2) / (self.r1 + self.r2)) ** 2
        return math.pi * (self.r1 + self.r2) * (1 + (3 * self.__h) / (10 + math.sqrt(4 - 3 * self.__h)))
    
    def drawing_figure(self, line_color:str, fill_color:str):
        tu.set_coords(self.x, self.y)
        tu.set_color(line_color, fill_color)
        t.begin_fill()
        t.circle(self.r1, 45)
        t.circle(self.r2, 90)
        t.circle(self.r1, 90)
        t.circle(self.r2, 90)
        t.circle(self.r1, 45)
        t.end_fill()
    
class ScreenSettings:
    def __init__(self):
        pass

    def set_screen_opened(self):
        tu.set_screen_opened()