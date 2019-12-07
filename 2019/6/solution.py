def parseInput():
    with open("input", 'r') as input_file:
        return input_file.readlines()

def buildGraph(data):
    graph = {}
    for d in data:
        planets = d.split(')')
        graph[planets[1].strip()] = planets[0].strip()
    return graph

def calculateOrbits(graph):     
    orbits = 0
    for planet, node in graph.items():
        orbits += calculateIndirectOrbits(node, graph)
    return orbits

def calculateIndirectOrbits(node, graph):
    orbits = 1
    if graph.get(node):
        orbits += calculateIndirectOrbits(graph.get(node), graph)
    return orbits

def findDistance(graph):
    santa = graph.get('SAN')
    you = graph.get('YOU')
    santa_parents = []
    you_parents = []
    while santa:
        santa_parents.append(santa)
        santa = graph.get(santa)
    while you:
        you_parents.append(you)
        you = graph.get(you)
    diff = list(set(santa_parents)- set(you_parents))
    diff.extend(list(set(you_parents)- set(santa_parents)))
    return len(diff)
               
def solution():
    data = parseInput()
    graph = buildGraph(data)
    orbits = calculateOrbits(graph)
    distance = findDistance(graph)
    print(1, orbits)
    print(2, distance)

if __name__ == "__main__":
    solution()
