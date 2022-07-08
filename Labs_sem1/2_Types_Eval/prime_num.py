input_number=int(input())
mas_of_prime=[2,3]

def prime_numbers_below( max_number):
     for floating_int in range(4, max_number + 1)  :
         x=floating_int**0.5
         for j in range(len(mas_of_prime) -1):
            if mas_of_prime[j] < x:
                if (floating_int) % mas_of_prime[j] ==0:
                    break
                elif mas_of_prime[j+1] > x:
                     mas_of_prime.append(floating_int)
prime_numbers_below(input_number)
print(mas_of_prime)