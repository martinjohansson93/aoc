import copy

def parseInput():
    with open("input", 'r') as input_file:
        my_list = input_file.readlines()[0].split(',')
        return my_list

def solution1():
    data = parseInput()
    for i in range(0, len(data), 4):
        if data[i] == 1:
            data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
        elif data[i] == 2:
            data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
        else:
            break
    print(1, data[0])


def solution():
    original_data = parseInput()
    original_data = list(map(int, original_data))
    for a in range(0, 100):
        for b in range(0, 100):
            data = copy.deepcopy(original_data)
            data[1] = a
            data[2] = b
            sol1 = False 
            if a == 12 and b == 2:
                sol1 = True
            for i in range(0, len(data), 4):
                if data[i] == 1:
                    data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
                elif data[i] == 2:
                    data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
                else:
                    if sol1:
                        print(1, data[0])
                        break
                    elif data[0] == 19690720:
                        print(2, a, b)
                        break
    

if __name__ == "__main__":
    solution()
