"""
Номер появления слова
"""
import sys
from collections import defaultdict


counter = defaultdict(int)

for line in sys.stdin:
	for w in line.strip().split():
		print(counter[w], end=" ")
		counter[w] += 1