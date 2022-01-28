"""
Количество слов в тексте
"""
import sys


words = []
for line in sys.stdin:
	words.extend(line.strip().split())

print(len(set(words)))