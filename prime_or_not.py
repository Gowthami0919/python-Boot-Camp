#write a program to print all the prime number in a given (between the num to num,printing all prime no.)
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
for i in range(a,b+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)     