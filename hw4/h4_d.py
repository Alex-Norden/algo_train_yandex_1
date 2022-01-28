"""
Клавиатура

Требуется написать программу, определяющую, какие клавиши
сломаются в процессе заданного варианта эксплуатации клавиатуры.
"""
from collections import Counter


n = int(input())
c = list(map(int, input().split()))
k = int(input())
p = map(int, input().split())
counter = Counter(p)

for i in range(n):
	# lim = c[i]
	if c[i] < counter[i + 1]:
		print("YES") #crushed
	else:
		print("NO")


# print(c)
# print(counter)