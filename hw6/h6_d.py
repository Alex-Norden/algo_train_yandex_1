"""
Космическое поселение

Написать программу, которая по заданным количеству и размеру модулей,
а также размеру поля для их размещения, определяет максимальную толщину
слоя дополнительной защиты, который можно добавить к каждому модулю
"""
n, a, b, w, h = map(int, input().split())

def rbinsearch():
	def check(side1, side2, s_ab):
		c1 = w // side1
		c2 = h // side2
		count_ab = c1 * c2
		return count_ab >= n and count_ab * s_ab <= s_wh

	s_wh = w * h

	l = -1
	# r = max((w//n - a)//2, (h//n - b)//2) + 10
	r = max(w, h) + 1

	while r - l > 1:
		m = (l + r) // 2 #значение толщины (d)

		d2 = m*2
		side_a = a + d2
		side_b = b + d2
		s_ab = side_a * side_b

		success = check(side_a, side_b, s_ab)
		if not success:
			success = check(side_b, side_a, s_ab)

		if success:
			l = m
		else:
			r = m

	# print(f"{l=}")
	if l > -1:
		return l
	return 0

print(rbinsearch())

"""
используем правый бинпоиск для поиска макс. толщины защиты

проверим, что влезает модулей не меньше, чем д.б
и что они занимают площадь не больше, чем должны

если не влазят, попробуем повернуть
"""