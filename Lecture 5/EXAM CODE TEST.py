class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.head = None # Stores the first element.

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
            try:
                curr = self.head
                for i in range(k-1):
                    curr = curr.next
                hist = curr.next
                curr.next = temp
                temp.next = hist
            except: print("Invalid Input: We do not have that many places, try with a shorter value of k!")
        elif k == 0:
            temp.next = self.head
            self.head = temp
        else: print("Invalid Input: Negative numbers are not expected!")

    def removeatk(self, k):
        if k > 0:
            try:
                curr = self.head
                for i in range(k-1):
                    curr = curr.next
                br = curr
                for i in range(2): curr = curr.next
                br.next = curr
            except: print("Invalid Input: We do not have that many places, try with a shorter value of k!")
        elif k == 0:
            self.head = self.head.next
        else: print("Invalid Input: Negative numbers are not expected!")


    def printlist(self):
        curr = self.head
        while curr != None:
            print(curr.data, "\b->", end=" ")
            curr = curr.next
        print("None")
        
List1 = Linkedlist()
List2 = Linkedlist()

L1 =[d for d in range(10,1,-2)]
# print(L1)
L2 =[d for d in range(11,2,-2)]
# print(L2)
for i in L1:
	List1.insertatbeg(i)
for i in L2:
	List2.insertatbeg(i)

List1.printlist()
List2.printlist()
print()
while List2.head:
	val = List2.head.data
	curr = List1.head
	n = 0
	#List1.printlist()
	#List2.printlist()
	#print()
	while True:
		if curr:
			#print(curr.data)
			if curr.data < val:
				n += 1
				curr = curr.next
			else:
				List1.insertatk(n, val)
				break
		else:
			List1.insertatk(n, val)
			break
	List2.removeatk(0)
	

List1.printlist()
List2.printlist()
