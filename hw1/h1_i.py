"""
Узник замка Иф

Определите, сможет ли узник выбрасывать кирпичи в море через это отверстие,
если стороны кирпича должны быть параллельны сторонам отверстия
"""
def read_int():
	return int(input())

def print_solution(a, b, c, d, e):
	a, b, c = sorted((a,b,c))
	if d > e:
		d, e = e, d

	if a <= d and b <= e:
		print("YES")
	else:
		print("NO")


a = read_int()
b = read_int()
c = read_int()
d = read_int()
e = read_int()

print_solution(a, b, c, d, e)