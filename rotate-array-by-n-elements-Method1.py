
def single_rotation(array,n):
    temp =array[0]
    for i in range(n-1):
        array[i]=array[i+1]
    array[i+1]=temp
def leftRotation(array,d,n):
    for i in range(d):
        single_rotation(array,n)
    
def printRotatedArray(array,n):
    for i in range(n):
        print("% d" % array[i],end=" ")
    print()
t=int(input())
for i in range(t):
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    array = list(map(int, input().rstrip().split()))
    leftRotation(array,d,n)
    printRotatedArray(array,n)