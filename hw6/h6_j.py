"""
Медиана объединения

Напишите программу, которая для каждой пары последовательностей
выведет левую медиану их объединения
"""
n, l = map(int, input().split())
seqs = tuple(tuple(map(int, input().split())) for _ in range(n))

def median(a, b): #like merge
	last = None
	i = j = 0
	for _ in range(l):
		if i < l and (j == l or a[i] < b[j]):
			last = a[i]
			i += 1
		else:
			last = b[j]
			j += 1
	return last

for i in range(n - 1):
	for j in range(i + 1, n):
		print(median(seqs[i], seqs[j]))

"""
сливаем две посл-ти до L (дальше не нужно, т.к. медиана найдена)
"""