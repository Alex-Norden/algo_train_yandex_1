"""
НГУ-стройка

Написать программу, которая позволяет выбрать минимальное число блоков,
которые, будучи установленными на указанных подрядчиками местах,
образуют перекрытие, либо определить, что этого сделать невозможно.
Высота, на которой образуется перекрытие, не имеет значения.

*Два блока можно склеить, если они соприкасаются перекрывающимися
частями боковых граней ненулевой площади
"""
OUT, IN = (1, 2)

n, w, l = map(int, input().split())

events = []
for i_block in range(1, n + 1):
	x1, y1, z1, x2, y2, z2 = map(int, input().split())
	if z1 > z2:
		t = z1
		z1 = z2
		z2 = t

	xy_area = abs(x2 - x1) * abs(y2 - y1)

	events.append((z1, IN, xy_area, i_block))
	events.append((z2, OUT, xy_area, i_block))

events.sort()

total_area = w*l
area = 0
# width_overlap = 0

min_count = n + 1
count = 0

for _, type_e, xy_area, _ in events:
	if type_e == IN:
		count += 1
		area += xy_area
	else:
		count -= 1
		area -= xy_area

	if area == total_area and count < min_count:
		min_count = count

if min_count == (n + 1):
	print("NO")
else:
	print("YES")
	print(min_count)

	block_inds = set()

	for _, type_e, xy_area, i_block in events:
		if type_e == IN:
			count += 1
			area += xy_area
			block_inds.add(i_block)
		else:
			count -= 1
			area -= xy_area
			block_inds.remove(i_block)

		if area == total_area and count == min_count:
			break

	print(*sorted(block_inds))


# print(f"{total_area=}")
# print(f"{min_count=}")

"""
чтобы исключить перекрытия нулевой толщины, сначала OUT, затем IN

p1 ближе к O, чем p2

сначала находим, когда достигается условие
потом восстанавливаем ответ
"""