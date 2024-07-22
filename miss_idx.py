my_list=list(map(int,input().split(" ")))
n=int(input())
total=n*(n+1)//2
sum=0
for i in range(0,len(my_list)):
    sum+=my_list[i]
print(total-sum)