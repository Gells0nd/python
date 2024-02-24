# Создайте программу, которая запрашивает у пользователя два целых чис- ла a и b, после чего выводит на экран результаты следующих математических операций:
#  сумма a и b;
#  разница между a и b;
#  произведение a и b;
#  частное от деления a на b;
#  остаток от деления a на b;
#  десятичный логарифм числа a;
#  результат возведения числа a в степень b.
# Подсказка. Функцию log10 вы найдете в модуле math.

import math

num1 = float(input('[~] Число A: '))
num2 = float(input('[~] Число B: '))

print(f'[+] Сумма: {num1 + num2}')
print(f'[+] Разница: {num1 - num2}')
print(f'[+] Произведение: {num1 * num2}')
print(f'[+] Частное от деления: {num1 // num2}')
print(f'[+] Остаток от деления: {num1 % num2}')
print(f'[+] Десятичный логорифм: {math.log10(num1)}')
print(f'[+] Результат возведения числа {num1} в степень {num2}: {num1**num2}')