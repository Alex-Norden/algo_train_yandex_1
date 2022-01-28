"""
Банковские счета

Для каждого запроса BALANCE программа должна вывести остаток на счету данного клиента.
Если же у клиента с запрашиваемым именем не открыт счет в банке, выведите ERROR.
"""
import sys
from collections import defaultdict


acc = defaultdict(int)


def deposit(name, s):
	acc[name] += int(s)

def withdraw(name, s):
	acc[name] -= int(s)

def transfer(name1, name2, s):
	s = int(s)
	withdraw(name1, s)
	deposit(name2, s)

def income(p):
	p = float(p) / 100
	for k, s in acc.items():
		if s > 0:
			acc[k] += int(s * p)

def balance(name):
	if name in acc:
		print(acc[name])
	else:
		print("ERROR")


funcs = {
	"DEPOSIT": deposit,
	"WITHDRAW": withdraw,
	"TRANSFER": transfer,
	"INCOME": income,
	"BALANCE": balance
}


for line in sys.stdin:
	if line:
		_type, *args = line.strip().split()
		funcs[_type](*args)