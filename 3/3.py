def sol_1(input_list):
    matrix = []
    for i in range(1000):
        matrix.append([])
        for j in range(1000):
            matrix[i].append(0)

    for a in input_list:
        i = a.split('@ ')[1].split(': ')  
        x = int(i[0].split(',')[0])
        y = int(i[0].split(',')[1])
        xsize = int(i[1].split('x')[0])
        ysize = int(i[1].split('x')[1])
        for i in range(x, x+xsize):
            for j in range(y, y+ysize):
                matrix[i][j] += 1
    res = 0
    for i in range(1000):
        for j in range(1000):
            if matrix[i][j] > 1:
                res += 1
    return res

with open("input.txt", 'r') as input_file:
    input_list = [x for x in input_file.readlines()]

print(sol_1(input_list))
        