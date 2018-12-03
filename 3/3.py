def sol_1(input_list):
    fabric_matrix = []

    for i in range(1000):
        fabric_matrix.append([])
        for j in range(1000):
            fabric_matrix[i].append(0)

    for i in input_list:
        i = i.split("@ ")
        i = i[1].split(': ')
        pos = i[0].split(',')
        size = i[1].split('x')
        print(int(pos[0]))
        print(int(pos[1]))
        print(int(size[0]))
        print(int(size[1]))
        
        for x in range(int(pos[0]) - 1, int(pos[0]) + int(size[0]) -1):
            print(x)
            for y in range(int(pos[1]) - 1, int(pos[1]) + int(size[1]) -1):
                fabric_matrix[x][y] += 1
    res = 0
    for i in range(1000):
        for j in range(1000):
            if fabric_matrix[i][y] > 1:
                res += 1
    return res

with open("input.txt", 'r') as input_file:
    input_list = [x for x in input_file.readlines()]

print(sol_1(input_list))
# print(sol_2(input_list))
        