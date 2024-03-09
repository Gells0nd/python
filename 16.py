# Напишите программу, которая будет запрашивать у пользователя радиус и сохранять его в переменной r. После этого она должна вычислить площадь круга с заданным радиусом и объем шара с тем же радиусом. Используйте в своих вычислениях константу pi из модуля math.

from math import pi

radius = float(input('[~] Введите радиус: '))

circle_S = pi * (radius**2)
circle_V = (4 / 3) * pi * (radius**3)

print(f'[+] Площадь круга: {circle_S}')
print(f'[+] Объем круга: {circle_V}')
