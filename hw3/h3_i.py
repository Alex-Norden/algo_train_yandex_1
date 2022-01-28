"""
Полиглоты

Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
"""
n = int(input())

k_all = None
k_any = set()

for _ in range(n):
	m = int(input())
	langs = tuple(input() for _ in range(m))

	if k_all is None:
		k_all = set(langs)
	else:
		k_all = k_all.intersection(langs)

	k_any.update(langs)

print(len(k_all))
for i in k_all:
	print(i)

print(len(k_any))
for i in k_any:
	print(i)