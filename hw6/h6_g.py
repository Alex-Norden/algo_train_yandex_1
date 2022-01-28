"""
Площадь

Определите максимальную ширину дорожки, которую можно выложить из имеющихся плиток
"""
n = int(input())
m = int(input())
t = int(input())

def rbinsearch():
	nm = n * m
	l = -1
	r = min(n, m) // 2 + 1
	while r - l > 1:
		mid = (l + r) // 2
		w2 = mid*2
		s = (n - w2)*(m - w2) #площадь клумбы
		if nm - s <= t:
			l = mid
		else:
			r = mid

	return l if l > -1 else 0

print(rbinsearch())

"""
используем правый бинпоиск для поиска макс. ширины дорожки
израсходовать можно не более T плиток, значит площадь дорожек <= T
"""