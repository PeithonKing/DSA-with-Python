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

    def steps(self): # Used for printing, display function
        j = 1
        k = 1
        while self.index > k:
            k += 2**j
            j += 1
        return j

    def twos(self, n): # Used for printing, display function
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
a = [11,9,1,12,14,5,8,15,30]
bh.insert(11)
bh.insert(5)
bh.insert(16)
bh.delete_min()
bh.insert(21)
bh.display(True)
bh.insert(1)
bh.insert(31)

bh.display(True)

