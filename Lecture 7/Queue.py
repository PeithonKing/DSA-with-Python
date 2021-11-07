LOL = {}
pb = ""
curses=["Told You not to remove the first element!",
		"Ahh! I see... your aim is to crash me!",
		"Why are you doing this to a sweet little program like me!",
		"Stop torturing me man!! I beg you!!",
		"Enough! You wont stop untill I crash. Ok, I will crash next time!",
		"RIP! This program crashed finally! Now press 'q' and leave me alone!"]
c = 0

instructions = '''Command Help:- 

Things inside curly brackets ({}) have to be replaced with inputs!
(Curly Brackets also have to be replaced)

{Qname} denotes the name of the Queue and takes only lowercase values!
1) "Start {Qname} {val}": 	Starts a Queue with a name and starting value(val).
2) "enqueue {Qname} {val}":     Adds a member to the queue.
3) "dequeue {Qname}":           Removes a member from the queue.
4) "printf {Qname}":            Prints the queue.
5) "printb {Qname}":             Prints the queue.
6) "print {Qname}":             Prints the queue.
7) "help":			Shows this message!
8) "q": 			End Program!

Note:-  Code is not Case Sensitive! 
	All input are stored as lower case roman letters
	("A" cannot be stored till now. Feature will be added in next update!)
	Counting of k starts from 0.
	Please Do not try to remove the first element of the queue.
'''

class Node:
	def __init__(self,val):
		self.data = val
		self.next = None
		
class Queue:
	def __init__(self):
		self.front = None
		self.end = None
	
	def enqueue(self, val):
		temp = Node(val)
		temp.next = self.end
		self.end = temp
		if self.front == None:
			self.front = temp

	def dequeue(self):
		curr = self.end
		if curr.next:
			while curr.next != self.front:
				curr = curr.next
			self.front = curr
			curr.next = None
			print(f"Removed an element!")
		else:
			global c
			print(curses[c%6])
			c += 1

	def printqueue(self):
		curr = self.end
		print("End | ", end = "")
		while curr != None:
			print(curr.data, end = " | ")
			curr = curr.next
		print("Front")
		
	def printb(self, curr):
		global pb
		if curr.next:
			Queue.printb(self, curr.next)
		pb += "| " + str(curr.data) + " "
			
	def printback(self):
		global pb
		pb = "Front "
		Queue.printb(self, self.end)
		pb += " | End"
		print(pb)


print(instructions)
while True:
	command = input("\nEnter Command: ").lower().strip()

	if command == "q":
		break

	elif command == "help":
		print("\n" + instructions)

	elif command.startswith("start"):
		try:
			_, Qname, val = command.split()
		except:
			print("Incomplete Input!")
			continue
		LOL[Qname] = Queue()
		LOL[Qname].enqueue(val)
		print(f"Queue {Qname} started and value of first element is {val}.")

	elif command.startswith("enqueue"):
		try:
			_, Qname, val = command.split()
			if Qname not in LOL.keys():
				print("No such list exists!")
				continue
		except:
			print("Incomplete Input!")
			continue
		LOL[Qname].enqueue(val)
		print(f"{val} added to {Qname}.")

	elif command.startswith("dequeue"):
		try:
			_, Qname = command.split()
			if Qname not in LOL.keys():
				print("No such list exists!")
				continue
		except:
			print("Incomplete Input!")
			continue
		LOL[Qname].dequeue()
		if c == 8:
			print("Too many bad inputs! So I decided to shut down!")
			break

	elif command.startswith("print"):
		try:
			_, Qname = command.split()
			if Qname not in LOL.keys():
				print("No such list exists!")
				continue
		except:
			print("Incomplete Input!")
			continue
		if _ == "printf": LOL[Qname].printqueue()
		elif _ == "printb": LOL[Qname].printback()
		else:
			LOL[Qname].printqueue()
			LOL[Qname].printback()

	else: print("Command not found!")
