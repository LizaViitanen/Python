print("Задание №4")
n = int(input("Введите любое положительное число: "))
a = n % 10
maks = a
n = n // 10
while a != 0:
    n = n // 10
    a = n % 10
    if maks < a:
        maks = a
print(f"Самая большая цифра в вашем числе: {maks}")