
def most_common(lst):
    return max(set(lst), key=lst.count)

def sol_1(string):
	chars = []
	for i in range(26):
		chars.append(chr(ord('A') + i))
	
	n = len(string)
	while True:
		for c in chars:
			string = string.replace(c + c.lower(), "")
			string = string.replace(c.lower() + c, "")
		if len(string) == n:
			return len(string)
		n = len(string)

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
res1 = sol_1(input_list[0].strip())
res2 = sol_2(input_list[0].strip())

print("Result1: " + str(res1))
print("Result2: " + str(res2))
