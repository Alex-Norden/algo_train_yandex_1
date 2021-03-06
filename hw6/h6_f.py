"""
Очень легкая задача

Помогите выяснить, какое минимальное время для этого потребуется
"""
n, x, y = map(int, input().split())

def lbinsearch():
	l = -1
	# r = n // (x + y) + 2
	r = n * max(x, y) + 1
	while r - l > 1:
		m = (l + r) // 2
		printed = m // x + m // y
		if printed >= n:
			r = m
		else:
			l = m
	return r

# делаем одну копию
n -= 1
total = min(x, y)

# печатаем дальше
total += lbinsearch()
print(total)

"""
используем левый бинпоиск по ответу для поиска мин. кол-ва секунд
для оценки правой границы предполагаем самый ХУДШИЙ случай (печать на одном долгом принтере)

чтобы использовать оба нужно как минимум 2 экземпляра
для этого нужно сделать копию на том, что быстрее печатает
и добавить это время к итоговому
"""