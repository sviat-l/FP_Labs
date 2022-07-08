n=int(input())
multi=1
for i in range(n+1):
    if i%7!=0:
        multi*=i
print(multi)
