"""
Обход

Выведите все элементы полученного дерева в порядке возрастания
"""
class Node:
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


class Tree:
	def __init__(self):
		self.root = None

	def add_node(self, x):
		def _add(node, x):
			if x < node.data:
				if node.left is None:
					node.left = Node(x)
				else:
					_add(node.left, x)
			elif x > node.data:
				if node.right is None:
					node.right = Node(x)
				else:
					_add(node.right, x)

		if self.root is None:
			self.root = Node(x)
		else:
			_add(self.root, x)

	def sorted_data(self, node=None):
		"""
		левый обход - влево до упора (None)
		1.левый обход для текущего и заполняем стек
		2.поднимаемся на уровень, возвращаем значение, шаг вправо и повтор шага 1
		если стек пуст и нет текущего узла (некуда идти), то заканчиваем

		порядок: слева, предок, справа
		если есть узел -> добавляем в стек, идём влево
		если нет текущего узла -> выталкиваем из стека, возвращаем зн-е, идём вправо
		"""
		if node is None:
			node = self.root

		stack = []
		while stack or node:
			if node is not None:
				stack.append(node)
				node = node.left
			else:
				node = stack.pop()
				yield node.data
				node = node.right


tree = Tree()

a = map(int, input().split())
for x in a:
	if x != 0:
		tree.add_node(x)

print("\n".join(map(str, tree.sorted_data())))