"""
Уравнение с корнем

Программа должна вывести все решения уравнения в порядке возрастания,
либо NO SOLUTION (заглавными буквами), если решений нет.
Если решений бесконечно много, вывести MANY SOLUTIONS.
"""
def print_sol(a, b, c): #линейное ур
	def print_x(x):
		int_x = int(x)
		if int_x == x:
			print(int_x)
		else:
			print("NO SOLUTION")

	if c < 0:
		print("NO SOLUTION")
	elif c == 0:
		if a == 0:
			if b == 0:
				print("MANY SOLUTIONS")
			else:
				print("NO SOLUTION")
		else:
			if b == 0:
				print_x(0)
			else:
				print_x(-b/a)
	else:
		if a == 0:
			if b == 0:
				print("NO SOLUTION")
			else:
				if c*c == b:
					print("MANY SOLUTIONS")
				else:
					print("NO SOLUTION")
		else:
			if b == 0:
				print_x(c*c/a)
			else:
				print_x((c*c - b)/a)

def read_int():
	return int(input())


a = read_int()
b = read_int()
c = read_int()
print_sol(a, b, c)