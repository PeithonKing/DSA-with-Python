from random import randint

def partition(iL, low , high):
    '''
    Our aim is to find a position for the pivot element such that
    all the elements lower than it lies on its left and
    all the elements higher or equal to it lies on its right.
    
    Finally it returns the position of the pivote element.
    '''
    pivot = iL[high] # Defining pivot element (last element here)
    # print("Pivot = ", pivot)
    i = low # This is the pointer, this will move forward and...
    # ...depict the place where the pivot element should be placed.
    for j in range(low, high):
        # If jth element < pivot, swap jth element with pointer
        if iL[j] < pivot:
            iL[j], iL[i] = iL[i], iL[j]
            # print(f"swapped positions {compare} and {j}.")
            # print(iL)
            i += 1 # Pointer is moved forward
    iL[i], iL[high] = iL[high], iL[i] # swapping pivote element to its correct position
    # print(f"swapped (pivote) positions {compare} and {high}.")
    # print(iL)
    return (i)

def QuickSort(iL, low , high):
    if low < high:
        # Get pivot position from partition
        pp = partition(iL, low, high)
        # Quicksort on left
        # print(f"Calling quickSort on left from positions {low} to {pp-1}")
        QuickSort(iL, low, pp-1)
        # quicksort on right
        # print(f"Calling quickSort on right from positions {pp+1} to {high}")
        QuickSort(iL, pp + 1, high)

a = []
while len(a) < 10:
	f = randint(1,20)
	if f not in a:
		a.append(f)
print(a)
QuickSort(a, 0, len(a)-1)
print(a)
