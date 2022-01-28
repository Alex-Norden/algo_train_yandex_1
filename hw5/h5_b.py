"""
Сумма номеров

Cколько существует наборов машин, стоящих подряд на местах с L до R,
что сумма их номеров равна K
"""
n, k = map(int, input().split())
a = list(map(int, input().split()))

last_ind = n - 1
l = r = 0
c = 0
sm = a[0]

to_next_l = False
to_next_r = False

while True:
	# print(f"{sm=}")
	if sm == k:
		c += 1
		to_next_l = True
		to_next_r = True
	elif sm > k:
		to_next_l = True
		if l == r:
			to_next_r = True
	else: #sm < k
		to_next_r = True

	if to_next_r:
		if r < last_ind:
			# add new item
			r += 1
			sm += a[r]
			to_next_r = False
		else:
			break

	if to_next_l:
		# sub old item
		sm -= a[l]
		l += 1
		to_next_l = False

print(c)