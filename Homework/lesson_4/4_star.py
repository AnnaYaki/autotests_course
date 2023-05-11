# Задача со ЗВЁЗДОЧКОЙ. Решать НЕ обязательно.
# Программа получает на вход натуральное число num.
# Программа должна вывести другое натуральное число, удовлетворяющее условиям:
# Новое число должно отличаться от данного ровно одной цифрой
# Новое число должно столько же знаков как исходное
# Новое число должно делиться на 3
# Новое число должно быть максимально возможным из всех таких чисел
# Например (Ввод --> Вывод) :
#
# 379 --> 879
# 15 --> 75
# 4974 --> 7974

def max_division_by_3(num):
    # Здесь нужно написать код
    arr = []
    new_num = 0
    mun = num
    while num > 0:
        arr.append(num % 10)
        num = num // 10
    dlina = len(arr)
    new_arr = []
    for i in range(dlina):
        new_arr.append(9)
    for i in new_arr:
        new_num = new_num * 10 + i

    arr_del3 = []
    for i in range(new_num):
        if i % 3 == 0:
            arr_del3.append(i)
    arr_znak = []
    for i in arr_del3:
        if i >= 10 ** (dlina - 1):
            arr_znak.append(i)
    povtor = dlina
    num = mun
    arr_itog = []
    gnom = 0
    for i in arr_znak:
        povtor = dlina
        gnom = 0
        while povtor > 0:
            x = str(i)
            y = str(num)
            if x[povtor - 1] == y[povtor - 1]:
                gnom += 1
            povtor = povtor - 1
        if gnom >= dlina - 1:
            arr_itog.append(i)
    new_num = max(arr_itog)

    return new_num

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    379, 810, 981, 4974, 996, 9000, 15, 0, 9881, 9984, 9876543210, 98795432109879543210
]

test_data = [
    879, 870, 987, 7974, 999, 9900, 75, 9, 9981, 9987, 9879543210, 98798432109879543210
]


for i, d in enumerate(data):
    assert max_division_by_3(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')