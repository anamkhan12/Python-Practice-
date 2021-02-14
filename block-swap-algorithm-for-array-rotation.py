def swap(arr, fi, si, d):
  for i in range(d):
      temp = arr[fi + i];
      arr[fi + i] = arr[si + i];
      arr[si + i] = temp;

def leftRotate(arr, d, n): 
  if(d == 0 or d == n): 
    return; 
  i = d 
  j = n - d 
  while (i != j): 
        
    if(i < j): 
      swap(arr, d - i, d + j - i, i) 
      j -= i    
    else: # B is shorter
      swap(arr, d - i, d, j) 
      i -= j 
  swap(arr, d - i, d, i)
def printArray(arr, size):
    for i in range(size):
        print(arr[i], end = " ");
    print();
 


if __name__ =='__main__':
  nd = input().split()
  n = int(nd[0])
  d = int(nd[1])
  array = list(map(int, input().rstrip().split()))
  leftRotate(array,d,n)
 