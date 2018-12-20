import math

denominations = [1,4,6]

def change(to_change):
	table = []
	for denomination_index in range(len(denominations)):
		for value in range(to_change + 1):
			table.append([])
			#The first row has to be filled-in first, here we can't
			#resource to previous values of the table
			if denomination_index == 0 and denominations[denomination_index] > value:
				#If the smallest denomination is bigger than the value we want
				#to change, we can't solve it
				table[denomination_index].append(0)
			elif denomination_index == 0:
				#If not, we use the coin so we append 1, as we are using one coin, plus
				#the number of coins of this value we used for changing the value that remains
				#after substracting this coin's value from the total, that is, if we are making
				#change of value 2 with a coin of value 1, we will append 1 + the number of coins
				#of value 1 we used to make change of (2 - 1).
				table[denomination_index].append(1 + table[denomination_index][value - 
															denominations[denomination_index]])
			elif denominations[denomination_index] > value:
				#If the value of the current denomination is bigger than the value
				#we want to change, we cannot use it, so we take the value
				#that we got for the previous denomination
				table[denomination_index].append(table[denomination_index - 1][value])
			else:
				#We take the smallest amount of coins between using this denomination, that is, 1 plus
				#the number of coins we used to make change of the remaining value after substracting
				#the value of this coin from the total (we take the number of coins for that value that
				#this denomination got, based on the principle of optimality) or the number of coins
				#we got for the previous denomination
				table[denomination_index].append(min(table[denomination_index - 1][value],
								 1 + table[denomination_index][value - 
															denominations[denomination_index]]))
	for row in table:
		for char in row:
			print(char, end = " ")
		print()

	return(table[len(denominations) - 1][to_change])

print("Result:", change(8))


