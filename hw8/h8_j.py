"""
Родословная: подсчет уровней

В генеалогическом древе у каждого человека,
кроме родоначальника, есть ровно один родитель.
Каждом элементу дерева сопоставляется целое
неотрицательное число, называемое высотой.
У родоначальника высота равна 0, у любого другого элемента
высота на 1 больше, чем у его родителя.

Вам дано генеалогическое древо, определите высоту всех его элементов
"""
def height(man):
	if man in child2parent:
		return 1 + height(child2parent[man])
	else: #нет родителя
		return 0

child2parent = {}
n = int(input())
for _ in range(n - 1):
	child, parent = input().split()
	child2parent[child] = parent

children = set(child2parent.keys())
parents = set(child2parent.values())

heights = {}
for man in children.union(parents):
	heights[man] = height(man)

for key, value in sorted(heights.items()):
	print(key, value)

"""
пытаемся от каждого ребёнка дойти до родителя
если есть родитель увел-ем высоту

*для ускорения можно добавить кэширование
"""