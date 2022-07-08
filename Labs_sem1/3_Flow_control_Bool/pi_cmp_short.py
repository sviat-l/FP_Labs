import math
     
def Leibniz_Gregory_Madhava_method(log_num_of_iterations):
    print('\n\n\n    Leibniz-Gregory-Madhava method' )
    print ( '\niterations    pi_result     difference')
    starting_number=1
    current_pi=sign_coef=4
    num_of_iterations=9
    for repeat_number in range(log_num_of_iterations):
        for repeat_number in range (num_of_iterations):
            starting_number+=2
            sign_coef=-sign_coef
            current_pi+= sign_coef/starting_number 
        num_of_iterations*=10
        print ( "%9i   %.10f  %.10f" % (num_of_iterations/9, current_pi, current_pi - math.pi))
        
    

def Archimedes_method ():
    print('\n\n\n           Archimedes method' )
    print ( '\n   sides      pi_result     difference')
    side_length_square=2  
    for poligons in range(20):
        num_of_sides=4*2**poligons
        pi_result =num_of_sides * math.sqrt(side_length_square)/2
        print ( "%8i   %.12f  %.12f" % (num_of_sides, pi_result, pi_result-math.pi))
        side_length_square= side_length_square/4 + (1 - math.sqrt(1-side_length_square/4))**2


def Chudnovsky_brothers_method ():
    print('\n\n\n      Chudnovsky brothers method ' )
    print ( '\nk_max         pi_result               difference')
    max_k=10
    pi_k=0
    factorial_part=exponent_part=1
    const=640320**1.5 / 12
    sum_part=13591409
    for k in range(max_k+1):
        delta=factorial_part*sum_part/exponent_part 
        pi_k+=delta

        sum_part+=545140134
        exponent_part*=-262537412640768000
        factorial_part*=24*(6*k+1)*(2*k+1)*(6*k+5)/((k+1)**3)

        pi_result=const/pi_k
        print ( "%3i     %.20f  %.20f" % (k, pi_result, pi_result - math.pi ))


Leibniz_Gregory_Madhava_method(8)
#Archimedes_method()
#Chudnovsky_brothers_method ()

