year=int(input())
c=year//100
expact=(8+(c//4)-c+ ((8*c+13)//25)+11*(year%19))%30
print(expact)