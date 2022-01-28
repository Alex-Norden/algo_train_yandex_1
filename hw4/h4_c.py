"""
Самое частое слово

Дан текст. Выведите слово, которое в этом тексте встречается чаще всего.
Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
"""
import sys
from collections import defaultdict


counter = defaultdict(int)

mx = 0
word = None

for line in sys.stdin:
	for w in line.strip().split():
		counter[w] += 1
		count = counter[w]

		if word is None or count > mx:
			word = w
			mx = count
		elif count == mx:
			if w < word:
				word = w
				mx = count

print(word)