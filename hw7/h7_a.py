"""
Наблюдение за студентами

Посчитать количество студентов, которые все таки будут искать ответы к экзамену
"""
BEGIN, END = (1, 2)

n, m = map(int, input().split())

events = []
for _ in range(m):
	b_ind, e_ind = map(int, input().split())
	events.append((b_ind, BEGIN))
	events.append((e_ind, END))

events.sort()
len_events = len(events)

ans = 0
c_watch = 0
l_ind = 0 #левый студент без наблюдателей

for i in range(len_events):
	if c_watch == 0:
		ans += events[i][0] - l_ind

	if events[i][1] == BEGIN:
		c_watch += 1
	else:
		c_watch -= 1

	if c_watch == 0:
		l_ind = events[i][0] + 1

ans += n - l_ind
print(ans)

"""
будем перебирать события, т.к. наблюдателей намного меньше, чем студентов(парт)

"смотрим назад" на "счётчик наблюдателей"
отрезки уже заданы
сортируем их по левыму краю (начало наблюдения)
если "счётчик наблюдателей"=0 (за партой никто не наблюдает), то добавляем студентов "без наблюдателей"

*возможен случай что наблюдатели закончились, а парты остались
"""