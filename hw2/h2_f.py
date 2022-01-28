"""
Симметричная последовательность

Определить, какое минимальное количество и каких чисел надо
приписать в конец этой последовательности, чтобы она стала симметричной
"""
def sol(a, n):
	for start in range(n):
		l = start
		r = n - 1
		while l < n and r >= 0 and a[l] == a[r] and l <= r:
			l += 1
			r -= 1
		if l > r:
			ans = [a[i] for i in range(start - 1, -1, -1)]
			len_ans = len(ans)
			print(len_ans)
			if len_ans:
				print(*ans)

			return


n = int(input())
a = list(map(int, input().split()))

sol(a, n)