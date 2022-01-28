"""
Город Че

Сколько способов есть выбрать два различных памятника для организации свиданий
"""
n, r_dist = map(int, input().split())
d = tuple(map(int, input().split()))

# count_pairs
count = 0
r = 0
for l in range(n):
	while r < n and d[r] - d[l] <= r_dist:
		r += 1
	count += n - r #если ничего не найдено, то добавится 0

print(count)

"""
Пока видят, двигаем правую границу
"""