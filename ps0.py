# 0 --------------------------------------------------------------------------------------

def is_even( x ): 

	if x % 1 == 0 and x >= 0: # excludes negatives and floats

		if x % 2 == 0: # if number can be divided evenly by 2, return "Even", else return "Odd"
		
			return True	# True for Even
					
		else:
		
			return False # False for True
		
# 1 --------------------------------------------------------------------------------------

def digit_number( x ):
		
	if x % 1 == 0 and x >= 0: # excludes negatives and floats
		
		return len( str( x ) ) # returns amount of digits in number

# 2 --------------------------------------------------------------------------------------

def add_digits( x ):

	if x % 1 == 0 and x >= 0: # excludes negatives and floats

		baseNumber = 0

		number = str( x )
	
		for digit in number: # for each digit in the number, add it to the base
	
			baseNumber += int( digit )
		
		return baseNumber

# 3 --------------------------------------------------------------------------------------

def sum_less_ints( x ):

	if x % 1 == 0 and x >= 0: # excludes negatives and floats

		addOnNumber = 1 # starts at one because don't want to multiply by 0
	
		number = 0
	
		while addOnNumber < x: # only adding numbers less than given
	
			number += addOnNumber
		
			addOnNumber += 1
		
		return number
# 4 --------------------------------------------------------------------------------------

def factorial( x ):

	if x % 1 == 0 and x >= 0: # excludes negatives and floats

		multiplyNumber = 1 
	
		baseNumber = 2

		while baseNumber <= x: # only multiplying numbers up to and including the given"
	
			multiplyNumber = multiplyNumber * baseNumber
		
			baseNumber += 1
		
		return multiplyNumber 
	
# 5 --------------------------------------------------------------------------------------

def is_factor( x, y ):

	if x % 1 == 0 and x > 0 and y % 1 == 0 and y > 0: # excludes non-positive integers and floats
	
		if x % y == 0: # if the remainder of x divided by y is 0, then y is a factor of x
	
			return True
	
		else:
		
			return False

# 6 --------------------------------------------------------------------------------------

def is_prime( x ):

	if x == 2:
	
		return True
		
	if x % 1 == 0 and x > 2 : # excludes numbers below 3 and floats ( 2 taken care of above )

		factor = 2
	
		loop = True

		while factor < x and loop != False: # will terminate once factor is greater than the number
											# ( factor have to be smaller than it's number )
										    # or loop = False
			if x % factor == 0:
		
				return False # False if Composite
			
				loop = False # break the loops if finds one factor
			
			if x % factor != 0:
		
				factor += 1
			
		if loop == True: # if finished loop without breaking it ( loop stays true ), then number is prime
	
			return True # True if Prime

# 7 --------------------------------------------------------------------------------------

def is_perfect( x ):

	if x % 1 == 0 and x > 0: # excludes non-positive integers and floats

		number = 1
	
		baseNumber = 0

		while number < x: # only want numbers below given
		
			if x % number == 0: # to find if number is factor of given
			
				baseNumber += number # if number is factor add it to the base variable ( baseNumber )
			
			number += 1
			
		if x == baseNumber: # if is equal to the sum of its factors, it is perfect
		
			return True # True if Perfect
			
		else: 
			
			return False # False if Not Perfect

# 8 --------------------------------------------------------------------------------------

def is_sum_digits_factor( x ):

	if x % 1 == 0 and x > 0: # excludes non-positive integers and floats

		if x % int(add_digits( x )) == 0: # calls in #2 function and does the operation in neat single-liner
										  # if the remainder of x divided by the sum of it digits is 0,
										  # then the sum of x's digits is a factor of x

			return True

		else:

			return False