"""
Дополнительная проверка на списывание

Выведите идентификатор, встречающийся в программе максимальное число раз.
"""
import sys


n, case_sen, st_digit = sys.stdin.readline().strip().split()
n = int(n)
case_sen = bool(case_sen == "yes")
st_digit = bool(st_digit == "yes")


keywords = set()
for _ in range(n):
	keyword = sys.stdin.readline().strip()
	if case_sen:
		keywords.add(keyword)
	else:
		keywords.add(keyword.lower())


def preproc_str(s):
	cleaned = "".join((c if c.isalnum() or c == "_" else " " for c in s))
	if case_sen:
		return cleaned
	else:
		return cleaned.lower()

def is_correct(w):
	if w in keywords:
		return False

	f_digit = w[0].isdigit()
	if f_digit:
		if len(w) == 1 or not st_digit:
			return False

	return True


cnt = {}
w2pos = {}
w_pos = 0

for line in sys.stdin:
	line = preproc_str(line.strip())

	for w in line.split():
		if is_correct(w):
			if w in cnt:
				cnt[w] += 1
			else:
				cnt[w] = 1
				w2pos[w] = w_pos
			w_pos += 1

# print(f"{w2pos=}")

# find popular
popular = None
max_count = -1
for w, count in cnt.items():
	# print(w, count)
	if popular is None or (count > max_count):
		popular = w
		max_count = count
	elif count == max_count and w2pos[w] < w2pos[popular]:
		popular = w

print(popular)