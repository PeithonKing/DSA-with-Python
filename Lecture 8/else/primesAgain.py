import time
t1 = time.time()
primes = []
start = 0
end = 4600
for num in range(2,end+1):
	isP = True
	for i in primes:
		if i > num**0.5: break
		if num % i == 0:
			isP = False
			break
	if isP: primes.append(num)

print(primes)
print(f"{len(primes)} primes are there between {start} and {end}")
print(f"Total time taken = {1000*(time.time() - t1)} ms")
