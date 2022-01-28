"""
Черепахи

Ваша задача определить, сколько самое большее количество черепах могут говорить правду.
"""
n = int(input())
n_1 = n - 1

ans = set()
for _ in range(n):
	a, b = map(int, input().split())
	if (0 <= a < n) and (0 <= b < n):
		if (a + b) == n_1:
			ans.add((a, b))

m = len(ans)
print(m)