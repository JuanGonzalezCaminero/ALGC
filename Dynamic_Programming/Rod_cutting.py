import math

values = {1:1, 2:5, 3:8, 4:9, 5:10, 6:17, 7:17, 8:20, 9:24, 10:30}

table = []

def rod_cut(target_length):
	for cut_length in range(0, target_length + 1):
		table.append([])
		for possible_cut in values:
			for row in table:
				for element in row:
					print(str(element).rjust(3), end = " ")
				print()
			print("\n-------------------")
			if possible_cut == 1 and possible_cut > cut_length:
				table[cut_length].append(math.inf)
			elif possible_cut == 1:
				table[cut_length].append(values[possible_cut])
			elif possible_cut > cut_length:
				table[cut_length].append(table[cut_length][possible_cut - 2])
			else:
				table[cut_length][possible_cut] = values[possible_cut]
				print(target_length, cut_length, possible_cut)
				table[cut_length].append(max(table[cut_length][possible_cut - 2],
											values[cut_length] +
											table[target_length - cut_length][possible_cut]))
	for row in table:
		for element in row:
			print(element, end = " ")
		print()

rod_cut(4)
										

