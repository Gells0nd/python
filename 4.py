# Создайте программу, запрашивающую у  пользователя длину и  ширину
# садового участка в футах. Выведите на экран площадь участка в акрах.

# Подсказка. В одном акре содержится 43 560 квадратных футов.

length = float(input("Введите длину участка в футах: "))
width = float(input("Введите ширину участка в футах: "))

area_in_square_feet = length * width

square_feet_in_acre = 43560

area_in_acres = area_in_square_feet / square_feet_in_acre

print(f"Площадь участка в акрах: {area_in_acres}")