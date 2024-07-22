x=int(input())
y=int(input())
z=int(input())
if(x>=y) and (x>=z):
    largest=x
    print(x)
elif (y>=x) and (y>=z):
    largest=y
    print(y)
else:
    largest=z
    print(z)
           