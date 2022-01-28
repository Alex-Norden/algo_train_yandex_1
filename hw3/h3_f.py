"""
Инопланетный геном

Вам даны два генома, определите степень близости первого генома второму геному.
"""
def get_pairs(s):
	return [s[i - 1:i + 1] for i in range(1, len(s))]


a = tuple(get_pairs(input()))
b = set(get_pairs(input()))

count = 0
for i in a:
	if i in b:
		count += 1

print(count)