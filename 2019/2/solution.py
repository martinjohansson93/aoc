import copy

def parseInput():
    with open("input", 'r') as input_file:
        my_list = input_file.readlines()[0].split(',')
        return my_list

def algorithm():
    pass

def one():
    original_data = parseInput()
    original_data = list(map(int, original_data))

    for a in range(0, 100):
        for b in range(0, 100):
            input_list = copy.deepcopy(original_data)
            input_list[1] = a
            input_list[2] = b
            for i in range(0, len(input_list), 4):
                if input_list[i] == 1:
                    input_list[input_list[i+3]] = input_list[input_list[i+1]] + input_list[input_list[i+2]]
                elif input_list[i] == 2:
                    input_list[input_list[i+3]] = input_list[input_list[i+1]] * input_list[input_list[i+2]]
                else:
                    if input_list[0] == 19690720:
                        print(2, a, b)
                    break

def two():
    input_list = parseInput()
    result = 0
    for i in input_list:
        algorithm()

    print(2, result)
if __name__ == "__main__":
    one()
    two()
