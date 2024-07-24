
#print the unique character in a string
vowels=['a',"e","i","o","u"] #or "aeiou"
consonet="bcdfghjklmnpqrstvwxyz"
ans=""
i="hello world"
inp=i.lower()
for i in inp:
    if(i not in ans):
        ans+=i
print(ans)        