#Breadth-First-Search

from graph import setupRandomGraph

graph = {1:[2,5], 2:[3,4], 3:[5], 4:[5], 5:[]}
print(graph)

visited = []
queue = []

queue.append(1)

while queue:
    n = queue.pop(0)
    print(n)

    for values in graph[n]:
        if values not in visited:
            queue.append(values)
            visited.append(values)
    
