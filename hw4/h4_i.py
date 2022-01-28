"""
Контрольная по ударениям

Выведите количество ошибок в Петином тексте, которые найдет Вася.
"""
from collections import defaultdict


n = int(input())

d_lower = defaultdict(set)
for _ in range(n):
	s = input()
	d_lower[s.lower()].add(s)
# print(f"{d_lower=}")

text = input()

mistakes = 0
for w in text.split():
	w_lower = w.lower()
	if w_lower in d_lower:
		if w not in d_lower[w_lower]:
			mistakes += 1
	else:
		stresses = 0
		for c in w:
			if c.isupper():
				stresses += 1
		if stresses != 1:
			mistakes += 1
	# 	print(f"{stresses=}")
	# print(f"{w=} | {mistakes=}")

print(mistakes)

"""
проходим по всем словам в тексте
если слово маленькими буквами в словаре, то проверяю если ли слово с ударением в множестве
если слово в мн-ве, то ошибки нет
иначе проверяю, что ровно одно ударение (иначе ошибка +1)
"""