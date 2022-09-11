# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

n = int(input('Введите значение n: '))
list = []
summa = 0 
for i in range(1, n + 1): 
    rez = ((1 + 1 / n)**n) 
    list.append(round(rez, 2))
print(f'Получившийся список чисел:\n{list}')
for i in range(0, len(list)):
    summa += list[i]
print(f'Сумма всего списка: {summa}')
