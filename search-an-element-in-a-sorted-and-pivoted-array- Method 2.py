for i in range(int(input())):
  a=int(input())
  n=int(input())
  l=list(map(int,input().split()))
  if(a in l):
    print(l.index(a))
  else:
    print(-1)