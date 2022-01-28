"""
OpenCalculator

Напишите программу, определяющую, сможет ли Петя ввести число N, а если нет,
то какое минимальное количество кнопок надо дополнительно отобразить на экране для его ввода.
"""
# x, y, z = map(int, input())
btns = set(map(int, input().split()))
n = int(input())

digits = set()
while n > 0:
	n, rem = divmod(n, 10)
	digits.add(rem)

count = len(digits - btns)
print(count)