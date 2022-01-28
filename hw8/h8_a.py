"""
Высота дерева

Реализуйте бинарное дерево поиска для целых чисел.
Программа получает на вход последовательность целых чисел и строит из них дерево.
Элементы в деревья добавляются в соответствии с результатом поиска их места.
Если элемент уже существует в дереве, добавлять его не надо.
Балансировка дерева не производится.
"""
class Node:
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


class Tree:
	def __init__(self):
		self.root = None #корень дерева

	def height(self):
		def _height(node):
			if node is None:
				return 0
			l_h = _height(node.left)
			r_h = _height(node.right)
			h = l_h if l_h > r_h else r_h
			return h + 1

		return _height(self.root)

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


tree = Tree()

a = map(int, input().split())
for x in a:
	if x == 0:
		print(tree.height())
	else:
		tree.add_node(x)