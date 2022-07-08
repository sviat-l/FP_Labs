import math

def Leibniz_pi_calculation_(iterations):
    starting_number=sign=1
    pi=0
    for i in range(iterations):
        pi+= 4/starting_number * sign
        starting_number+=2
        sign=-sign
    return pi
     
def Leibniz_Gregory_Madhava_method():
    print('\n\n\n    Leibniz-Gregory-Madhava method' )
    log_num_of_iterations=8
    #num_of_iterations= int(input('\nЗагальна кількість ітерацій 10**')) +1
    print ( '\niterations          pi_result     difference')
    for exponent in range(1,log_num_of_iterations+1):
        iterations=10**exponent
        pi_result =Leibniz_pi_calculation_(iterations)
        difference= pi_result - math.pi 
        print ( "%9i  %4s   %.10f  %.10f" % (iterations,f'10^{exponent}' ,pi_result, difference))

def Archimedes_pi_calculation (max_side_number):
    side_length_square=2  
    for poligons in range(max_side_number):
        num_of_sides=4*2**poligons
        pi_result =num_of_sides * math.sqrt(side_length_square)/2
        difference=pi_result-math.pi
        print ( "%8i   %.12f  %.12f" % (num_of_sides, pi_result,difference))
        side_length_square= side_length_square/4 + (1 - math.sqrt(1-side_length_square/4))**2

def Archimedes_method ():
    print('\n\n\n           Archimedes method' )
    max_side_number=20
    #max_side_number=int(input('\n Найбільша кількість сторін 2**(2+'))+1
    print ( '\n   sides      pi_result       difference')
    Archimedes_pi_calculation (max_side_number)


def Chudnovsky_pi_calculation (max_k):
    pi_k=0
    factorial_part=exponent_part=1
    const=640320**1.5 / 12
    sum_part=13591409
    for k in range(max_k+1):
        delta=factorial_part*sum_part/exponent_part 
        pi_k+=delta

        sum_part+=      545140134
        exponent_part*=-262537412640768000
        factorial_part*=24*(6*k+1)*(2*k+1)*(6*k+5)/((k+1)**3)

        pi_result=const/pi_k
        difference= pi_result - math.pi 
        print ( "%3i     %.20f  %.20f" % (k, pi_result, difference))
    return const/pi_k


def Chudnovsky_brothers_method ():
    print('\n\n\n      Chudnovsky brothers method ' )
    print ( '\nk_max         pi_result               difference')
    Chudnovsky_pi_calculation(17)


Leibniz_Gregory_Madhava_method()
Archimedes_method()
Chudnovsky_brothers_method ()






