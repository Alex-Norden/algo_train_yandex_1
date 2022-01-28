"""
Счет в гипершашках

Написать программу, которая по числу k и значениям чисел на карточках,
которые имеются у Андрея, определяет количество различных вариантов счета,
которые Андрей может показать на табло
"""
n, k = map(int, input().split())
x = list(map(int, input().split()))

cnt = {}
for xi in x:
	if xi in cnt:
		cnt[xi] += 1
	else:
		cnt[xi] = 1
uniq = list(cnt.keys())
uniq.sort()
len_uniq = len(uniq)

r = 0
ans = 0
duplicates = 0

for l in range(len_uniq):
	while r < len_uniq and uniq[l] * k >= uniq[r]:
		if cnt[uniq[r]] > 1:
			duplicates += 1
		r += 1

	range_len = r - l
	if cnt[uniq[l]] > 1:
		ans += (range_len - 1) * 3
		duplicates -= 1

	if cnt[uniq[l]] > 2:
		ans += 1

	ans += (range_len - 1) * (range_len - 2) * 3

	ans += duplicates * 3

print(ans)