class BinaryMinHeap:
	def __init__(self):
		self.ilist = []
		self.index = 0

	def parent(self, i):
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
		# print(f"Insering {val}")
		self.ilist.append(val)
		self.index = self.index + 1
		i = self.index - 1
		while i:
			if self.ilist[self.parent(i)] > self.ilist[i]:
				# Swapping parent with child if child value is less
				self.ilist[self.parent(i)], self.ilist[i] = self.ilist[i], self.ilist[self.parent(i)]
				i = self.parent(i)
			else:
				break

	def display(self):
		for i in range(0,self.index):
			print(self.ilist[i],',', end='')
		print()

	def findmin(self):
		if self.index:
			return self.ilist[0]
		else:
			# print("No element in heap")
			return None
	
	def SwapAndRecur(self, baap, bachha): # Used exclusively by heapify
		self.ilist[bachha], self.ilist[baap] = self.ilist[baap], self.ilist[bachha]
		if bachha < self.index:
			self.heapify(bachha)

	def heapify(self, i):
		leftchild = self.left(i)
		rightchild = self.right(i)
		if leftchild and not rightchild:
			if self.ilist[leftchild] < self.ilist[i]:
				self.SwapAndRecur(i, leftchild)
		if not leftchild and rightchild:
			if self.ilist[rightchild] < self.ilist[i]:
				self.SwapAndRecur(i, rightchild)
		if leftchild and rightchild:
			if min(self.ilist[leftchild], self.ilist[rightchild]) < self.ilist[i]:
				if self.ilist[leftchild] > self.ilist[rightchild]:
					self.SwapAndRecur(i, rightchild)
				if self.ilist[leftchild] <= self.ilist[rightchild]:
					self.SwapAndRecur(i, leftchild)


	def delete_min(self):
	# Find the minimum to return it later
		minimum = self.findmin()
	# Reduce the size of the index
		self.index -= 1
	# Replace the root with the last element of the heap
		#print(f"Before swapping elements\n{self.ilist}")
		self.ilist[self.index], self.ilist[0] = self.ilist[0], self.ilist[self.index]
		#print(f"After swapping elements\n{self.ilist}")
		self.ilist.pop()
		#print(f"After poping last element\n{self.ilist}")
	# Heapify the entire structure
		self.heapify(0)
	# Return the item back
		return minimum
		
bh = BinaryMinHeap()
a = [x for x in range(15)]
for i in a:
	bh.insert(i)
bh.display()
bh.delete_min()
bh.display()

