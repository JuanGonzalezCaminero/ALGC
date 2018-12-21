import random

function = "2 * x ** 2 + x + 1"

def definite_integral(function, a, b, number_of_evaluations):
	#Evaluate the function in a series of random points 
	#between a and b 
	total = 0
	for i in range(number_of_evaluations):
		x = random.uniform(a, b)
		total += eval(function)
	average = total/number_of_evaluations

	return((b - a) * average)

print(definite_integral(function, 0, 1, 10000))