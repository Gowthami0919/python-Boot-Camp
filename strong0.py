sum=0
num=int(input("enter a no."))
while(num):
    fact=1
    rem=num%10
while(i<rem):
    fact=fact*i
    i=i+1
    sum=sum+fact
    num=num/10
if(num):
    print("given no. is a strong no.")
else:
    print("given no. is not a strong no.")
