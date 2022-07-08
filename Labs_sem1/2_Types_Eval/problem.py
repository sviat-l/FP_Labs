input_text=input()
    # функція для перевірки простоти числа
def prime_checker(number):
    if number==2: 
        return True
    for i in range(2 , round(number**0.5)+1):
        if number%(i)==0:
            return False
    return True 

def lowest_prime(input_number):
       for i in range (2, input_number - 1 ):
            if input_number% (i)!=0:
                if prime_checker(i)==True :
                 return(i)

    # перебір усіх символів            
for symbol in input_text:
    if ord(symbol)> 57   or ord(symbol)<48:
        print('Error')
        exit()

if int(input_text) <3 :
        print('Error')
else: print( lowest_prime( int(input_text))) 

#   метод через try-except
    #try:
    #    if int(input_text)<3 :
    #    print('Error')
    #    else: lowest_prime( int(input_text)) 
    #except ValueError:
    #   print('Error')
