# Сложение без переноса разрядов
# Пример:
# Ввод
#   405
#   839
# Вывод
#   234

# Все числа < 1000

N = int(input())
M = int(input())

M_hundreds = M // 100
N_hundreds = N // 100
M_decimals = (M // 10) % 10
N_decimals = (N // 10) % 10
M_units = M % 10
N_units = N % 10

ans = ((M_hundreds + N_hundreds) % 10) * 100
ans = ans + ((M_decimals + N_decimals) % 10) * 10
ans = ans + (M_units + N_units) % 10

print(ans)
