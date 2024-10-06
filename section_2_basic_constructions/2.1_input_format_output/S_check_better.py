# Формат ввода
#     Название товара;
#     цена товара;
#     вес товара;
#     количество денег у пользователя.

# Формат вывода
#
#     Красивый чек в формате:
#
#             ================Чек================
#             Товар:                    <продукт>
#             Цена:     <число>кг * <число>руб/кг
#             Итого:                   <число>руб
#             Внесено:                 <число>руб
#             Сдача:                   <число>руб
#             ===================================

nametag = input()
price = int(input())
mass = int(input())
given = int(input())

price_str = str(mass) + "кг" + " * " + str(price) + "руб/кг"
itogo_str = str(mass * price) + "руб"
vneseno_str = str(given) + "руб"
sdacha_str = str(given - mass * price) + "руб"
check = "Чек"

print(f"{check:=^35}")
print(f"Товар:{nametag: >29}")
print(f"Цена:{price_str: >30}")
print(f"Итого:{itogo_str: >29}")
print(f"Внесено:{vneseno_str: >27}")
print(f"Сдача:{sdacha_str: >29}")
print("=" * 35)
