l=['user1','user2','user3','user4','user5']
is_present=False
for name in l:
    if name=='user3':
        is_present = True
        break
if is_present== True:
    print('user3 is present in the list!')
else:
    print('user3 is not present im the list!')