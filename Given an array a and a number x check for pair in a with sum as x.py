def pairInSortedRotated( arr, n, x ): 
  
      
    l = 0
    r = n-1
    while(l<r):
        if arr[l] + arr[r] == x :
           return 1
        if (arr[l] + arr[r] < x ): 
            l = l + 1
        else: 
            r = r - 1
    return 0
    
  
def quickSort(A, start, end):
    if start < end:
        pivot = partition(A, start, end)
        quickSort(A, start, pivot-1)
        quickSort(A, pivot + 1, end)

def partition(A, start, end):
    x = A[end]
    k = (start-1)
    for j in range(start, end):
        if A[j] <= x:
            k += 1
             
            A[k], A[j] = A[j], A[k]
 
        A[k + 1], A[ei] = A[end], A[k + 1]
         
    return k + 1
     
A = [ 1, 4, 45, 6, 10, 8 ]
n = 16
arr_size = len(A)
if (pairInSortedRotated(A, len(A), n)):
    print("Array has two elements with the given sum")
else:
    print("Array doesn't have two elements  with the given sum")

      