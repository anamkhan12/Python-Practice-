test_list = [(1, 4, 3, 5), (6,7, 8), (2, 4, 10)] 
  
# printing list  
print("The original list : " + str(test_list))  
  
# Mathematical Median of Cumulative Records  
# Using loop + "~" operator  
res = [] 
for sub in test_list : 
  for ele in sub : 
    res.append(ele)
res.sort()
mid = len(res) // 2
print(res)
print(mid)
x= mid+1
res = (res[mid] + res[~mid]) / 2
 # res = (res[mid] + res[mid-1]) / 2  
# Printing result  

print("Median of Records is : " + str(res))  