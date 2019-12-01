def sol_1(input_list):
    twoes = 0
    threes = 0
    for i in input_list:
        all_chars = {}
        for c in i:
            try:
                all_chars[c] += 1
            except:
                all_chars[c] = 1

        if 2 in set(all_chars.values()):
            twoes += 1
        if 3 in set(all_chars.values()):
            threes += 1
    return twoes*threes

def sol_2(input_list):
    for row in input_list:
        for a in input_list:
            chars = ""
            for i  in range(len(a)):
                if row[i] == a[i]:
                    chars += a[i]
            if len(row) - len(chars) == 1:
                return chars

with open("input.txt", 'r') as input_file:
    input_list = [x for x in input_file.readlines()]

print(sol_1(input_list))
print(sol_2(input_list))
        