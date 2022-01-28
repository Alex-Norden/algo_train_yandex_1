"""
Глубина добавляемых элементов

В бинарное дерево поиска добавляются элементы.
Выведите глубину для каждого добавленного элемента в том порядке, как они добавлялись.
Если элемент уже есть в дереве, то ничего добавлять и выводить не нужно.
Глубиной называется расстояние от корня дерева до элемента включительно.
"""
class Node:
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


class Tree:
	def __init__(self):
		self.root = None

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
		def _add(node, x, h):
			h += 1
			if x < node.data:
				if node.left is None:
					node.left = Node(x)
					print(h, end=" ")
				else:
					_add(node.left, x, h)
			elif x > node.data:
				if node.right is None:
					node.right = Node(x)
					print(h, end=" ")
				else:
					_add(node.right, x, h)

		h = 1
		if self.root is None:
			self.root = Node(x)
			print(h, end=" ")
		else:
			_add(self.root, x, h)


tree = Tree()

a = map(int, input().split())
for x in a:
	if x != 0:
		tree.add_node(x)