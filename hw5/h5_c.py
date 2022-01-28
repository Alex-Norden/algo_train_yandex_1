"""
Туризм

Для каждой трассы выведите одно число — суммарную высоту подъемов на данной трассе

*трасса может идти как слева-направо, так и справа-налево
*начало и конец трассы могут совпадать
"""
n = int(input())
y = [int(input().split()[1]) for _ in range(n)]

p_right = [0] * (n + 1)
p_left = [0] * (n + 1)

for i in range(1, n):
	h = y[i] - y[i - 1]
	if h < 0:
		h = 0
	p_right[i + 1] = p_right[i] + h

for i in range(n - 1, 0, -1): #[n-1, 1]
	h = y[i - 1] - y[i] #теперь наоборот
	if h < 0:
		h = 0
	p_left[i] = p_left[i + 1] + h

# print(f"{p_right=}")
# print(f"{p_left=}")

m = int(input())
for _ in range(m):
	s, f = map(int, input().split())
	if s > f:
		ans = p_left[f] - p_left[s]
	else:
		ans = p_right[f] - p_right[s]
	print(ans)