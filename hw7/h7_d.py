"""
Реклама

Определить моменты времени, когда нужно включить трансляцию рекламных роликов,
чтобы как можно большее количество покупателей прослушало ролик целиком
от начала до конца хотя бы один раз
"""
IN, BEFORE_OUT = (1, 2) #вход, 5 минут до выхода
TIME_ADV = 5

n = int(input())
events = [] #размер заранее не знаем
for i_man in range(n):
	tin, tout = map(int, input().split())
	if tout - tin >= TIME_ADV:
		events.append((tin, IN, i_man))
		events.append((tout - TIME_ADV, BEFORE_OUT, i_man))

events.sort()
len_events = len(events)

if len_events == 0:
	print(0, TIME_ADV, TIME_ADV*2)
elif len_events == 2: #one man
	print(1, events[0][0], events[0][0] + TIME_ADV)
else:
	best_ans = 0
	best1 = best2 = 0
	ad1 = set()
	for i in range(len_events):
		# e1 = events[i]
		t_e1, type_e1, i_man_e1 = events[i]
		if type_e1 == IN:
			ad1.add(i_man_e1)
			if len(ad1) > best_ans:
				best_ans = len(ad1)
				best1 = t_e1
				best2 = t_e1 + TIME_ADV

		count_ad2 = 0
		for j in range(i + 1, len_events):
			# e2 = events[j]
			t_e2, type_e2, i_man_e2 = events[j]
			if type_e2 == IN and i_man_e2 not in ad1:
				count_ad2 += 1
			if t_e2 - t_e1 >= TIME_ADV and len(ad1) + count_ad2 > best_ans:
				best_ans = len(ad1) + count_ad2
				best1 = t_e1
				best2 = t_e2
			if type_e2 == BEFORE_OUT and i_man_e2 not in ad1:
				count_ad2 -= 1

		if type_e1 == BEFORE_OUT:
			ad1.remove(i_man_e1)

	print(best_ans, best1, best2)

"""
заводим список событий
добавляем только посещения от 5 минут
"""