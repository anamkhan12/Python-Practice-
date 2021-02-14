
def cyclicallyrotate(array,n):
  temp_last= array[n-1]
  for i in range(n-1,0,-1):
    array[i]=array[i-1]
  array[0] = temp_last

def printRotatedArray(array,n):
    for i in range(n):
        print("% d" % array[i],end=" ")
    print()
t=int(input())
for i in range(t):
    n = int(input())
    array = list(map(int, input().rstrip().split()))
    cyclicallyrotate(array,n)
    printRotatedArray(array,n)
    
    