def parseInput():
    with open("input", 'r') as input_file:
        return input_file.readlines()

def one():
    input_list = parseInput()    
    total_fuel = 0
    for num in input_list:
        total_fuel += fuelRequired(num)

    print(1, total_fuel)

def two():
    input_list = parseInput()    
    total_fuel = 0
    for fuel in input_list:
        while True:    
            fuel = fuelRequired(fuel)
            if fuel <= 0:
                break
            total_fuel += fuel

    print(2, total_fuel)

def fuelRequired(i):
    return int((int(i)/3)) - 2

if __name__ == "__main__":
    one()
    two()
