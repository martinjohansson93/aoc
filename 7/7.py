def sol_1(input_list):
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
			if char in order:
				continue
			values = start_stop[char]
			if len(values) == 0:
				order.append(char)
				break
			not_ready = False
			for v in values:
				if v not in order:
					not_ready =True 
					break
			if not_ready:
				continue
			order.append(char)
			break
		if len(order) == 26:
			string = ""
			for i in order:
				string += i
			return string

def increment_all(running_steps):
	for key, step in running_steps.items():
		running_steps[key] += 1
	return running_steps
			
def sol_2(input_list):
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
	free_workers = 6
	ascii_A = ord('A')
	running_steps = {}
	seconds = 0
	while True:
		increment_all(running_steps)
		for key, value in running_steps.items():
			if value >= 60 + ord(key) - ascii_A + 1:
				order.append(key)
				del running_steps[key]
				free_workers += 1
		if not free_workers:
			continue
		for char in chars:
			if char in order or char in running_steps.keys():
				continue
			values = start_stop[char]
			if len(values) == 0:
				running_steps[char] = 0
				free_workers += -1
				if not free_workers:
					break
				else:
					continue
			not_ready = False
			for v in values:
				if v not in order:
					not_ready = True 
					break
			if not_ready:
				continue
			running_steps[char] = 0
			free_workers += -1
			if free_workers:
				continue
			break
		if len(order) == 26:
			string = ""
			for i in order:
				string += i
			return seconds
		seconds += 1

with open("input.txt", 'r') as input_file:
    input_list = [x for x in input_file.readlines()]
res1 = sol_1(input_list)
res2 = sol_2(input_list)

print("Result1: " + str(res1))
print("Result2: " + str(res2))
