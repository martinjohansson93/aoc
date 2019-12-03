from collections import Counter

def parseInput():
    with open("input", 'r') as input_file:
        lines = input_file.readlines()
        wire1 = lines[0].split(',')
        wire2 = lines[1].split(',')
        return wire1, wire2

def algorithm():
    wire1, wire2 = parseInput()
    result = 0
    path1 = []
    path2 = []

    x = 0
    y = 0
    for wire in wire1:
        dir = wire[:1]
        for i in range(0, int(wire[1:])):
            if dir == 'U':
                y += 1
            elif dir == 'D':
                y -= 1
            elif dir == 'R':
                x += 1
            elif dir == 'L':
                x -= 1
            path1.append((x, y))
    x = 0
    y = 0
    for wire in wire2:
        dir = wire[:1]
        for i in range(0, int(wire[1:])):
            if dir == 'U':
                y += 1
            elif dir == 'D':
                y -= 1
            elif dir == 'R':
                x += 1
            elif dir == 'L':
                x -= 1
            path2.append((x, y))
    res = set(path1).intersection(path2)
    res2 = list(res)
    if res:
        print(1, min([manhattan(i) for i in res]))
    smallest_distance = 1000000000
    for r in res:
        if path2.index(r) + path1.index(r) < smallest_distance:
            smallest_distance = path2.index(r) + path1.index(r)

    print(2, smallest_distance + 2 )

def manhattan(res):
    x = res[0]
    y = res[1]
    if x < 0:
        x = x *-1
    if y < 0:
        y = y *-1
    
    return x + y

if __name__ == "__main__":
    algorithm()
