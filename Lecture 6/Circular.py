class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

class Clinklist:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_begin(self, val):
        temp = Node(val)
        if self.tail == None:
            self.tail = temp
        prvH = self.head
        self.head = temp
        if prvH: temp.next = prvH
        else: temp.next = self.head

    def insert_end(self, val):
        temp = Node(val)
        self.tail.next = temp
        self.tail = temp
        temp.next = self.head

    def insert_k(self, k, val):
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

    def remove_k(self, k):
        if k > 0:
            curr = self.head
            for i in range(k-1):
                curr = curr.next
            br = curr
            for i in range(2): curr = curr.next
            br.next = curr
        else:
            self.head = self.head.next

    def remove_beg(self):
        Clinklist.remove_k(self, 0)

    def remove_end(self):
        curr = self.head
        while curr.next != self.tail:
            curr = curr.next
        self.tail = curr
        curr.next = self.head

    def printlist(self):
        curr = self.head
        if self.head != None:
            while curr != self.tail:
                print(curr.data,"\b->",end = " ")
                curr = curr.next
            print(curr.data,"\b->",end = " Head\n")
        else:
            print(self.head)

Clinklist1 = Clinklist()

Clinklist1.insert_begin(2)
Clinklist1.insert_begin(1)
Clinklist1.insert_end(3)
Clinklist1.insert_end(4)
Clinklist1.insert_end(5)
Clinklist1.insert_end(6)
Clinklist1.insert_end(7)
Clinklist1.printlist()
Clinklist1.insert_k(0, "a")
Clinklist1.printlist()
Clinklist1.remove_k(0)
Clinklist1.printlist()
Clinklist1.remove_k(4)
Clinklist1.printlist()
Clinklist1.remove_k(3)
Clinklist1.printlist()
Clinklist1.remove_beg()
Clinklist1.printlist()
Clinklist1.remove_end()
Clinklist1.printlist()
