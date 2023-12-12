import random 


def findKthLargest( nums , k , low ,high):
    return select(nums, low, high, k)

#Simple partition code to partition using last element 
def partition(A,start, end):
    if start==end:
        return start
    pivot = A[end]
    i = start - 1
    for j in range(start, end):
        if A[j] < pivot:
            i+=1
            A[i], A[j] = A[j], A[i]

    A[end],A[i+1] = A[i+1], A[end]

    return i+1

#Partition for random pivot
def partition_r(A, start, end):
    randpivot = random.randrange(start, end)
    A[end], A[randpivot] = A[randpivot], A[end]
    return partition(A, start, end)

#Partition on a particular pivot with index pivotIndex
def partition_custom( A, start, end, pivotIndex):
    A[end], A[pivotIndex] = A[pivotIndex], A[end] #swapping the lasst element index with the pivot index
    return partition(A, start, end) 




#We write code to find median of 5 elements in 6 comparisions. This is O(1)
def find_median_5_elements( A, start):
    if A[start]>A[start+1]:
        A[start] , A[start+1] = A[start+1], A[start]

    if A[start+3] > A[start+4]:
        A[start+3], A[start+4] = A[start+4], A[start+3]

    if A[start]>A[start+3]:
        A[start], A[start+3] = A[start+3], A[start]
        A[start+1], A[start+4] = A[start+4], A[start+1]

    if A[start+2] > A[start+1]:
        if A[start+1] < A[start+3]:
            return min(A[start+2], A[start+3])
        else:
            return min(A[start+2], A[start+4])
    else:
        if A[start+2] > A[start+3]:
            return min(A[start+2],A[start+4])
        else:
            return min(A[start+1],A[start+3])

#Array A starting from p till r. We find the kth largest element
def select(A, p, r, k):
    
    #If startposition is same as end, we return the same element
    if p>=r:
        return A[p]
    
    #We'll partition the array from p to r using median of medians
    #divide into n/5 groups, each groups has 5 elemnts
    number_of_groups = (r-p)//5
    
    #If we have atleast 1 group, we go ahead with median of medians partition. Else, we just pivot with random element
    if number_of_groups>1: #base case
        medians = []
        for i in range(number_of_groups):
            median = find_median_5_elements(A[(p + i*5) : (p + i*5 + 5)], 0)
            medians.append(median)

        pivot_element = select(medians, 0, len(medians) - 1, len(medians) // 2)# the recurion will stop whene the base case become number of groubs less then 1 
        
        #We have the pivot element but not the index.
        pivot_index = p

        for i in range(p, r):
            if A[i] == pivot_element:
                pivot_index = i

        q =partition_custom(A, p, r, pivot_index)

    else:
        # When numbers of elemnts is too small for median of medians
        q = partition_r(A, p, r)
    

    #Let's assume x is the position from end where q is pivoted
    x = r-q+1 #to find the median position

    #If position of x is the same what we need, we just return it
    if x==k: return A[q]
    
    #If the current position is on right side of what we need, we search towards left
    #Here, we want find k-x position as we now considering the the largest element from x (We have already searched x positions)
    if k>x: return select(A, p, q-1,k-x)
    
    #If the current position is on left side of what we need, we search towards right
    if k<x: return select(A,q+1,r,k)
def quickRandomSelect(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
       # pi is partitioning index, arr[p] is now
        # at right place
        p=arr.index(findKthLargest(arr,low ,high,int((high-low)/2 +1) ))#find the pivot based on the array elemnt 
        arr[high],arr[p]=arr[p],arr[high]
        pi = partition(arr, low, high)
        # Separately sort elements before
        # partition and after partition
        quickRandomSelect(arr, low, pi-1)
        quickRandomSelect(arr, pi+1, high)

def generateRandomArray(n): 
    A=[]
    for i in range(1, n + 1): 
         A.append(random.randint(1, 300) )
    return A 


def saveArray(filename,arr):
    fileToBeWrittenTo = open(filename,"w") 
    for i in range(0, len(arr) - 1): 
         fileToBeWrittenTo.write(str(arr[i])+"\n") 
         
         
t = "Cs&"*3
print("t"+t)

print(oct(365))

print("umm '\n 'erry")