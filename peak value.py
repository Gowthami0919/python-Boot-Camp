#checking the array if the peak value exits in corner 
n=list(map(int,input().split()))
count=0
for i in range(1,len(n)-1):
    if n[i]>n[i-1] and n[i]>n[i+1]:
        count=i
if(n[-1]>n[-2] and n[i]>count):
    count=len(n)-1
print(n[count])    