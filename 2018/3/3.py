def sol(input_list):
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
    res1 = 0
    for i in range(1000):
        for j in range(1000):
            if matrix[i][j] > 1:
                res1 += 1
    res2 = None
    for a in input_list:
        i = a.split(' @ ')[1].split(': ')  
        x = int(i[0].split(',')[0])
        y = int(i[0].split(',')[1])
        xsize = int(i[1].split('x')[0])
        ysize = int(i[1].split('x')[1])
        overlapping = False
        for j in range(x, x+xsize):
            for k in range(y, y+ysize):
                if not matrix[j][k] == 1:
                    overlapping = True
                    break
            if overlapping:
                break
        if not overlapping:
            res2 = a.split(' @ ')[0][1:]
            print(res2)
            break     
    return res1, res2

    
with open("input.txt", 'r') as input_file:
    input_list = [x for x in input_file.readlines()]

res1, res2 = sol(input_list)
print("Result1: " + str(res1))
print("Result2: " + str(res2))
