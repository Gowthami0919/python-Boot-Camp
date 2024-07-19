n=list(map(int,input().split(",")))
evencount=0
oddcount=0
for i in range(len(n)):
    if(n[i]%2==0):
        evencount+=1
    else:
        oddcount+=1
        
print(evencount)
print(oddcount)    
        