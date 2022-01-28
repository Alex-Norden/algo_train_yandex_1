"""
Автобусы

Определите наименьшее количество новых автобусов,
достаточное для обеспечения движения по расписанию
в течение неограниченного периода времени
"""
ARR, DEP = (1, 2)

def to_minutes(t):
	h = int(t[:2])
	m = int(t[3:])
	return h*60 + m

n, m = map(int, input().split())

cnt_bus = [0] * (n + 1) #номера автобусов [1, N]
cnt_balance = [0] * (n + 1)
events = []
over_midnight = 0

for i in range(m):
	i_dep, t_dep, i_arr, t_arr = input().split()
	i_dep = int(i_dep)
	i_arr = int(i_arr)
	t_dep = to_minutes(t_dep)
	t_arr = to_minutes(t_arr)
	if t_arr < t_dep:
		over_midnight += 1

	cnt_balance[i_dep] -= 1
	cnt_balance[i_arr] += 1
	events.append((t_arr, ARR, i_arr))
	events.append((t_dep, DEP, i_dep))

disbalance = False
for i in range(1, n + 1):
	if cnt_balance[i] != 0:
		disbalance = True

if disbalance:
	print(-1)
else:
	events.sort()
	for _, type_e, i_city in events:
		if type_e == ARR:
			cnt_bus[i_city] += 1
		else:
			if cnt_bus[i_city] > 0:
				cnt_bus[i_city] -= 1

	ans = 0
	for i in range(1, n + 1):
		ans += cnt_bus[i]
	print(ans + over_midnight)

"""
приезд +1, отъезд -1
т.к. автобус может отправиться в тот же момент, то событие приезда РАНЬШЕ

если в городе не было автобуса, то вычитания не будет, но будет +1, в итоге сумма 1
это не выполняется только для автобусов-полуночников (для них в сумме будет 0, т.к. сначала прибытие +1, затем отправление -1)
поэтому посчитаем их кол-во заранее
"""