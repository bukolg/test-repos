#Лаба_1
arr = [10,20,None,40,50,60]
sum=0
k=0
m=len(arr)
print(arr)
for i in range(m):
    if arr[i]:
        sum=sum+arr[i]
    else:
        k = i
sar=sum/(m-1)
arr[k] = sar
print(arr)