import math

values = [1, 4, 6]

previous_values = []

def rod_cut(to_change):
	current_min = math.inf
	previous_values.append(current_min)
	for amount in range(1, to_change + 1):
		for value in values:
			if value == 1:
				current_min = amount
				previous_values.append(amount)
			elif value <= amount:
				current_min = min(current_min, 1 + previous_values[amount - value])
				print(previous_values)

		previous_values.append(current_min)
	print(current_min)
	print(previous_values)

rod_cut(8)