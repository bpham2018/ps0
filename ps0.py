# 0 --------------------------------------------------------------------------------------

def is_even( x ):

	if x % 2 == 0:
		
		return "True"
		
	if x % 2 != 0:
		
		return "False"
		
# 1 --------------------------------------------------------------------------------------

def digit_number( x ):
		
	return len( str( x ) )

# 2 --------------------------------------------------------------------------------------

def add_digits( x ):

	baseNumber = 0

	number = str( x )
	
	for digit in number:
	
		
		baseNumber += int( digit )
		
	return baseNumber

# 3 --------------------------------------------------------------------------------------

def sum_less_ints( x ):

	addOnNumber = 1
	
	number = 0
	
	while addOnNumber < x:
	
		number += addOnNumber
		
		addOnNumber += 1
		
	return number

# 4 --------------------------------------------------------------------------------------

def factorial( x ):

	addOnNumber = 1

	number = 1

	while addOnNumber <= x:
	
		number = number * addOnNumber
	 
		addOnNumber += 1
	
	return number
	
# 5 --------------------------------------------------------------------------------------

def is_factor( x, y ):
	
	if x % y == 0:
	
		return "True"
	
	else:
		
		return "False"

# 6 --------------------------------------------------------------------------------------

#def is_prime( x ):

#factor = 2

#	if x >= 2:
		
#		for x:
			
#			if x % factor != 0:
			
#				return "prime"
				
#				factor += 1
				

# 7 --------------------------------------------------------------------------------------

def is_perfect( x ):

	number = 1
	
	addNumber = 0

	while number < x:
		
		if x % number == 0:
			
			addNumber += number
			
		number += 1
			
	if x == addNumber:
		
		return "True"
			
	else: 
			
		return "False"

# 8 --------------------------------------------------------------------------------------

def s:

	if x % add_digits( x ) == 0:

		return "true"

	else:

		return "false"



















































