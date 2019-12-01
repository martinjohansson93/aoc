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
	for v in excluded:
		sum_count_dict.pop(str(int(v)), None)
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
	return set(values_found)

def calc_sum_distance(matrix_cordinates, matrix_size, x, y):
	sum_dis = 0
	for cord in matrix_cordinates.values():
		sum_dis += abs(cord['x'] - x) + abs(cord['y'] - y)
	return True if sum_dis <= 10000 else False

def parse_input(input_list):
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
	return matrix_dict, matrix_size
	
def sol_1(input_list):
	matrix = []
	matrix_dict, matrix_size = parse_input(input_list)
	for i in range(matrix_size):
		matrix.append([])
		for j in range(matrix_size):
			matrix[i].append(closest(matrix_dict, i, j))
	return find_most_reccuring(matrix, matrix_size, find_infity_values(matrix, matrix_size))

def sol_2(input_list):
	matrix_dict, matrix_size = parse_input(input_list)
	nbr_of_areas = 0
	for i in range(matrix_size):
		for j in range(matrix_size):
			if calc_sum_distance(matrix_dict, matrix_size, i, j):
				nbr_of_areas += 1
	return nbr_of_areas

with open("input.txt", 'r') as input_file:
    input_list = [x for x in input_file.readlines()]
res1 = sol_1(input_list)
res2 = sol_2(input_list)

print("Result1: " + str(res1))
print("Result2: " + str(res2))
