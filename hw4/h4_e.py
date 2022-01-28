"""
Пирамида

По заданному набору блоков определите,
пирамиду какой наибольшей высоты можно построить из них.
"""
n = int(input())

a = [tuple(map(int, input().split())) for _ in range(n)]

a.sort()
max_h = a[0][1]
s = 0

for i in range(1, n):
	w, h = a[i]
	if w > a[i - 1][0]:
		s += max_h
		max_h = h
	elif h > max_h:
		max_h = h

s += max_h
print(s)