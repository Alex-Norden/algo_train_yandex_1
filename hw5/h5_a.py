"""
Стильная одежда

Помогите Глебу выбрать одну майку и одни штаны так, чтобы разница в их цвете была как можно меньше
Если вариантов выбора несколько, выведите любой из них
"""
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

delta2inds = {}

i = j = 0
i_last = n - 1
j_last = m - 1

while i < i_last or j < j_last:
	if i < i_last and (a[i] < b[j] or j==j_last):
		i += 1
	else:
		j += 1
	delta2inds[abs(a[i] - b[j])] = (i, j)

min_delta = min(delta2inds.keys())
i, j = delta2inds[min_delta]
print(a[i], b[j])