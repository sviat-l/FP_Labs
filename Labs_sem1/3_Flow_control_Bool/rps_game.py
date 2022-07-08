text=input()
results=[]
while text:
    if text[0]==text[1]:
        results.append('False | False')
    elif text=='RS' or text=='PR' or text=='SP':
        results.append('True')
    else:
        results.append('False')
    
    text = (input())

for result in results:
    print(result)

        
        


