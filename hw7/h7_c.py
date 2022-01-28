"""
Рассадка в аудитории

Какое наименьшее количество типов билетов должен подготовить преподаватель,
чтобы никакие два студента с одинаковыми билетами не могли разговаривать?
Выведите способ раздачи преподавателем билетов
"""
n, d = map(int, input().split())
x = tuple(map(int, input().split()))

CAN, NOT_CAN = (1, 2) #может разговаривать/нет

events = []
for xi in x:
	events.append((xi, CAN))
	events.append((xi + d, NOT_CAN))

events.sort()

max_count = count = 0

for _, type_e in events:
	if type_e == CAN:
		count += 1
		if count > max_count:
			max_count = count
	else:
		count -= 1

x2var = {}
num_variant = 1

for xi, type_e in events:
	if type_e == CAN:
		x2var[xi] = num_variant

		if num_variant < max_count:
			num_variant += 1
		else:
			num_variant = 1

print(max_count)
ans = (x2var[xi] for xi in x)
print(*ans)