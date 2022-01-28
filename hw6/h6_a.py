"""
Двоичный поиск

Требуется для каждого из K чисел вывести в отдельную строку "YES",
если это число встречается в первом массиве, и "NO" в противном случае
"""
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def binsearch(x):
	l = -1
	r = n
	while r - l > 1:
		m = (l + r) // 2
		if a[m] == x:
			return True
		elif a[m] > x:
			r = m
		else:
			l = m

for x in b:
	if binsearch(x):
		print("YES")
	else:
		print("NO")