"""
Детали

Напишите программу, которая вычислит, какое количество деталей
м.б. получено по этой технологии из имеющихся исходно N кг сплава
"""
def solution(n, k, m):
	ctotal = 0
	rem_total = n

	while True:
		ck, rem_k = divmod(rem_total, k)
		if not ck: #заготовок не вышло
			break
		cm, rem_m = divmod(k, m)
		if not cm: #деталей не вышло
			break

		ctotal += cm*ck
		rem_total = rem_k + rem_m*ck

	return ctotal


n, k, m = map(int, input().strip().split())
print(solution(n, k, m))