input1=int(input())
input2=int(input())
arr=sorted(input2)
d=0
for i in range(input1):
    if 18-arr[i] in arr[i+1:] and arr[i]*(18-arr[i])>=d:
        d=arr[i]*(18-arr[i])
        x=[18-arr[i],arr[i]]
