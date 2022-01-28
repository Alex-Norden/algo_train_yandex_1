"""
Красота превыше всего

Найти отрезок наименьшей длины, удовлетворяющий указанным ограничениям
"""

n, k = map(int, input().split())
a = list(map(int, input().split()))

l = 0
cnt = {}

res_l = 0 #границы по-умолчанию
res_r = n - 1
min_len = n

for r in range(n):
	if a[r] in cnt:
		cnt[a[r]] += 1
	else:
		cnt[a[r]] = 1

	# если правее есть такой же эл-т, то сдвинуть левый указатель
	while cnt[a[l]] > 1:
		cnt[a[l]] -= 1
		l += 1

	if len(cnt) == k: #если длины совпадают, то и мн-ва совпадают, т.к. в CNT нет лишних
		len_s = r - l + 1
		if len_s < min_len:
			min_len = len_s
			res_l = l
			res_r = r

	# print(f"{l=} | {r=}")

print(res_l + 1, res_r + 1)

"""
отрезок наим. длины/'сжатие по-максимуму' (отличается от расширения)
идти по строке
пока есть дубли 'поджимать' левый указатель
если мн-во подходит, попробовать обновить минимум
"""