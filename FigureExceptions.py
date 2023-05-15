class FigureError(BaseException):
    pass

class FigureDatatypeError(FigureError):
    def __init__(self, message):
        self.message = message

class FigureSizeError(FigureError):
    def __init__(self, message):
        self.message = message

class FigureColorError(FigureError):
    pass

class FigureColorFormatError(FigureColorError):
    def __init__(self, message):
        self.message = message

class FigureMathematicalError(FigureError):
    pass

class FigureAngleError(FigureMathematicalError):
    def __init__(self, message):
        self.message = message