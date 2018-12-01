def sol_1(input_list):
    return sum(input_list)

def sol_2(input_list):
    freq = 0
    all_sums = set()
    while True:
        for i in input_list:
            set_size = len(all_sums)
            freq += i
            all_sums.add(freq)
            if len(all_sums) == set_size:
                return freq

with open("input.txt", 'r') as input_file:
    input_list = [eval(x) for x in input_file.readlines()]

print(sol_1(input_list))
print(sol_2(input_list))
        