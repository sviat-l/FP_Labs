exponent=int(input())
num_0=num=5**(exponent)
hamming_weight=0

while num>0:
    if  num&1:
        hamming_weight+=1
    num= num>>1

    
if hamming_weight%2==0:
    type='evil number'
else: type= 'odious number'

print(f'Number {num_0} is {type}. Its hamming weight is {hamming_weight}.')   
