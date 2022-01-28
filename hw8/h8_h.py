"""
АВЛ-сбалансированность

Дерево называется АВЛ-сбалансированным,
если для любой его вершины высота левого
и правого поддерева для этой вершины различаются не более чем на 1
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

	def is_balanced(self):
		"""
		height с добавлением условия балансировки
		"""
		def _height(node):
			if node is None:
				return 0
			l_h = _height(node.left)
			r_h = _height(node.right)
			self._balance = self._balance and abs(l_h - r_h) < 2
			h = l_h if l_h > r_h else r_h
			return h + 1

		self._balance = True
		_height(self.root)
		return self._balance


tree = Tree()

a = map(int, input().split())
for x in a:
	if x != 0:
		tree.add_node(x)

print("YES" if tree.is_balanced() else "NO")