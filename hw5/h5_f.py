"""
Кондиционеры

Написать программу, которая определит, за какую минимальную
суммарную стоимость кондиционеров можно оснастить все классы школы

O(n*log(n) + m*log(m))
"""
n = int(input())
a = list(map(int, input().split()))
m = int(input())
bc = [tuple(map(int, input().split())) for _ in range(m)] #b, c

a.sort()
bc.sort(key=lambda t: t[1])

s = 0
r = 0
for ai in a:
	# while r < (m - 1) and ai > bc[r]:
	while ai > bc[r][0]:
		r += 1
	# найден подходящий
	s += bc[r][1]

print(s)