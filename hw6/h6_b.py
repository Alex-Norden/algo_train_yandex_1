"""
Приближенный двоичный поиск

Для каждого из чисел второй последовательности найдите ближайшее к нему в первой
"""

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def delta(x1, x2):
	if x1 > x2:
		return x1 - x2
	return x2 - x1

def lbinsearch(x):
	l = -1
	r = n
	while r - l > 1:
		m = (l + r) // 2
		if a[m] >= x:
			r = m
		else:
			l = m
	if r < n:
		return r

def rbinsearch(x):
	l = -1
	r = n
	while r - l > 1:
		m = (l + r) // 2
		if a[m] <= x:
			l = m
		else:
			r = m
	if l > -1:
		return l

def binsearch(x):
	"""
	L___R
	"""
	l = rbinsearch(x)
	r = lbinsearch(x)

	if l is None:
		return r
	elif r is None:
		return l
	else:
		if delta(a[l], x) > delta(a[r], x):
			return r
		else:
			return l

for x in b:
	i = binsearch(x)
	print(a[i])
