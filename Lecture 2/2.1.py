from math import sin
# from random import randint
a = [int(10*sin(x)) for x in range(10)]
# b = [randint(-9,9) for x in range(10)]
# print(b)

def maximum(List): # Input a list as arguement and get the minimum element of the list
	'''Function to find minimum element of a list'''
	val = List[0]
	for i in List:
		if i > val: val = i
	return val
	
def minimum(List): # Input a list as arguement and get the minimum element of the list
	'''Function to find maximum element of a list'''
	val = List[0]
	for i in List:
		if i < val: val = i
	return val
			

def Kth_L(l,k):
	'''Function to find kth largest element in a list'''
	temp = [x for x in l]
	for i in range(k-1):
	 	temp.remove(maximum(temp))
	 	# print(temp)
	return maximum(temp)
	
def Kth_S(l,k):
	'''Function to find kth smallest element in a list'''
	temp = [x for x in l]
	for i in range(k-1):
		temp.remove(minimum(temp))
		# print(temp)
	return minimum(temp)
	
def max_of_three():
	numbers = [int(input(f"Enter the number{i+1}: ")) for i in range(3)]
	print("Maximum of the three is", maximum(numbers), "\b.")

def LeapYear(year):
	if year%100 == 0:
		if year%400 == 0:
			print(f"{year} is a leap year.")
		else: print(f"{year} is not a leap year.")
	elif year%4 == 0: print(f"{year} is a leap year.")
	else: print(f"{year} is not a leap year.")

def F_and_L(num):
	print(f"{str(num)[0]} is the first digit of {num}.")
	print(f"{num%10} is the last digit of {num}.")
	
def F_swap_L(num):
	num = list(str(num))
	num[0], num[-1] = num[-1], num[0]
	string = ""
	for i in num: string += i
	num = int(string)
	return num
	
print("", F_swap_L(123654))
print() # Just to add a new line and keep things neat
F_and_L(2548)
print() # Just to add a new line and keep things neat
LeapYear(int(input("Enter a Year: ")))
print() # Just to add a new line and keep things neat
max_of_three()
print() # Just to add a new line and keep things neat
print("a = ", a)
print("Finding the kth smallest and largest element of a!")
k = int(input("Enter the value of k: "))
print(f"{k}th smallest element of a is {Kth_S(a,k)}.")
print(f"{k}th largest element of a is {Kth_L(a,k)}.")
