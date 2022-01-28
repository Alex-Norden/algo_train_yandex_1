"""
Пересечение множеств

Даны два списка чисел, которые могут содержать до 10000 чисел каждый.
Выведите все числа, которые входят как в первый, так и во второй список в порядке возрастания.
Примечание. И даже эту задачу на Питоне можно решить в одну строчку.
"""
def sol(a, b):
	intersec = set(a).intersection(set(b))
	print(*sorted(intersec))


a = list(map(int, input().split()))
b = list(map(int, input().split()))

sol(a, b)