"""
Современники

Вам дан список великих людей с датами их жизни.
Выведите всевозможные максимальные множества современников.
Множество современников будем называть максимальным,
если нет другого множества современников,
которое включает в себя всех людей из первого множества.
"""
def is_leap(y):
	if y % 4 != 0 or (y % 100 == 0 and y % 400 != 0):
		return False
	else:
		return True

# print(is_leap(2100))

def to_days(day, month, year):
	month2days = [None, 31, None, 31, 30, 31, 30, 31, 31, 30, 31, 30] #[0, 11] декабрь не нужен
	days = 0
	for y in range(1, year): #[1..year-1]
		days += 366 if is_leap(y) else 365

	for m in range(1, month): #[1..month-1]
		if m == 2:
			days += 29 if is_leap(year) else 28
		else:
			days += month2days[m]

	return days + day

# print(to_days(18, 8, 2021))

def add_years(day, month, year, offset):
	year += offset
	return day, month, year


OUT, IN = (1, 2)


n = int(input())

events = []
for i_man in range(1, n + 1):
	s = input()
	d1, m1, y1, d2, m2, y2 = map(int, s.split())
	tin = to_days(d1, m1, y1)
	tout = to_days(d2, m2, y2)

	t18 = to_days(d1, m1, y1 + 18)
	if t18 < tout: #пережил 18 лет
		t80 = to_days(d1, m1, y1 + 80)
		events.append((t18, IN, i_man))
		events.append((min(tout, t80), OUT, i_man))


def solution():
	if len(events) == 0:
		print(0)
		return

	events.sort()

	contemps = set()
	updated = False

	for _, type_e, i_man in events:
		if type_e == IN:
			contemps.add(i_man)
			updated = True
		else:
			if updated:
				print(*contemps)
				updated = False
			contemps.remove(i_man)


solution()

"""
перевести в дни с учётом дней в месяцах и високосного года
сдвинуть отрезки от 18 лет до min(годы_жизни, 80)

исходя из условия OUT РАНЬШЕ IN
при наступлении 18 лет добавить в мн-во
при смерти или наступлении 80 лет удалить
"""