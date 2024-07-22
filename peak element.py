#peak element (imp)
#n=list(map(int,input().split()))
#count=0
#for i in range(1,len(n)-1):
    #if n[i]>n[i-1] and n[i]>n[i+1]:
        #count=i
        #break
#print(n[count])

#or for more than one peak value in a list
n=list(map(int,input().split()))
count=0
for i in range(1,len(n)-1):
    if n[i]>n[i-1] and n[i]>n[i+1]:
        print(n[i],end=" ")

#break is use to stop
#sample testcase1-
#5 12 8 17 -2
#12
#sample testcase2-
#5 12 8 17 -2
#12 17