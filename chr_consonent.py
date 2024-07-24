#print all the vowels followed by consonent 
i="gowthami"
vowels=['a',"e","i","o","u"] #or "aeiou"
consonet="bcdfghjklmnpqrstvwxyz"
ans=" "
inp=i.lower()
for i in inp:
      if (i in vowels):
          ans+=i
print(ans,end=" ")
for i in inp:
      if (i in consonet):
          ans+=i          
print(ans,end=" ")
