"""
Расстановка ноутбуков

Определите, какие размеры должен иметь стол,
чтобы оба ноутбука на него поместились, и площадь стола была минимальна.
"""
def solution(a, b, c, d):
	if b > a:
		a, b = b, a

	if d > c:
		c, d = d, c

	if c > a:
		a, b, c, d = c, d, a, b

	side11 = a
	side12 = (b + d)
	s1 = side11 * side12

	side21 = max(b, c)
	side22 = (a + d)
	s2 = side21 * side22

	if s1 < s2:
		return side11, side12
	else:
		return side21, side22


a, b, c, d = map(int, input().strip().split())
res = solution(a, b, c, d)
print(" ".join(map(str, res)))