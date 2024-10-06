# Сегодня в N часов M минут хозяин магазина заказал доставку нового товара.
# Оператор сказал, что продукты доставят через T минут. Сколько будет времени на
# электронных часах, когда привезут долгожданные продукты?

# Формат ввода
# В первой строке записано натуральное число N (0 <= N < 24).
# Во второй строке записано натуральное число M (0 <= M < 60).
# В третьей строке записано натуральное число T (30 <= T < 10^6).

# Формат вывода
# Одна строка, представляющая циферблат электронных часов.

# Example 1
# Input   Output
#     8       09:05
#     0
#     65

starting_hours = int(input())
starting_minutes = int(input())
wait_all = int(input())

wait_hours = wait_all // 60
wait_minutes = (wait_all % 60) + starting_minutes

final_hours = (starting_hours + wait_hours + (wait_minutes // 60)) % 24
final_minutes = wait_minutes % 60

print(f"{final_hours:0>2}:{final_minutes:0>2}")
