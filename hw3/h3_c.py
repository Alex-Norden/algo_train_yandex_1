"""
Кубики
"""
def sol(a, b):
	def print_set(s):
		print(len(s))
		print(*sorted(s))

	s1 = set(a)
	s2 = set(b)
	intersec = s1.intersection(s2)
	print_set(intersec)
	print_set(s1 - intersec)
	print_set(s2 - intersec)


n, m = map(int, input().split())

a = [int(input()) for _ in range(n)]
b = [int(input()) for _ in range(m)]

sol(a, b)