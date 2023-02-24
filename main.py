# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = int(input("Введите трёхзначное число: "))
num=number
summ = 0
while num > 0:
    result = num % 10
    summ = summ + result
    num = num//10

print("Сумма цифр числа", number, "=", summ, "(",int(number /100) % 10,"+",int(number /10) % 10,"+",number % 10,")")