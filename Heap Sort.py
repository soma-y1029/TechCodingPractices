def maxheapify(arr, size, p): 
    largest = p
    l, r = 2*p+1, 2*p+2
    if l < size and arr[largest] < arr[l]: largest = l
    if r < size and arr[largest] < arr[r]: largest = r
    if largest != p: 
        arr[p], arr[largest] = arr[largest], arr[p]
        maxheapify(arr, size, largest) 

def maxheapsort(arr): 
    n = len(arr)
    # buid heap tree
    for p in reversed(range(n//2)):
        maxheapify(arr, n, p)
        
    # extract from top and do for rest of nodes
    for i in reversed(range(n)): 
        arr[0], arr[i] = arr[i], arr[0]
        maxheapify(arr, i, 0) # heapify from top but excludes sorted tails (i is decreasing)
    
    return arr
