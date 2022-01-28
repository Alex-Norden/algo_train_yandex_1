"""
Кассы

На одном из московских вокзалов билеты продают N касс.
Каждая касса работает без перерыва определенный промежуток
времени по фиксированному расписанию (одному и тому же каждый день)

Определить, на протяжении какого времени в течение суток работают все кассы одновременно
"""
OPEN, CLOSE = (1, 2)

def to_minutes(h, m):
	return h*60 + m

n = int(input())
e = []
for _ in range(n):
	h1, m1, h2, m2 = map(int, input().split())
	topen = to_minutes(h1, m1)
	tclose = to_minutes(h2, m2)
	if topen >= tclose:
		e.append((0, OPEN))
		e.append((1440, CLOSE))

	e.append((topen, OPEN))
	e.append((tclose, CLOSE))

len_events = len(e)
e.sort()
c_kass = 0
t_minutes = 0

for i in range(len_events):
	# print(f"{c_kass=}")
	if c_kass == n:
		t_minutes += e[i][0] - e[i - 1][0]
	type_e = e[i][1]
	if type_e == OPEN:
		c_kass += 1
	else:
		c_kass -= 1

print(t_minutes)

"""
разрезаем отрезки проходящие через полночь на 2
"смотрим на пред. промежуток"
если кол-во открытых касс было равно общему кол-ву, добавляем этот промежуток
"""