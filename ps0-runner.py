import ps0

# 0 test ---------------------------------------------------------------------------------

print( "\nEven or odd test with odd number ( 9 )" )

print( ps0.is_even( 9 ) + "\n" )

print( "Even or odd test with even number ( 28 )" )

print( ps0.is_even( 28 ) + "\n" )

# 1 test ---------------------------------------------------------------------------------

print( "Number of digits test with 1 digit number ( 1 )" )

print( ps0.digit_number( 1 ) + "\n" )

print( "Number of digits test with 2 digit number ( 22 )" )

print( ps0.digit_number( 22 ) + "\n" )

print( "Number of digits test with 3 digit number ( 333 )" )

print( ps0.digit_number( 333 ) + "\n" )

# 2 test ---------------------------------------------------------------------------------

print( "Sum of digits test with single digit number ( 5 )" )

print( ps0.add_digits( 5 ) + "\n" )

print( "Sum of digits test with double digit number ( 87 )" )

print( ps0.add_digits( 87 ) + "\n" )

print( "Sum of digits test with triple digit number ( 999 )" )

print( ps0.add_digits( 999 ) + "\n" )

# 3 test ---------------------------------------------------------------------------------

print( "Sum of less than test with single digit number ( 7 )" )

print( ps0.sum_less_ints( 7 ) + "\n" )

print( "Sum of less than test with double digit number ( 14 )" )

print( ps0.sum_less_ints( 14 ) + "\n" )

# 4 test ---------------------------------------------------------------------------------

print( "Factorial test with number 1" )

print( ps0.factorial( 1 ) + "\n" )

print( "Factorial test with number 0" )

print( ps0.factorial( 0 ) + "\n" )

print( "Factorial test with double digit number ( 11 )" )

print( ps0.factorial( 11 ) + "\n" )

# 5 test ---------------------------------------------------------------------------------

print( "Is 3 a factor of 9?" )

print( ps0.is_factor( 9, 3 ) + "\n" )

print( "Is 3 a factor of 10?" )

print( ps0.is_factor( 10, 3 ) + "\n" )

# 6 test ---------------------------------------------------------------------------------

print( "Prime test with prime single digit prime number ( 2 )" )

print( ps0.is_prime( 2 ) + "\n" )

print( "Prime test with prime single digit prime number ( 5 )" )

print( ps0.is_prime( 5 ) + "\n" )

print( "Prime test with composite double digit number ( 30 )" )

print( ps0.is_prime( 30 ) + "\n" )

print( "Prime test with prime triple digit number ( 317 )" )

print( ps0.is_prime( 317 ) + "\n" )

# 7 test ---------------------------------------------------------------------------------

print( "Perfect test with perfect single digit number ( 6 )" )

print( ps0.is_perfect( 6 ) + "\n" )

print( "Perfect test with perfect double digit number ( 28 )" )

print( ps0.is_perfect( 28 ) + "\n" )

print( "Perfect test with nonperfect double digit number ( 45 )" )

print( ps0.is_perfect( 45 ) + "\n" )

# 8 test ---------------------------------------------------------------------------------

print( "Is sum of digits a factor test with number '1'" )

print( ps0.is_sum_digits_factor( 1 ) + "\n" )

print( "Is sum of digits a factor test with number '12'" )

print( ps0.is_sum_digits_factor( 12 ) + "\n" )

print( "Is sum of digits a factor test with number '205'" )

print( ps0.is_sum_digits_factor( 205 ) + "\n" )