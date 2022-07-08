average=error_check=0
for i in range(5):
    temp= int(input())
    if 100>=temp>=0 :
        average+=temp/5
    else:  error_check=1
    
if 90<=average<=100: 
    letter='A'
elif 82<=average<90:
    letter='B'
elif 75<=average<82:
    letter='C'
elif 67<=average<75:
    letter='D'
elif 60<=average<67:
    letter='E'
else:
    letter='F'
    
if error_check:
    print('None')
elif average == 0:
    print(f'Average grade = 0 -> F')
else:
    print(f'Average grade = {round(average,10)} -> {letter}')