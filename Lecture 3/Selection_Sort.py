import random

def minPosition(List):
	'''Returns position of the minimum element'''
	pos = 0
	val = List[0]
	for i in range(len(List)):
		if List[i] < val:
			val = List[i]
			pos = i
	return pos

def SelectionSort(inputList):
	for i in range(len(inputList)):
		partition = i
		v = minPosition(a[i:len(inputList)])
		# "v" stores the position of the minimum element
		# of the unsorted part of the list, denoted by a[i:len(a)]
		inputList[v+i], inputList[i] = inputList[i], inputList[v+i]

a = [random.randint(0,9) for x in range(10)]
print(a)
SelectionSort(a)
print(a)
