"""
Метро

Определите минимальное и максимальное время, которое Таня могла
провести на платформе, или сообщите, что она точно сбилась со счёта
"""
def read_int():
	return int(input())

def print_solution(a, b, n, m):
	min1 = n + a*(n - 1)
	min2 = m + b*(m - 1)
	l = max(min1, min2)

	max1 = n + a*(n + 1)
	max2 = m + b*(m + 1)
	r = min(max1, max2)

	if l > r:
		print(-1)
	else:
		print(l, r)


a = read_int()
b = read_int()
n = read_int()
m = read_int()

print_solution(a, b, n, m)