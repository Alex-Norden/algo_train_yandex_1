"""
Расшифровка письменности Майя

Единственная строка выходных данных программы должна содержать количество возможных вхождений слова W в S.
"""
def get_counter(s):
	counter = {}
	for ch in s:
		if ch in counter:
			counter[ch] += 1
		else:
			counter[ch] = 1
	return counter

def match_counters(cnt1, cnt2):
	matches = 0
	for ch in cnt1:
		if cnt1[ch] == cnt2.get(ch, None):
			matches += 1
	return matches

def modif_counter(scnt, wcnt, ch, count):
	ans = 0
	if ch not in scnt:
		scnt[ch] = 0
	if scnt[ch] == wcnt.get(ch, None):
		ans = -1
	scnt[ch] += count
	if scnt[ch] == wcnt.get(ch, None):
		ans = 1
	return ans


len_w, len_s = map(int, input().split())
w = input()
s = input()
wcnt = get_counter(w)
scnt = get_counter(s[:len_w])

matching_letters = match_counters(wcnt, scnt)
occurrences = 1 if matching_letters == len(wcnt) else 0

for i in range(len_w, len_s):
	matching_letters += modif_counter(scnt, wcnt, s[i - len_w], -1)
	matching_letters += modif_counter(scnt, wcnt, s[i], 1)
	if matching_letters == len(wcnt):
		occurrences += 1

print(occurrences)