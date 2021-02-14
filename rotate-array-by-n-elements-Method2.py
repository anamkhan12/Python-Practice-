def main():
    t = int(input())
    for _ in range(t):
        temp = input().split(" ")
        temp = list(filter(None, temp))
        n=0
        d=0
        if len(temp)==2:
            n = int(temp[0])
            d = int(temp[1])
        else:
            n= int(temp[0])
            d = int(input())
        temp = input()
        temp2 = filter(None, temp.split(' '))
        A = list(map(lambda x:int(x), temp2))
        foo(A,d)

def foo(A,d):
    ans = A[d:]+A[:d]
    ans = map(lambda x:str(x), ans)
    print(" ".join(ans))

main()