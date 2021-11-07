def bs(a, x, lb, ub):
	global ans
	if lb <= ub:
		if (ub+lb) % 2:
			c = int((ub+lb+1)/2)
		else:
			c = int((ub+lb)/2)
		if a[c] == x:
			ans = c
		elif x < a[c]:
			if c-1 != ub:
				bs(a, x, lb, c-1)
		else:
			if c != lb:
				bs(a, x, c, ub)

a = [1, 2, 3, 5, 6, 7, 8]
ans = -1
print(f"List is {a}.")
x = int(input("Find in list: "))
bs(a, x, 0, len(a)-1)
if ans >= 0:
	print(f"{x} is in list at position {ans}.")
else:
	print(f"{x} not found in {a}.")
