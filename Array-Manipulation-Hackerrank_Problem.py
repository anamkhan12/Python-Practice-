

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    array =[0] * (n+1)
    for value  in queries:
      a = value[0] -1
      b = value[1]
      k= value[2]
      array[a] += k
      array[b] -= k
    max =0
    count =0
    for i in array: 
      count +=i
      if count > max:
        max = count      
    return max

if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(result)