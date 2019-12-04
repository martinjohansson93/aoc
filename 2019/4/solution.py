def parseInput():
    with open("input", 'r') as input_file:
        return "172851-675869"

def algorithm():
    pass

def isTriple(value, i):
    if i > 1:
        if value[i-1] == value[i] and value[i-2] == value[i]:
            return True
    if i > 0 and i < len(value)-1:
        if value[i-1] == value[i] and value[i+1] == value[i]:
            return True
    if i < len(value)-2:
        if value[i+1] == value[i] and value[i+2] == value[i]:
            return True
    return False

def isDouble(value, secondSolution=False):
    for i in range(1, len(value)):
        if i > 0:
            if value[i-1] == value[i]:
                if isTriple(value, i) and secondSolution:
                    continue
                return True
    return False

def isIncreasing(value):
    prev = 0
    for i in range(0, len(value)):
        if prev > value[i]:
            return False
        prev = value[i]
    return True

def solution():
    res1 = []
    res2 = []
    for i in range(172851, 675870):
        success = isIncreasing(str(i))
        if not success:
            continue
        success = isDouble(str(i))
        if not success:
            continue
        res1.append(i)
        success = isDouble(str(i), secondSolution=True)
        if not success:
            continue
        res2.append(i)
    print(1, len(res1))
    print(2, len(res2))
    
if __name__ == "__main__":
    solution()
