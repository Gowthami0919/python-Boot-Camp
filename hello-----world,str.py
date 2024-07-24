#hello-----world
#hello---wor--ld 
# //hifi(-) should be front outward of the string
#-----hello world

inp=input()
count=0
ans=""
for i in inp:
    if(i=="-"):
        count+=1
    else:
        ans=ans+i   
print("-"*count+ans )
    
    