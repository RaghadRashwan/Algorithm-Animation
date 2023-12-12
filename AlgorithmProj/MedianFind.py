def partition(arr, low, high,q):
   i = (low-1)     # index of smaller element
   #R eplacing the value of the pivot with the value in 
   #the last index of the opinion
   arr[high], arr[q] = arr[q], arr[high]
   # Put the value of the last index in a variable Pivo
   pivot = arr[high]
   # The j element is the current element to be arranged &
   #the for start condition is this value is in range
   for j in range(low, high):

       # If current element is smaller than or equal to pivot
       # increment index of smaller element
       if arr[j] <= pivot:
           i = i+1 
           # Replace the value of element j with the value of element i = index
           # with the value of element i = index 
           arr[i], arr[j] = arr[j], arr[i]  
                                        #for the smallest element of the array
 # If the pivot value is less than the value of j, replace the pivot 
 #value with an index value of i+1
   arr[i+1], arr[high] = arr[high], arr[i+1]  
   return (i+1)

def Select(arr, l, r, k):
 
     # if k is smaller than number of elements in array
     #  print(k)
    if (k > 0 and k <= r - l + 1):
 
        # Partition the array around last element and get position of pivot
        # element in sorted array
        # print(l,"  ",r," ")
        index = partition(arr, l, r, r)
 
        # if position is same as k
        if (index - l == k - 1):
            return index
 
        # If position is more, recur for left subarray
        if (index - l > k - 1):
            return Select(arr, l, index - 1, k)
 
        # Else recur for right subarray
        return Select(arr, index + 1, r,
                            k - index + l - 1)
    print("Index out of bound")

def quickSelect(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        p=Select(arr,low ,high,int((high-low)/2 +1) )
        pi = partition(arr, low, high,p)
        # Separately sort elements before
        # partition and after partition
        quickSelect(arr, low, pi-1)
        quickSelect(arr, pi+1, high)
