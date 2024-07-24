#sum of digits in a string
i="hello123world"
check="0123456789"
ans=0
inp=i.lower()
for i in inp:
      if (i in check):
          ans+=int(i)
          
print(ans)  




    