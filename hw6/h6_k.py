"""
Медиана объединения-2

Напишите программу, которая для каждой пары последовательностей
выведет левую медиану их объединения
"""
def gen_seq(l, x1, d1, a, c, m):
	s = [x1]*l
	d = d1
	for i in range(1, l):
		s[i] = s[i - 1] + d
		d = (a * d + c) % m
	return s

def lbinsearch(l, r, check, params):
	while r - l > 1:
		m = (l + r) // 2
		if check(m, *params):
			r = m
		else:
			l = m
	return r

def is_ge(i, s, x):
	return s[i] >= x

# def is_gt(i, s, x):
# 	return s[i] > x

def count_less(s, x):
	return lbinsearch(-1, len(s), is_ge, (s, x))

def median_merge(s1, s2): #like rbinsearch
	len_s1 = len(s1)
	l = min(s1[0], s2[0]) - 1
	r = max(s1[-1], s2[-1]) + 1
	while r - l > 1:
		m = (l + r) // 2
		c_less = count_less(s1, m) + count_less(s2, m)
		if c_less < len_s1: #<= L-1
			l = m
		else:
			r = m
	return l

n, l = map(int, input().split())

seqs = [gen_seq(l, *map(int, input().split())) for _ in range(n)]

for i in range(n):
	for j in range(i + 1, n):
		print(median_merge(seqs[i], seqs[j]))

"""
будем максимизировать count_less(X) (счётчик элементов меньших X)
для поиска медианы используем правый бинпоиск по ответу
медиана нах-ся на позиции L, т.е. кол-во элементов слева <= L-1 (индексация с 0)

для подсчёта кол-ва элементов слева (меньших медианы) будем использовать левый бинпоиск
с условием is_ge()
если правая граница не сдвинется, то значит все элементы больше X
"""