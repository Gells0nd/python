# Интернет-магазин занимается продажей различных сувениров и безде-лушек. Каждый сувенир весит 75 г, а безделушка – 112 г. Напишите программу, запрашивающую у пользователя количество тех и других покупок,
# после чего выведите на экран общий вес посылки.

first_item = int(input('[~] Сколько сувениров вы купили: '))
second_item = int(input('[~] Сколько безделушек вы купили: '))

weight = (first_item * 75) + (second_item * 112)

print(f'[!] Общий вес посылки: {weight / 1000}кг')