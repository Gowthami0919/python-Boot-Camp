def evensum(cls,input1,input2):
    x=input1[::-1]
    return sum([x[i] for i in range(input2) if i%2==0])