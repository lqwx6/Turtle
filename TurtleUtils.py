from re import match
import FigureExceptions as fe

class TurtleHepler:
    def __init__(self, t):
        self.t = t

    def set_screensize(self, x:int=400, y:int=400):
        self.t.screensize(x, y)

    def set_coords(self, x, y):
        if self.t.heading() != 0: self.t.left(self.t.heading() * -1)
        self.t.pu()
        self.t.setx(x)
        self.t.sety(y)
        self.t.pd()
    
    def set_color(self, line_color:str, fill_color:str):
        if not isinstance(line_color, str) or not isinstance(fill_color, str):
            raise fe.FigureDatatypeError('The color can only be specified in six-digit HEX format')
        r1 = match('^#[0-9aA-fF]{6}$', line_color)
        r2 = match('^#[0-9aA-fF]{6}$', fill_color)
        if r1 is None or r2 is None: raise fe.FigureColorFormatError('Color entered incorrectly')
        self.t.fillcolor(fill_color)
        self.t.pencolor(line_color)

    def check_figure_arguments(self, x, y, *sizes):
        if not isinstance(x, int) or not isinstance(y, int):
            raise fe.FigureDatatypeError('The coordinate data type can only be int')
        for size in sizes:
            if not isinstance(size, (int, float)):
                raise fe.FigureDatatypeError('The size of the figure can only be int or float')
            if size <= 0:
                raise fe.FigureSizeError('The size of the figure must be greater than zero')
    
    def set_screen_opened(self):
        self.t.exitonclick()