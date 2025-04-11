num=int(input())
f=[1,1]
for N in range(2,num+1):
    value=(f[N-1]*f[N-1]+f[N-2]*f[N-2])%47
    f.append(value)
print(f[-1])