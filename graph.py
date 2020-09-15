import random

def setupRandomGraph():
    graph = {}
    def getNumNodes():
        while True:
            try:
                numNodes = int(input("How many nodes? "))
                while numNodes > 30:
                    print("Too many nodes!")
                    numNodes = getNumNodes()
                while numNodes < 0:
                    print("Negative nodes? What universe do you live in!?")
                    numNodes = getNumNodes()
            except ValueError:
                print("Please enter an integer")
                continue
            else:
                return numNodes
    numNodes = getNumNodes()

    for i in range(1,numNodes+1):
        graph[i] = []
        if i < numNodes - 3:
            for j in range(random.randint(2,5)):
                addme = i + random.randint(1,3)
                if addme not in graph[i]:
                    graph[i].append(addme)
        if i > numNodes - 4 and i < numNodes - 2:
            for j in range(random.randint(0,3)):
                addme = i + random.randint(1,3)
                if addme not in graph[i]:
                    graph[i].append(addme)
    
    return graph



