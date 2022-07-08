input_number=200000
mas_of_prime=[2]

def prime_numbers_below( max_number):
     for floating_int in range(2,max_number - 1):
            for j in mas_of_prime:
                if (floating_int) % j ==0:
                    break
                elif j == mas_of_prime [len (mas_of_prime) -1]:
                    mas_of_prime.append(floating_int)
prime_numbers_below(input_number)

print(mas_of_prime)