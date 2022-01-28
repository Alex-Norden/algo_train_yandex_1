"""
Определить вид последовательности
"""
CONSTANT, ASCENDING, WEAKLY_ASCENDING, DESCENDING, WEAKLY_DESCENDING, RANDOM = range(1, 7)
answers = (
	"CONSTANT",
	"ASCENDING",
	"WEAKLY ASCENDING",
	"DESCENDING",
	"WEAKLY DESCENDING",
	"RANDOM"
)


STOP_NUM = -2*(10**9)

t = None
prev = None

while True:
	cur = int(input())
	if cur == STOP_NUM:
		break

	# define new_type
	new_t = None
	if prev is not None:
		if cur > prev:
			new_t = ASCENDING
		elif cur < prev:
			new_t = DESCENDING
		else:
			new_t = CONSTANT
	prev = cur

	# switch seq_type
	if not t:
		t = new_t
	elif t != new_t:
		if t == CONSTANT:
			if new_t == ASCENDING:
				t = WEAKLY_ASCENDING
			elif new_t == DESCENDING:
				t = WEAKLY_DESCENDING
		elif t == ASCENDING:
			if new_t == CONSTANT:
				t = WEAKLY_ASCENDING
			elif new_t == DESCENDING:
				t = RANDOM
		elif t == WEAKLY_ASCENDING:
			if new_t == DESCENDING:
				t = RANDOM
		elif t == DESCENDING:
			if new_t == CONSTANT:
				t = WEAKLY_DESCENDING
			elif new_t == ASCENDING:
				t = RANDOM
		elif t == WEAKLY_DESCENDING:
			if new_t == ASCENDING:
				t = RANDOM

if not t: #len seq < 2
	t = CONSTANT

print(answers[t - 1])