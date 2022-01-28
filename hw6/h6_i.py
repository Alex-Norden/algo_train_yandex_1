"""
Субботник

Выведите одно число — наименьше возможное значение
максимального числа неудобства сформированных бригад
"""
n, brig, c = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort()

def lbinsearch():
	def check(m):
		i = 0
		n_brig = 0
		while i < n - c + 1:
			if a[i + c - 1] - a[i] <= m:
				n_brig += 1
				i += c
			else:
				i += 1
		return n_brig >= brig

	l = -1
	r = a[n - 1] - a[0] + 1 #максимальное неудобство (разница в росте)
	while r - l > 1:
		m = (l + r) // 2
		if check(m):
			r = m
		else:
			l = m
	return r

print(lbinsearch())

"""
используем левый бинпоиск по ответу (число неудобства)
проверяем удалось ли сформировать требуемое кол-во бригад по С человек
"""