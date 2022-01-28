"""
Чемпионат по метанию коровьих лепешек

Будем считать, что участник соревнования занял k-е место,
если ровно (k − 1) участников чемпионата метнули лепешку строго дальше, чем он

Какое максимально высокое место мог занять Василий?
"""
def sol(a, n):
	max_a = max(a)
	t_dist = 0 #столько точно не выбил
	to_find = False

	for i in range(n - 1):
		if a[i] == max_a and not to_find:
			to_find = True
		elif to_find:
			a2 = a[i]
			a3 = a[i + 1]
			if (a2 % 10) == 5 and a2 > a3:
				if a2 > t_dist:
					t_dist = a2

	if t_dist: #найден в списке
		t_pos = 1
		for dist in a:
			if dist > t_dist:
				t_pos += 1
		return t_pos
	else:
		return 0


n = int(input())
a = list(map(int, input().split()))

print(sol(a, n))