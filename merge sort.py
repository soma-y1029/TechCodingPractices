# takes one argument to be sorted
def margesort(nums): 
    if len(nums) < 2: return
    
    # divide phase
    mid = len(nums)//2 # find middle of the array
    left, right = nums[:mid], nums[mid:] # split to left and right parts
    margesort(left)
    margesort(right)
    
    # conquer phase
    i = j = k = 0 # left, right, nums index
    while i < len(left) and j < len(right): # loop while i and j are in the range 
        if left[i] < right[j]: # left[i] is smaller, put left[i] to k in nums
            nums[k] = left[i]
            i += 1 # increment index for i
            
        else: # right[j] is equals to or larger than left[i], put right[j] to k in nums
            nums[k] = right[j]
            j += 1 # increment index for j
        k += 1 # increment k for either cases
    
    # do for remainings if any
    while i < len(left): # exhausts i if any
        nums[k] = left[i]
        i += 1; k += 1 # increment both indecies

    while j < len(right): # exhausts j if any
        nums[k] = right[j] 
        j += 1; k += 1 # increment both indecies
        
    return nums
    

print(margesort([12, 11, 13, 5, 6, 7]))
