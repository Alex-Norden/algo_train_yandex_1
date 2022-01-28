"""
Телефонные номера

Для каждого телефонного номера в адресной книге выведите YES (заглавными буквами),
если он совпадает с тем телефонным номером, который Вася хочет добавить в адресную
книгу или NO (заглавными буквами) в противном случае.
"""
def read_number():
	num = []
	for c in input().strip():
		if c.isdigit():
			num.append(c)

	if len(num) == 7:
		return "8495" + "".join(num)
	else:
		num[0] = "8"
		return "".join(num)


new_num = read_number()
for _ in range(3):
	old_num = read_number()
	if old_num == new_num:
		print("YES")
	else:
		print("NO")