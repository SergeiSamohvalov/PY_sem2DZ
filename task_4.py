# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

# finp = open('file.txt','w')
# while True:
#     if s=="":
#         break
# finp.write(s+"\n")
# finp.close()


import random

workpoz = 1
n = int(input('Задайте колличество элементов: '))
list = []
for i in range(0, n):
    num = random.randint(n * -1, n)
    list.append(num)
print(f'Выводим получившийся список \n{list}')
poz = input('Задайте номера позиций элементов через пробел(нумерация от 0 до n-1): ') 
for i in range(0, len(poz.split(' '))):
    a = int(poz.split(' ')[i])
    workpoz *= list[a]
print(f'Произведение элементов на заданных позициях: {workpoz}')