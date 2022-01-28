"""
Охрана

Укажите, верно ли что для данного набора охранников,
объект охраняется в любой момент времени хотя бы одним охранником
и удаление любого из них приводит к появлению промежутка времени,
когда объект не охраняется.
"""
IN, OUT = (1, 2)

k = int(input())

ans = [""] * k
for i_test in range(k):
	n, *times = map(int, input().split())

	events = [0] * (n * 2)
	for i in range(0, n * 2, 2):
		events[i] = (times[i], IN, i)
		events[i + 1] = (times[i + 1], OUT, i)

	events.sort()
	good_seq = set()
	seq = set()
	good_flag = True
	prev_time = -1
	for (t, type_e, i_scr) in events:
		if t != 0 and len(seq) == 0:
			good_flag = False
			break

		if len(seq) == 1 and t != prev_time:
			good_seq.update(seq)

		if type_e == IN:
			seq.add(i_scr)
		else:
			seq.remove(i_scr)
		prev_time = t

	if prev_time != 10000:
		good_flag = False

	if good_flag and len(good_seq) == n:
		ans[i_test] = "Accepted"
	else:
		ans[i_test] = "Wrong Answer"

print("\n".join(ans))

"""
введём номер охранника "i_scr" (будет с шагом 2, но это не важно)

в момент пересменки сначала приходит новый, затем уходит старый, т.е. IN РАНЬШЕ OUT

если наступил момент, когда охранников нет и это не начало -> WA
если последний охранник ушёл раньше конца последней смены -> WA

если охранник на посту один на протяжении ненулевого промежутка -> он необходим
"""