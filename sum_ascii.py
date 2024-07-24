#sum using ascii values
a="abc12345" #or a=input() 
sum=0
for i in a:
    if(ord(i)>=48 and ord(i)<=57): #65 to 90 are to check capital letters
        sum+=int(i)
print(sum)   
#48 to 57 are to check number
#ord(a)==97 X,ord(b)==98 X,ord(c)==99 X,             sum=0+1=1
# ord(1)==49>48 and <=57,ord(2)==50 V,sum=0+1         sum=2+1=3
#sum=3+3=6


#sum using string
#a="gowthami123"
#sum=0
#for i in a:
    #if(i.isdigit()):
        #sum+=int(i)
#print(sum)     