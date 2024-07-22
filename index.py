my_list=list(map(int,input().split(" ")))
k=int(input())
n=int(input())
if(len(my_list)<k+n):
    print("error")
else:
    for i in range(len(my_list)):
        print(my_list[k+n],end="")
        break
        
        
        