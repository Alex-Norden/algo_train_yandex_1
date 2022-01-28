"""
Продажи

Создайте список всех покупателей, а для каждого покупателя
подсчитайте количество приобретенных им единиц каждого вида товаров.
"""
import sys
from collections import defaultdict


customers = defaultdict(dict)

for line in sys.stdin:
	if line:
		name, item, count = line.strip().split()
		count = int(count)

		if item in customers[name]:
			customers[name][item] += count
		else:
			customers[name][item] = count

for name in sorted(customers.keys()):
	print("{}:".format(name))

	items = customers[name]
	item_names = sorted(items.keys())
	for k in item_names:
		print(k, items[k])