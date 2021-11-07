class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, val):
        temp = Node(val)
        temp.next = self.top
        self.top = temp

    def pop(self):
        self.top = self.top.next


    def printstack(self):
        curr = self.top
        while curr != None:
            print(curr.data, "\b->", end=" ")
            curr = curr.next
        print("None")
                 
s1 = Stack()
s1.push(6)
s1.push(5)
s1.push(4)
s1.push(3)
s1.push(2)
s1.push(1)
s1.printstack()
s1.pop()
s1.pop()
s1.pop()
s1.printstack()
