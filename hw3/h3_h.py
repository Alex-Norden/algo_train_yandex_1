"""
Злые свинки

По заданному расположению птиц необходимо определить,
какое минимальное количество выстрелов необходимо, чтобы все птицы были сбиты.
"""
n = int(input())

hit_x = set()
for _ in range(n):
	x, y = map(int, input().split())
	hit_x.add(x)

print(len(hit_x))