from enum import StrEnum
from importlib.util import find_spec

# binary_value = "1001"
# print(int(binary_value, 2))

# value = 7
# print(bin(value))
# bin()
# oct()
# hex()

# value = '100111101'
# print(int(value, 2))


# banknot = int(input("ВВедите натуральное число больше 100:"))
# print(f"{banknot - (int(2.5 * 38))}")

# name_item = str(input())
# price_by_kilometer = int(input())
# weight = int(input())
# money = int(input())
#
# total_price = price_by_kilometer * weight
# change = money - total_price
#
# print("Чек")
# print(f"{name_item} - {weight}кг - {price_by_kilometer}руб/кг")
# print(f"Итого: {total_price}руб")
# print(f"Внесено: {money}руб")
# print(f"Сдача: {change}руб")

# number = int(input())
# print("Купи слона!\n" * number)

# value = int(input())
# text = str(input())
#
# print(f'Я больше никогда не буду писать "{text}"\n' * value)


# name = str(input("Enter your name : "))
# number_of_box = int(input("Enter number of box : "))
#
# group = number_of_box // 100
# bed = number_of_box // 10 % 10
# num_of_baby = number_of_box % 10
#
#
# print(f"Группа №{group}.\n{num_of_baby}. {name}.\nШкафчик: {number_of_box}.\nКроватка: {bed}.")


# value = int(input())
#
# a = value // 1000
# b = value // 100 % 10
# c = value // 10 % 10
# d = value % 10
# print(f"{b}{a}{d}{c}")


# number_M = int(input())
# number_N = int(input())
#
# # единицы
# a = (number_M % 10 + number_N % 10) % 10
#
# # десятки
# b = ((number_M // 10) % 10 + (number_N // 10) % 10) % 10
#
# #сотни
# d = ((number_M // 100) + (number_N // 100)) % 10
#
# result = d * 100 + b * 10 + a
# print(result)

# N_children = int (input())
# M_candies = int(input())
#
#
# sum_of_candies_to_children = (M_candies // N_children)
# remaining = M_candies % N_children
#
# print(sum_of_candies_to_children)
# print(remaining)


# red = int(input())
# green = int(input())
# blue = int(input())
#
#
# steps_result = (red + blue) + 1
#
# print(steps_result)

# N = int(input())
# M = int(input())
# T= int(input())
#
# total_minutes = M + T
# added_hours = total_minutes // 60
#
# new_minutes = total_minutes % 60
#
# new_hours = (N + added_hours ) % 24
# print(f"{new_hours:02d}:{new_minutes:02d}")

# A = int(input())
# B = int(input())
# C = int(input())
#
# distance = abs(B - A)
#
# time = distance / C
#
#
# print(f"{time:.2f}")

# m = 12
# n = 19
# k = 25
#
# # максимальное число
# print(max(m, n, k))
#
# line_1 = "m"
# line_2 = "n"
# line_3 = "k"
#
# # минимальная лексикографически строка
# print(min(line_1, line_2, line_3))
#
# # количество цифр в числе 2 в степени 2022
# print(len(str(2 ** 2022)))

# decimal_num = int(input())
# binary_num = str(input())
#
# convertation = (int(binary_num, 2))
# total = decimal_num + convertation
# print(total)

# binary_price = str(input())
# currency = int(input())
#
#
# decimal_converter = int(binary_price, 2)
# change_total = currency - decimal_converter
#
#
# print(change_total)

# name_item = input()
# price_item = int(input())
# weight_item = int(input())
# money = int(input())
#
# total = price_item * weight_item
# change = money - total
# price_line = f"{weight_item}кг * {price_item}руб/кг"
#
# print("=" * 16 + "Чек" + "=" * 16)
# print(f"{'Товар:':<26}{name_item:>9}")
# print(f"{'Цена:':<21}{price_line:>14}")
# print(f"{'Итого:':<26}{str(total) + 'руб':>9}")
# print(f"{'Внесено:':<26}{str(money) + 'руб':>9}")
# print(f"{'Сдача:':<26}{str(change) + 'руб':>9}")
# print("=" * 35)

# N = int(input())
# M = int(input())
# K1 = int(input())
# K2 = int(input())
#
#
# x = N * (M - K2) // (K1 - K2)
#
# y = N - x
#
# print(x, y)

# -----------------------------------------------while For циклы -------------------------------------------------------

# yell = str(input())
#
# while yell != "Три!":
#     print("Режим ожидания...")
#     yell = str(input())
# print("Ёлочка, гори!")
#
#
# while (yell := str(input("цыфра "))) != "Три":
#     print("Режим ожидания...")
# print("Ёлочка, гори!")


# counter = 0
# while (name := str(input())) != "Приехали!":
#     if "зайка" in name.lower():
#         counter += 1
# print (counter)

# start = int(input())
# finish = int(input())

# for i in range(number1, number2 + 1):
#     print(i, end=" ")
#
# if start < finish:
#     for i in range(start, finish + 1):
#         print(i, end=' ')
# else:
#     for i in range(start, finish -1, -1):
#         print(i, end=' ')



# total = 0
#
# while (price := float(input())) != 0:
#     if price >= 500:
#         price *= 0.9
#     total += price
# print(total)

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

while b != 0:
    a, b = b, a % b
print(a)