# 2023/09/20 00:00|Строки и Индексация строк.
name = 'Andrey'
print('Hello, ' + name + '!')
print('Hello' * 5)
print(name[0])  # Первый элемент имеет № "0"
print(name[-1])  # индексация поддерживает и отрицательные значения
#  "-1" - вывести последний символ
#  [0:0:0] может иметь 3 элемента, 1 обязателен
print(name[0:3])  # разделили строку на 2 части
# вывели первые 3 элемента (с 1 по 3)
print(name[0:3:2])  # вывести 3 элемента с шагом 2
print(name[:3])  # с начала до 3
print(name[2:])  # со 2 до конца
print(name[::-1])  # Вывести все элементы с шагом -1, т.е. в обратном порядке
