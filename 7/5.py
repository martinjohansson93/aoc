def most_common(lst):
    return max(set(lst), key=lst.count)

def sol_1(string):
	chars = []
	for i in range(26):
		chars.append(chr(ord('A') + i))
	start_stop = {}
	for char in chars:
		start_stop[char] = []
	for line in input_list:
		first = line.split(" must be finished before step ")[0][-1]
		last = line.split(" must be finished before step ")[1][0]
		start_stop[last].append(first)
	order = []
	while True:
		for char in chars:
			values = start_stop[char]
			for v in values:
				if not v in order:
					print("HJJJEJE")
					not_ready = True
					break
			if not_ready:
				break
			order += char
		if len(order) == len(input_list):
			string = ""
			for i in order:
				string += i
			return string
			
# def sol_2(string):
# 	chars = []
# 	for i in range(26):
# 		chars.append(chr(ord('A') + i))
# 	values = []
# 	for a in chars:
# 		new_string = string.replace(a, "").replace(a.lower(), "")
# 		print(len(new_string))
# 		print(len(string))
# 		values.append(sol_1(new_string))
# 	print(values)
# 	return min(values)

with open("input.txt", 'r') as input_file:
    input_list = [x for x in input_file.readlines()]
res1 = sol_1(input_list)
# res2 = sol_2(input_list[0].strip())

print("Result1: " + str(res1))
# print("Result2: " + str(res2))
