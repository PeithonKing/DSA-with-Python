ans = -1
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
				
def search(x):
	global ans
	ans = -1
	bs(a, x, 0, len(a)-1)
	if ans >= 0: return True
	else: return False

import time
t1 = time.time()
maxim = 20000
a = list(range(1, maxim))
i = 2
while i	<= maxim**0.5:
	for j in range(2*i,maxim+1,i):
		if search(j): a.remove(j)
	i += 1
#print(a)
# print(f"There are {len(a)} primes found.")
print(f"Total time taken = {(time.time() - t1)} s")

