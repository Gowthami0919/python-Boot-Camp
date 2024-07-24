
#i="gowthami"
#check=['a',"e","i","o","u"]
#count=0
#inp=i.lower()
#for i in inp:
      #if (i in check):
          #count+=1
#print(count)

#write a program to count a consonet and vowels in a string 
vowels=['a',"e","i","o","u"] #or "aeiou"
consonet="bcdfghjklmnpqrstvwxyz"
count_vowels=0
count_consonet=0
inp="hello world"
inp=inp.lower()
for i in inp:
      if (i in vowels):
          count_vowels+=1
for i in inp:
    if(i in consonet):
        count_consonet+=1
              
print(count_vowels)
print(count_consonet)
