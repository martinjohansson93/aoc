def most_common(lst):
    return max(set(lst), key=lst.count)

def sol(input_list):
	current_guard = None
	guard_dict = {}
	current_guard_sleeping = False
	for row in input_list:
		row_parts = row.split('] ')
		time = row_parts[0][-5:]
		minutes = time[-2:]
		if 'Guard' in row_parts[1]:
			current_guard = row_parts[1].split('#')[1].split(' ')[0]
		if 'falls' in row_parts[1] and not current_guard_sleeping:
			minutes_started_sleeping = minutes
			current_guard_sleeping = True
		if 'wakes' in row_parts[1] and current_guard_sleeping:
			if not current_guard in guard_dict:
				guard_dict[current_guard] = []
			for i in range(int(minutes_started_sleeping), int(minutes) +1):
				guard_dict[current_guard].append(i)
			current_guard_sleeping = False
	most_common_sleeping_id = 0
	most_common_sleeping_minutes = 0
	most_times_sleeping_on_minute_amount = 0
	most_times_sleeping_on_minute_id = 0

	for key, value in guard_dict.items():
		if len(value) > most_common_sleeping_minutes:
			most_common_sleeping_minutes = len(value)
			most_common_sleeping_id = key
		times_occur_most = 0
		for m in set(value):
			times_occur = value.count(m)
			if times_occur > times_occur_most:
				times_occur_most = times_occur
				times_occur_most_minute = m
		if times_occur_most > most_times_sleeping_on_minute_amount:
			most_times_sleeping_on_minute_amount = times_occur_most
			most_times_sleeping_on_minute_minute = times_occur_most_minute
			most_times_sleeping_on_minute_id = key
		
	return int(most_common_sleeping_id) * int(most_common(guard_dict[most_common_sleeping_id])), int(most_times_sleeping_on_minute_id) * int(most_times_sleeping_on_minute_minute)

with open("input.txt", 'r') as input_file:
    input_list = [x for x in input_file.readlines()]

res1, res2 = sol(sorted(input_list))
print("Result1: " + str(res1))
print("Result2: " + str(res2))
