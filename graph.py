graph = {}

def getNumNodes():
    while True:
        try:
            numNodes = int(input("How many nodes? "))
            while numNodes > 26:
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

