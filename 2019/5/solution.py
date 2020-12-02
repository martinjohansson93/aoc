import copy

def parseInput():
    with open("input", 'r') as input_file:
        my_list = input_file.readlines()[0].split(',')
        return my_list

def computer(data):
    i = 0
    last_i = None 
    while i < len(data):
        if last_i == i:
            break
        last_i = i
        para1Mode = para2Mode = para3Mode = 0
        temp = data[i][::-1]
        opcode = temp[:2]
        if len(temp) == 3:
            para1 = temp[2]
        elif len(temp) == 4:
            para2 = temp[3]
        elif len(temp) == 5:
            para3 = temp[4]
        if opcode == '01' or opcode == '1' or opcode == '02' or opcode == '2':
            para1 = data[int(data[i+1])] if para1Mode else data[i+1]
            para2 = data[int(data[i+2])] if para2Mode else data[i+2]
            para3 = data[int(data[i+3])] if para3Mode else data[i+3]
            if opcode == '01' or opcode == '1':
                para3 = str(int(para1) + int(para2))
            elif opcode == '02' or opcode == '2':
                para3 = str(int(para1) * int(para2))
            i += 4
            continue
        if opcode == '03' or opcode == '3':
            value = input()
            data[int(data[i+1])] = value
            i += 2
            continue
        if opcode == '04' or opcode == '4':
            print(data[int(data[i+1])])
            i += 2
            continue
        i += 1
    print(data)

def solution():
    original_data = parseInput()
    computer(original_data)

if __name__ == "__main__":
    solution()
