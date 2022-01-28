"""
Родословная: число потомков

В генеалогическом древе у каждого человека,
кроме родоначальника, есть ровно один родитель

Для каждого элемента дерева определите число
всех его потомков (не считая его самого)
"""
import sys
sys.setrecursionlimit(100000)
from collections import defaultdict


n = int(input())

p2children = defaultdict(list)
all_mans = set()

for _ in range(n - 1):
	child, parent = input().split()
	p2children[parent].append(child)
	all_mans.add(child)
	all_mans.add(parent)

cnt = {}
def count_childs(man):
	if man in cnt:
		# print("man in cnt", man, cnt[man])
		return cnt[man]

	children = p2children.get(man, None)
	if not children: #base case
		# print("not children")
		return 0

	#recursive case
	# добавляем потомков и считаем их детей
	count = len(children)
	# print("len(children)")
	for child in children:
		count += count_childs(child)
	return count

for man in all_mans:
	cnt[man] = count_childs(man)

for man, count in sorted(cnt.items()):
	print(man, count)


"""
записываем детей к родителям
заводим множество всех людей
для каждого человека считаем рекурсивно кол-во детей
"""