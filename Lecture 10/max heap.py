class BMaxH:
	def __init__(self):
		self.ilist = []
		self.index = 0
	
	def parent(self,i):
		return (i-1)//2

	def left(self, i):
		if self.index > 2*i+1:
			return 2*i+1
		else:
			return None

	def right(self, i):
		if self.index > 2*i+2:
			return 2*i+2
		else:
			return None

	def insert(self,val):
		self.ilist.append(val)
		self.index = self.index + 1
		i = self.index - 1
		while i != 0:
			if self.ilist[i] > self.ilist[self.parent(i)]:
				self.ilist[i],self.ilist[self.parent(i)] = self.ilist[self.parent(i)],self.ilist[i]
				i = self.parent(i)
			else:
				break
	'''def display(self):
		for i in range(0,self.index):
			print(self.ilist[i],',', end='')
		print('None')'''
		
	def steps(self):
		j = 1
		k = 1
		while self.index > k:
			k += 2**j
			j += 1
		return j

	def twos(self, n):
		j = 0
		for i in range(n):
			j += 2**i
		return j
	
	def display(self, vis=False, spacing = 3): 
		# Actual space between lowest level people
		# would be double of the value of spacing variable
		if vis:
			s = self.steps()

			tree = [[0]]
			for _ in range(s-1):
				temp = []
				for parent in tree[-1]:
					if parent != None:
						temp.append(self.left(parent))
						temp.append(self.right(parent))
				tree.append(temp)
			# print(tree)

			atStep = s-1
			space = " "
			for temp in tree:
				j = self.twos(atStep)
				# print(f"j = {j}")
				print((spacing*j)*space, end = "")            # Cal
				middle = (2*spacing*(j+1)-1)*space                  # Cal
				for ind in temp:
					if ind != None:
						elem = self.ilist[ind]
						print(elem, end = middle)
						elem = str(elem)
						if len(elem) > 1:
							for back in range(len(elem)-1):
								print("\b", end = "")
					else:
						print(None, end = middle)
						elem = str(None)
						if len(elem) > 1:
							for back in range(len(elem)-1):
								print("\b", end = "")
						
				# print("\nOne Step Done")
				print('\n')
				atStep -= 1
						
			
			
		else:print(self.ilist)


	def findmax(self):
		if self.index == 0:
			return None
		else:
			return self.ilist[0]
		
	def heapify(self, i): 
		leftchild = self.left(i)
		rightchild = self.right(i)
		# Check with left child (and it exists or not)
		if leftchild < self.index and self.ilist[leftchild] > self.ilist[i]:
			smallest = leftchild
		else:
			smallest = i
		if rightchild < self.index and self.ilist[rightchild] > self.ilist[smallest]:
			smallest = rightchild

		if smallest != i: 
			self.ilist[i], self.ilist[smallest] = self.ilist[smallest], self.ilist[i]
			self.heapify(smallest)

	def deletemax(self):
		max_item = self.findmax()
		if max_item is None:
			print('heap already empty')
			return
		self.ilist[0] = self.ilist[self.index-1]
		self.index -= 1
		self.ilist.pop()
		self.heapify(0)
		return max_item

bh = BMaxH()
a = [11,9,1,12,14,5,8,15,30]
for i in a:
    bh.insert(i)
    bh.display(True)
bh.deletemax()
bh.display(True)
bh.deletemax()
bh.display(True)
