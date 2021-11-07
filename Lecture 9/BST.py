class Node:
	def __init__(self, val):
		self.data = val
		self.parent = None
		self.left = None
		self.right = None

class BST:
	def __init__(self):
		self.root = None

	def searchU(self,val, show = True):
		pos = self.search(val,self.root)
		if pos:
			if show:
				print(f"Yes, {val} exists in this tree.")
			return pos
		else:
			if show:
				print(f"No, {val} does not exist in this tree.")
			return None
			

	def search(self,val,curr):
		if curr is None or curr.data == val:
			return curr
		elif val > curr.data:
			return self.search(val, curr.right)
		else:
			return self.search(val, curr.left)

	def insertU(self,val):
		print(f"Trying to insert {val}.")
		temp = Node(val)
		if self.root:
			res = self.insert(val, self.root)
			if res:
				print(f"Succesfully inserted {val} to Tree!\n")
				if val > res.data:
					temp.parent = res
					res.right = temp
				elif val < res.data:
					temp.parent = res
					res.left = temp
		else:
			self.root = temp
			print(f"Succesfully inserted {val} to Tree!\n")

	def insert(self, val, curr):
		if curr.data == val:
			print("Element already exists in tree!\n")
			return None
		elif val > curr.data:
			if curr.right:
				return self.insert(val, curr.right)
			else: return curr
		elif val < curr.data:
			if curr.left:
				return self.insert(val, curr.left)
			else: return curr
		
	def GonL(self, n): #Finds Greatest element on left
		curr = n.left
		while curr.right:
			curr = curr.right
		return curr
			
	def remove(self,val):
		if self.root:
			print(f"Trying to remove {val}.")
			ele = self.searchU(val, False)
			if ele:
				if ele.left and ele.right: # If BOTH child exists
					floor = self.GonL(ele)
					ele.data = floor.data
					if floor.left:
						ele.left = floor.left
						# floor.parent = None # No need to do this. 
						# Reason:- once we move out of this,
						# floor will be lost anyway.
					if floor.data == floor.parent.data:
						floor.parent.left = None
					else: floor.parent.right = None
				elif ele.left or ele.right:
					# If any one child exists
					if ele.parent:
						if ele.parent.left == ele: # if ele is the left child
							if ele.right: 
								ele.parent.left = ele.right
								ele.right.parent = ele.parent
							else: 
								ele.parent.left = ele.left
								ele.left.parent = ele.parent
						else: # if ele is the right child
							if ele.right: 
								ele.parent.right = ele.right
								ele.right.parent = ele.parent
							else: 
								ele.parent.right = ele.left
								ele.left.parent = ele.parent
								
					else:
						if ele.right: self.root = ele.right
						else: self.root = ele.left
				else:
					if ele.parent:
						if ele.parent.left == ele: # if ele is the left child
							ele.parent.left = None
						else: # if ele is the right child
							ele.parent.right = None
					else:
						self.root = None
				print("Removed Successfully")
			else:
				print(f"{val} does not exist in tree")
		else: print("Tree is empty!")

	def displayU(self, details = False):
		if details:
			self.details(self.root)
		else:
			self.displayinOrder(self.root)
			print("\b\b  ")

	def details(self, curr):
		if curr:
			self.details(curr.left)
			if curr.parent: p = curr.parent.data
			else: p = None
			if curr.left: l = curr.left.data
			else: l = None
			if curr.right: r = curr.right.data
			else: r = None			
			print(f"data = {curr.data}, Parent = {p}, left = {l}, right = {r}")
			self.details(curr.right)
	
	def displayinOrder(self, curr):
		if curr:
			self.displayinOrder(curr.left)
			print(curr.data, end= ", ")
			self.displayinOrder(curr.right)
	
	

# from random import randint
a = [5,3,6,4,2,1,2.5,3.5,4.5,5.5,1.5]
t = BST()
for i in a:
	t.insertU(i)
t.displayU()
t.displayU(True)
t.searchU(5)

print()
t.remove(1)
t.displayU()
t.displayU(True)
