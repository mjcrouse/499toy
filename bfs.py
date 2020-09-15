#Breadth-First-Search

from graph import setupRandomGraph

graph = setupRandomGraph()
print(graph)
print(list(graph.keys()))
visited = len(list(graph.keys())) * [False]
print(visited)
queue = []

queue.append(1)

while queue:
    n = queue.pop(0)
    print(n)

    for i in graph[n]:
        print("i:", i)
        if visited[n] == False:
            queue.append(i)
            visited[n] = True
    
