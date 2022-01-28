"""
Ближайшее число

Напишите программу, которая находит в массиве элемент,
самый близкий по величине к данному числу.
"""
n = int(input())
a = list(map(int, input().split()))
x = int(input())

min_d = None
ans = None

for num in a:
	d = x - num if x > num else num - x
	if min_d is None or d < min_d:
		ans = num
		min_d = d

print(ans)
# print(f"{min_d=}")