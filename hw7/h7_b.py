"""
Точки и отрезки

Дано n отрезков на числовой прямой и m точек на этой же прямой
Для каждой из данных точек определите, скольким отрезкам они принадлежат
Точка x считается принадлежащей отрезку с концами a и b,
если выполняется двойное неравенство min(a, b)≤ x ≤ max(a, b)
"""
BEGIN, POINT, END = (1, 2, 3)

n, m = map(int, input().split())
events = []
for _ in range(n):
	a, b = map(int, input().split())
	if a > b:
		a, b = b, a
	events.append((a, BEGIN))
	events.append((b, END))

points = tuple(map(int, input().split()))
for p in points:
	events.append((p, POINT))

events.sort()

p2count = {}
count = 0

for e in events:
	type_e = e[1]
	if type_e == BEGIN:
		count += 1
	elif type_e == END:
		count -= 1
	else:
		# ans.append(count)
		p2count[e[0]] = count

ans = (p2count[p] for p in points)
print(*ans)

"""
события из отрезков и точек
в начале/конце отрезка увел. счётчик отрезков
для точек выводим текущее значение счётчика (можно с помощью списка)

*событие POINT между BEGIN, END, т.к. границы включительно
*вывод точек в исх. порядке
"""