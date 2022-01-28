"""
Треугольник

Даны три натуральных числа.
Возможно ли построить треугольник с такими сторонами.
Если это возможно, выведите строку YES, иначе выведите строку NO.

Треугольник — это три точки, не лежащие на одной прямой.
"""
def check(a, b, c):
	if (a + b) > c and (a + c) > b and (b + c) > a:
		print("YES")
	else:
		print("NO")

def read_int():
	return int(input())


a = read_int()
b = read_int()
c = read_int()
check(a, b, c)