#Лаба_1 (1 задание)
arr = [10,20,None,40,50,60]
sum_=0
k=0
m=len(arr)
print(arr)
for i, value in enumerate(arr):
    if value:
        sum_ += value
    else:
        k = i
sar=sum_ / m
arr[k] = sar
print(arr)
