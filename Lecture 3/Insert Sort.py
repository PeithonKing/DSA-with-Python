def InsertSort(List):
	p1 = 1
	while p1 < len(List):
		# print("p1 = ", List[p1])
		temp = List[p1]
		# print("temp =", temp)
		p2 = p1-1
		# print("p2 = ", List[p2])		
		while p2 >= 0:
			if temp < List[p2]:
				List[p2], List[p2+1] = List[p2+1], List[p2]
				# print(f"Swapped {List[p2]} and {List[p2+1]}")
				# print(List)
				p2 -= 1
			else:
				List[p2+1] = temp
				# print("Inserting!")
				# print(List)
				break
		p1 += 1


import random
a = [random.randint(-9,9) for x in range(10)]
print(a)
InsertSort(a)
print(a)
