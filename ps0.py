# 0 --------------------------------------------------------------------------------------

def is_even( x ):

	if x % 2 == 0:
		
		return "Even"
		
	if x % 2 != 0:
		
		return "Odd"
		
# 1 --------------------------------------------------------------------------------------

def digit_number( x ):
		
	return str( len( str( x ) ) )

# 2 --------------------------------------------------------------------------------------

def add_digits( x ):

	baseNumber = 0

	number = str( x )
	
	for digit in number:
	
		
		baseNumber += int( digit )
		
	return str( baseNumber )

# 3 --------------------------------------------------------------------------------------

def sum_less_ints( x ):

	addOnNumber = 1
	
	number = 0
	
	while addOnNumber < x:
	
		number += addOnNumber
		
		addOnNumber += 1
		
	return str( number )

# 4 --------------------------------------------------------------------------------------

def factorial( x ):

	if x == 0:
	
		multiplyNumber = 0
	
	else:
	
		multiplyNumber = 1
	
		baseNumber = 2

		while baseNumber <= x:
	
			multiplyNumber = multiplyNumber * baseNumber
		
			baseNumber += 1
		
	return str( multiplyNumber )
	
# 5 --------------------------------------------------------------------------------------

def is_factor( x, y ):
	
	if x % y == 0:
	
		return "True"
	
	else:
		
		return "False"

# 6 --------------------------------------------------------------------------------------

def is_prime( x ):

	factor = 2
	
	loop = True

	while factor < x and loop == True:
	
		if x % factor == 0:
		
			return "Composite"
			
			loop = False
			
		if x % factor != 0:
		
			factor += 1
			
	if loop == True:
	
		return "Prime"

				

# 7 --------------------------------------------------------------------------------------

def is_perfect( x ):

	number = 1
	
	addNumber = 0

	while number < x:
		
		if x % number == 0:
			
			addNumber += number
			
		number += 1
			
	if x == addNumber:
		
		return "Perfect"
			
	else: 
			
		return "Nonperfect"

# 8 --------------------------------------------------------------------------------------

def is_sum_digits_factor( x ):

	if x % int(add_digits( x )) == 0:

		return "True"

	else:

		return "False"



















































