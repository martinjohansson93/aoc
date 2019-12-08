def parseInput():
    with open("input", 'r') as input_file:
        return [int(char) for char in input_file.readlines()[0]]

def createLayers(data):
    layers = []
    for i in range(0, len(data), 25*6):
        layers.append(data[i:i+25*6])
    return layers

def findLayerWithLeastZeroes(layers):
    least_zeroes = 1000000
    best_layer = None
    for i in range(0, len(layers)):
        count = layers[i].count(0)
        if count < least_zeroes:
            least_zeroes = count
            best_layer = i
    return best_layer

def getFinalImage(layers):
    image = ''
    for i in range(0, 25*6):
        for j in range(0, len(layers)):
            if layers[j][i] == 2:
                if j == len(layers)-1:
                    image += str(layers[j][i])
                    break
                continue
            image += str(layers[j][i])
            break
    return image

def getSolution1Value(best_layer):
    one_count = best_layer.count(1)
    two_count = best_layer.count(2)
    return one_count * two_count

def printFinalImage(final_image):
    for i in range(0, 25*6, 25):
        row = ''
        for pixel in final_image[i:i+25]:
            if pixel == '1':
                row += ':'
            else:
                row += ' '
        print(row)

def solution():
    data = parseInput()
    layers = createLayers(data)
    best_layer = findLayerWithLeastZeroes(layers)
    final_image = getFinalImage(layers)
    print(1, getSolution1Value(layers[best_layer]))
    print(2)
    printFinalImage(final_image)

if __name__ == "__main__":
    solution()
