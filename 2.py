print("Задание №2")
a = int(input("Введите время в секундах, а мы переведем это в часы (в формате ЧЧ:ММ:СС): "))
if a >= 3600:
    hour = a // 3600
    if hour < 10:
        hour = "0" + str(hour)
    b = a % 3600
    m = b // 60
    if m < 10:
        m = "0" + str(m)
    sec = b % 60
    if sec < 10:
        sec = "0" + str(sec)
    print(f" {hour}:{m}:{sec}")
else:
    hour = '00'
    m = a // 60
    if m < 10:
        m = "0" + str(m)
    sec = a % 60
    if sec < 10:
        sec = "0" + str(sec)
    print(f" {hour}:{m}:{sec}")