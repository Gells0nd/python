# Как известно, поверхность планеты Земля искривлена, и расстояние между точками, характеризующимися одинаковыми градусами по долготе,
# может быть разным в зависимости от широты. Таким образом, для вычисления расстояния между двумя точками на Земле одной лишь теоремой Пифагора не обойтись. Допустим, (t1, g1) и (t2, g2) – координаты широты и долготы двух точек на поверхности Земли. Тогда расстояние в километрах между ними с учетом искривленности планеты можно найти по следующей формуле:

# distance = 6371,01 * arccos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1 - g2)).

# Примечание. Число 6371,01 в этой формуле, конечно, было выбрано не случайно
# и представляет собой среднее значение радиуса Земли в километрах.

# Напишите программу, в которой пользователь будет вводить координаты двух точек на Земле (широту и долготу) в градусах. На выходе мы
# должны получить расстояние между этими точками при следовании по
# кратчайшему пути по поверхности планеты.

# Подсказка. Тригонометрические функции в  Python оперируют радианами. Таким образом, вам придется введенные пользователем величины из градусов перевести в радианы, прежде чем вычислять расстояние между точками. В модуле math есть удобная функция с названием radians-Функции:radians, служащая как раз для перевода градусов в радианы.

from math import radians, cos, acos, sin

t1 = float(input('[~] Ширина 1: '))
t2 = float(input('[~] Долгота 1: '))

print('---------')

g1 = float(input('[~] Ширина 2: '))
g2 = float(input('[~] Долгота 2: '))

t1, t2, g1, g2 = radians(t1), radians(t2), radians(g1), radians(g2)

result = 6371 * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1 - g2))

print(f'[!] Расстояние между 2 точками: {result}км')