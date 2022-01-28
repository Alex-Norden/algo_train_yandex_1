"""
Подстрока

Требуется найти максимальную по длине подстроку данной строки,
такую что каждый символ встречается в ней не более k раз.
"""

n, k = map(int, input().split())
s = input()

max_len = 0
res_l = l = 0

cnt = {}
for r in range(n):
	if s[r] in cnt:
		if cnt[s[r]] == k:
			while s[l] != s[r]:
				cnt[s[l]] -= 1
				l += 1
			cnt[s[l]] -= 1
			l += 1

		cnt[s[r]] += 1
	else:
		cnt[s[r]] = 1

	len_sub = r - l + 1
	if len_sub > max_len:
		max_len = len_sub
		res_l = l

	# print(f"{l=} | {r=}")

print(max_len, res_l + 1)

"""
добавляем
если символ был и уже K раз, то сдвинуть L
сравниваем длину
"""