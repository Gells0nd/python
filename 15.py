# Для этого упражнения вам необходимо будет написать программу, которая будет запрашивать у пользователя расстояние в футах. После этого она должна будет пересчитать это число в дюймы, ярды, метры и мили и вывес­ти на экран. Коэффициенты для пересчета единиц вы без труда найдете в интернете.

foots = int(input('[~] Введите растояние в футах: '))

duims = foots / 0.08
yards = foots * 0.3
milles = foots * 0.0001
metters = foots * 0.3

print(f'[+] Дюймы: {duims}')
print(f'[+] Ярды: {yards}')
print(f'[+] Милли: {milles}')
print(f'[+] Метры: {metters}')

