# Программа, которую вы напишете, должна начинаться с запроса у пользователя суммы заказа в ресторане. После этого должен быть произведен
# расчет налога и  чаевых официанту. Вы можете использовать принятую
# в вашем регионе налоговую ставку для подсчета суммы сборов. В качестве
# чаевых мы оставим 18 % от стоимости заказа без учета налога. На выходе программа должна отобразить отдельно налог, сумму чаевых и итог,
# включая обе составляющие. Форматируйте вывод таким образом, чтобы
# все числа отображались с двумя знаками после запятой.

price = int(input('[~] Введите сумму вашего заказа: '))

tea_money = price * 0.18
nds = price * 0.20

result = price + tea_money + nds

print(f'[~] Вы должны заплатить: {result}р')
