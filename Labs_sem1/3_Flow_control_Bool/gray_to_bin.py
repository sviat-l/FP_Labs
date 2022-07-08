grey_str = input()
code_str=grey_str[0]
for i in range(1,len(grey_str)):
    code_str+= str(int(code_str[i-1]) ^ int(grey_str[i]))
print(code_str)