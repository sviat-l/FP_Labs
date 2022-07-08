text=input()
binar=int((text), base=2)
grey=binar^(binar>>1)
i=0
while text[i]!='1':
    i+=1
print('0'*i + bin(grey)[2:])