'''
def f(x):
	def g(x):
		return (x+2)
	def h(x):
		return (x-2)
	if x >= 0: return g(x)
	else: return h(x)

while True:
	v = int(input("\nEnter a value: "))
	print(f(v))


a = []
while True:
	num = input("Enter a Number: ")
	if num == "q":
		break
	else:
		a.append(int(num))
print(a)
'''
"""a = [1, 3, 3, 6, 5, 7, 4, 10, 8, 5]
print(a.index(10))"""
a = None
print(str(a))
print(a)
