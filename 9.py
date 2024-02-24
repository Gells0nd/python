# Представьте, что вы открыли в банке сберегательный счет под 4 % годовых. Проценты банк рассчитывает в конце года и добавляет к сумме счета. Напишите программу, которая запрашивает у пользователя сумму перво-начального депозита, после чего рассчитывает и выводит на экран сумму на счету в конце первого, второго и третьего годов. Все суммы должны быть округлены до двух знаков после запятой.

sum = 1_000_000

for i in range(1, 11):
	sum = sum + sum * 0.04
	print(f'[!] Текущий год: {i}\t|\tСумма вклада на данный год: {round(sum, 2)}')

print(f'\n[!] Сумма на момент окончания вклада: {round(sum, 2)}')