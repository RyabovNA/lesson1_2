first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second and second == third:
    print('Количество одинаковых чисел среди 3-х введённых: 3')
elif first == second != third or first == third != second or second == third != first:
    print('Количество одинаковых чисел среди 3-х введённых: 2')
elif first != second != third:
    print('Количество одинаковых чисел среди 3-х введённых: 0')