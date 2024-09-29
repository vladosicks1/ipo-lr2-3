import math
x = float(input('Введите объем шара: '))

v = pow(x, 1/3)
r = 3*v/(4*math.pi)

print("Радиус равен:",r)