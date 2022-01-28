"""
Пробежки по Манхэттену
"""
def extend(rect, d):
	min_plus, max_plus, min_minus, max_minus = rect
	return min_plus - d, max_plus + d, min_minus - d, max_minus + d

def intersect(a, b):
	return max(a[0], b[0]), min(a[1], b[1]), max(a[2], b[2]), min(a[3], b[3])


t, d, n = map(int, input().split())
pos_rect = (0, 0, 0, 0)

for _ in range(n):
	x, y = map(int, input().split())
	pos_rect = extend(pos_rect, t)
	nav_rect = extend((x + y, x + y, x - y, x - y), d)
	pos_rect = intersect(pos_rect, nav_rect)

points = []
for x_p_y in range(pos_rect[0], pos_rect[1] + 1):
	for x_m_y in range(pos_rect[2], pos_rect[3] + 1):
		if (x_p_y + x_m_y) % 2 == 0:
			x = (x_p_y + x_m_y) // 2
			y = x_p_y - x
			points.append((x, y))

print(len(points))
for p in points:
	print(*p)