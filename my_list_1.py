#my list dynamic
my_list=list(map(str,input().split(",")))
choice=int(input())
if(choice==1):
    my_list.append(4)
    print(my_list)
elif (choice==2):
    my_list.pop(2)
    print(my_list)  
elif( choice==3):
    my_list.sort()
    print(my_list) 
else:
    l=len(my_list)
    print("hello",l)  
