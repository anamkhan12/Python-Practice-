def binarysearch(arr, i,h,key):
  if i> h : return -1

  mid = (i+h)//2
  if arr[mid] == key : return mid

  #for sorted array
  if arr[i] <= arr[mid]:
    if key >= arr[i] and  key <= arr[mid]:
      return binarysearch(arr,i,mid - 1, key) 
    return binarysearch(arr,mid + 1,  h, key)

  #for unsorted array
    if key >= mid and  key <= h:
      return binarysearch(arr,mid + 1,h, key) 
    return binarysearch(arr,i,mid - 1 ,key)

if __name__ == '__main__':
 
  t=int(input())
  for j in range(t):
    key = int(input())
    n = int(input())
    array = list(map(int, input().rstrip().split()))
    k=binarysearch(array,0,n - 1 ,key)
    if k != -1 : 
      print("Index:% d"% k)
    else:
        print('Key not found')
       
    def binarysearch(arr, i,h,key):
  if i> h : return -1

  mid = (i+h)//2
  if arr[mid] == key : return mid

  #for sorted array
  if arr[i] <= arr[mid]:
    if key >= arr[i] and  key <= arr[mid]:
      return binarysearch(arr,i,mid - 1, key) 
    return binarysearch(arr,mid + 1,  h, key)

  #for unsorted array
    if key >= mid and  key <= h:
      return binarysearch(arr,mid + 1,h, key) 
    return binarysearch(arr,i,mid - 1 ,key)

if __name__ == '__main__':
 
  t=int(input())
  for j in range(t):
    key = int(input())
    n = int(input())
    array = list(map(int, input().rstrip().split()))
    k=binarysearch(array,0,n - 1 ,key)
    if k != -1 : 
      print("Index:% d"% k)
    else:
        print('Key not found')
       
    

  

  