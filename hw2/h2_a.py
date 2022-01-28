"""
Возрастает ли список?

Выведите YES, если массив монотонно возрастает и NO в противном случае.
"""
def read_int():
	return int(input())

def check(a):
	n = len(a)
	if n > 1:
		for i in range(1, n):
			if a[i] <= a[i - 1]:
				return False
	return True


a = list(map(int, input().split()))

if check(a):
	print("YES")
else:
	print("NO")