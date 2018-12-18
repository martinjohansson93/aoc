import collections

def find_most_reccuring(matrix, matrix_size, excluded):
	sum_count_dict = {}
	for row in matrix:
		counts = collections.Counter(row)
		for key, value in counts.items():
			try:
				sum_count_dict[key] = sum_count_dict[key] + value
			except:
				sum_count_dict[key] = value
	print(excluded)
	for v in excluded:
		sum_count_dict.pop(str(int(v)), None)
	print(sum_count_dict)
	return max(sum_count_dict.values())

def closest(matrix_cordinates, x, y):
	closest = None
	closest_distance = float('Inf')
	for index, cord in matrix_cordinates.items():
		diff = abs(cord['x'] - x) + abs(cord['y'] - y)
		if diff == closest_distance:
			closest = '500'
		if diff < closest_distance:
			closest = index
			closest_distance = diff
	return closest

def find_infity_values(matrix, matrix_size):
	# Traverse x=0, x=n, y=0, y=n
	values_found = ['500']
	for i in range(matrix_size):
		values_found.append(matrix[0][i])
		values_found.append(matrix[i][0])
		values_found.append(matrix[matrix_size-1][i])
		values_found.append(matrix[i][matrix_size-1])
	print(set(values_found))
	return set(values_found)

def sol_1(input_list):
	matrix = []
	x_values = []
	y_values = []
	index = 0
	matrix_dict = {}
	for row in input_list:
		x = int(row.split(", ")[0].strip())
		y = int(row.split(", ")[1].strip())
		x_values.append(x)
		y_values.append(y)
		matrix_dict[str(index)] = {'x': x, 'y': y}
		index += 1
	matrix_size = (max(max(x_values), max(y_values))) +1
	for i in range(matrix_size):
		matrix.append([])
		for j in range(matrix_size):
			matrix[i].append(closest(matrix_dict, i, j))
	return find_most_reccuring(matrix, matrix_size, find_infity_values(matrix, matrix_size))

def sol_2(string):
	chars = []
	for i in range(26):
		chars.append(chr(ord('A') + i))
	values = []
	for a in chars:
		new_string = string.replace(a, "").replace(a.lower(), "")
		print(len(new_string))
		print(len(string))
		values.append(sol_1(new_string))
	print(values)
	return min(values)

with open("input.txt", 'r') as input_file:
    input_list = [x for x in input_file.readlines()]
res1 = sol_1(input_list)
# res2 = sol_2(input_list)

print("Result1: " + str(res1))
# print("Result2: " + str(res2))
