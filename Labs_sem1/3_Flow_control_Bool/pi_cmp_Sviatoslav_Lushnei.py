import math

def Leibniz_Gregory_Madhava_method (log_num_of_iterations):
    print('\n\n\n    Leibniz-Gregory-Madhava method' )
    print ( '\niterations         difference')

    starting_number=1
    sign_coef=4
    current_difference=4-math.pi
    num_of_iterations=9


    for current_log in range(log_num_of_iterations):
        for current_iteration in range (num_of_iterations):
            starting_number+=2
            sign_coef=-sign_coef
            current_difference+= sign_coef/starting_number
        num_of_iterations*=10
        print ( "%9i  %4s  %.10f" % (num_of_iterations/9, f'10^{current_log+1}', current_difference))

def Archimedes_method (division_number):
    print('\n\n\n        Archimedes method' )
    print ( '\n   sides            difference')
    side_length_square=2
    for poligons in range(division_number):
        num_of_sides=4*2**poligons
        pi_difference =num_of_sides * math.sqrt(side_length_square)/2 - math.pi
        print ( "%8i         %.12f" % (num_of_sides, pi_difference))
        side_length_square= side_length_square/4 + (1 - math.sqrt(1-side_length_square/4))**2


def Chudnovsky_brothers_method (max_k):
    print('\n\n\n      Chudnovsky brothers method ' )
    print ( '\nk_max        difference')
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

        pi_difference= const/pi_k - math.pi
        print ( "%3i   %.20f" % (k, pi_difference))
    return const/pi_k


Leibniz_Gregory_Madhava_method(8)
Archimedes_method(20)
Chudnovsky_brothers_method (10)






