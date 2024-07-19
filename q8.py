p=list(map(int,input().split(" ")))
sum=0
count=0
n=len(p)
for i in range(len(p)):
    if(i%2==0):
        sum+=p[i]
        count+=1        
print(sum/i)        
