"""
Детский праздник

Через какое время будут надуты все шарики при наиболее оптимальной
работе помощников, и сколько шариков надует каждый из них
"""

m, n = map(int, input().split())
mans = [None] * n
for i in range(n):
	t_one, z, y = map(int, input().split())
	mans[i] = (t_one, z, t_one * z + y)

TIME_MAX = 200*15000
def lbinsearch():
	def check(t_mid):
		total_count = 0
		for t_one, z, t_man in mans:
			count_times_with_rest, t_rem = divmod(t_mid, t_man)
			count_without_rest = min(t_rem // t_one, z)
			total_count += count_times_with_rest * z + count_without_rest
		return total_count >= m

	l = -1
	r = TIME_MAX + 1
	while r - l > 1:
		mid = (l + r) // 2
		if check(mid):
			r = mid
		else:
			l = mid
	return r

t_ans = lbinsearch()

rem_count = m
ans_list = [None] * n
for i, (t_one, z, t_man) in enumerate(mans):
	count_times_with_rest, t_rem = divmod(t_ans, t_man)
	count_without_rest = min(t_rem // t_one, z)
	count_man = count_times_with_rest * z + count_without_rest
	ans_list[i] = rem_count if count_man > rem_count else count_man
	rem_count -= count_man
	if rem_count < 0:
		rem_count = 0

	# print(f"{count_times_with_rest=}")
	# print(f"{count_without_rest=}")

print(t_ans)
print(*ans_list)

"""
подход = время непрерывного надувания и отдыха
считаем кол-во подходов и умножаем на кол-во шаров за подход
если осталось время непрерывно надувает дальше (успеет не более Z)

используем левый бинпоиск по ответу
проверим надуто ли кол-во
максимальное время, если будет надувать один самый медленный и много отдыхать
"""