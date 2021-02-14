def sumElement(arr,n):
    totalsum=0
    if n == 0:
        return 0
    else:
       
       for i in range(n):
          totalsum += arr[i]
       return totalsum
if __name__ == '__main__':
  testcase =int(input())
  for _ in range(testcase):
    n=int(input())
    for x in input().split():
      print(x)
      arr=[x]
    print(arr)
    print(sumElement(arr,n))