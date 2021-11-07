a = [1, 2, 3, 5, 6, 7, 8]
ans = -1
print(f"List is {a}.")
x = int(input("Find in list: "))
lb = 0
ub = len(a)-1

while lb <= ub:
	if (ub+lb) % 2:
		c = int((ub+lb+1)/2)
	else:
		c = int((ub+lb)/2)
	if a[c] == x:
		ans = c
		break
	elif x < a[c]:
		if ub != c-1:
			ub = c-1
		else:
			break
	else:
		if lb != c:
			lb = c
		else:
			break

if ans >= 0:
	print(f"{x} is in the list at position {ans}.")
else:
	print(f"{x} not found in {a}.")
