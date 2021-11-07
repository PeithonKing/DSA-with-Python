# NOTIFY ME IF THERE ARE ANY BUGS HERE

class Node:
	def __init__(self,val):
		self.data = val
		self.next = None
		
class Linkedlist:
	def __init__(self):
		self.head = None 	# Stores the first element.

	def insertatbeg(self, val):
		temp = Node(val)
		temp.next = self.head
		self.head = temp
	
	def insertatend(self, val):
		temp = Node(val)
		curr = self.head
		while curr.next != None:
			curr = curr.next
		curr.next = temp

	def insertatk(self, k, val):
		temp = Node(val)
		if k > 0:
			curr = self.head
			for i in range(k-1):
				curr = curr.next
			hist = curr.next
			curr.next = temp
			temp.next = hist
		else:
			temp.next = self.head
			self.head = temp

	def removeatk(self, k):
		if k > 0:
			curr = self.head
			for i in range(k-1):
				curr = curr.next
			br = curr
			for i in range(2): curr = curr.next
			br.next = curr
		else:
			self.head = self.head.next

	def printlist(self):
		curr = self.head
		while curr != None:
			print(curr.data, "\b->", end=" ")
			curr = curr.next
		print("None")

linkedlist1 = Linkedlist()

linkedlist1.insertatbeg(2)
linkedlist1.insertatbeg(1)
linkedlist1.insertatend(3)
linkedlist1.insertatend(4)
linkedlist1.printlist()
linkedlist1.insertatk(0, "a")
linkedlist1.printlist()
linkedlist1.removeatk(0)
linkedlist1.printlist()
linkedlist1.removeatk(3)
linkedlist1.printlist()
