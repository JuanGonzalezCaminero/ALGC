
values = {1:1, 2:5, 3:8, 4:9, 5:10, 6:17, 7:17, 8:20, 9:24, 10:30}

previous_values = []

def rod_cut(rod_length):
	current_max = 0
	previous_values.append(0)
	for length in range(1, rod_length + 1):
		for possible_cut in values:
			if possible_cut <= length:
				current_max = max(current_max, values[possible_cut] + 
											   previous_values[length - possible_cut])
				print(previous_values)
		previous_values.append(current_max)
	print(current_max)
	print(previous_values)

rod_cut(4)