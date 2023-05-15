import Figure as f

c = f.Circle(50, 50, 100)
c.drawing_figure('#FF0000', '#00FF00')
print(f'Площадь круга: {c.get_area()}')
print(f'Периметр круга: {c.get_perimetr()}')

s = f.Square(0, 0, 50)
s.drawing_figure('#FF0F00', '#FF00F0')
print(f'Площадь квадрата: {s.get_area()}')
print(f'Периметр квадрата: {s.get_perimetr()}')

r = f.Rectangle(120, 120, 80, 40)
r.drawing_figure('#AA0F36', '#235723')
print(f'Площадь прямоугольника: {r.get_area()}')
print(f'Периметр прямоугольника: {r.get_perimetr()}')

t = f.Triangle(-20, -20, 12, 9, 180)
t.drawing_figure('#742592', '#8F8A54')
print(f'Площадь треугольника: {t.get_area()}')
print(f'Периметр треугольника: {t.get_perimetr()}')

p = f.Pentagon(-40, -120, 40)
p.drawing_figure('#861249', '#FFAA09')
print(f'Площадь пятиугольника: {p.get_area()}')
print(f'Периметр пятиугольника: {p.get_perimetr()}')

h = f.Hexagon(120, -50, 60)
h.drawing_figure('#123456', '#789ABC')
print(f'Площадь шестиугольника: {h.get_area()}')
print(f'Периметр шестиугольника: {h.get_perimetr()}')

e = f.Elipse(-150, -70, 45, 20)
e.drawing_figure('#9876AF', '#AF6798')
print(f'Площадь эллипса: {e.get_area()}')
print(f'Периметр эллипса: {e.get_perimetr()}')

ss = f.ScreenSettings()
ss.set_screen_opened()