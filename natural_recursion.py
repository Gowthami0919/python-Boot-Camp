#some of first n natural number using recursion 

n=int(input('enter n value:'))
def my_function(n):
    if n==0:
        return 0
    return my_function(n-1)+n
answer=my_function(n)
print(answer)    