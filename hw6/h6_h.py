"""
Провода

Дано N отрезков провода длиной LN сантиметров.
Требуется с помощью разрезания получить из них K равных отрезков как можно большей длины,
выражающейся целым числом сантиметров. Если нельзя получить K отрезков длиной даже 1 см, вывести 0
"""
def print_sol(n, k, lengths):
	def rbinsearch():
		def check(m):
			count = 0
			for length in lengths:
				count += length // m
			return count >= k

		l = 0 #недопустимое зн-е, т.к. деление на 0
		r = max(lengths) + 1
		while r - l > 1:
			m = (l + r) // 2
			if check(m):
				l = m
			else:
				r = m

		return l

	lengths.sort()
	print(rbinsearch())

n, k = map(int, input().split())
lengths = [int(input()) for _ in range(n)]

print_sol(n, k, lengths)

"""
бинпоск по ответу (длине отрезка)
удастся ли нарезать K отрезков длиной M
"""