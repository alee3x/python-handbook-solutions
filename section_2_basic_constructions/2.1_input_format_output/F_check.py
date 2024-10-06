tovar = input()
price = int(input())
mass = int(input())
money = int(input())

print(f"Чек\n{tovar} - {mass}кг - {price}руб/кг")
print(f"Итого: {price * mass}руб\nВнесено: {money}руб")
print(f"Сдача: {money - price * mass}руб")

