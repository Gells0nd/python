# Представьте, что вы пишете программное обеспечение для автоматической кассы в  магазине самообслуживания. Одной из функций, заложенных в кассу, должен быть расчет сдачи в случае оплаты покупателем наличными. Напишите программу, которая будет запрашивать у пользователя сумму сдачи в центах. После этого она должна рассчитать и вывести на экран, сколько и каких монет потребуется для выдачи указанной суммы, при условии что должно быть задействовано минимально возможное количество монет. Допустим, у нас есть в распоряжении монеты достоинством в 1, 5, 10, 25 центов, а также в 1 (loonie) и 2 (toonie) канадских доллара.

def calculate_change(amount_in_cents):
    coins = {
        200: "toonies",
        100: "loonies",
        25: "quarters",
        10: "dimes",
        5: "nickels",
        1: "pennies"
    }

    change = {}
    for coin_value in sorted(coins.keys(), reverse=True):
        num_coins = amount_in_cents // coin_value
        if num_coins > 0:
            change[coins[coin_value]] = num_coins
            amount_in_cents -= num_coins * coin_value

    return change


def main():
    while True:
        try:
            amount_in_cents = int(input("[~] Введите сумму сдачи в центах: "))
            if amount_in_cents < 0:
                print("[!] Сумма не может быть отрицательной.")
                continue
            break
        except ValueError:
            print("[!] Пожалуйста, введите целое число.")

    change = calculate_change(amount_in_cents)
    print(f"[~] Для выдачи суммы в {amount_in_cents} центов потребуется:")
    for coin, count in change.items():
        print(f"{coin}: {count}")


if __name__ == "__main__":
    main()
