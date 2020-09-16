#Breadth-First-Search

from graph import setupRandomGraph

def bfs(v):
    visited = []
    queue = []
    result = []

    queue.append(v)
    visited.append(v)

    while queue:
        n = queue.pop(0)
        result.append(n)

        for values in graph[n]:
            if values not in visited:
                queue.append(values)
                visited.append(values)

    return result

graph = {1:[2,5], 2:[3,4], 3:[5], 4:[5], 5:[]}
print(graph)
print(bfs(1))
assert bfs(1) == [1, 2, 5, 3, 4], "Not equal"

graph = {1: [2], 2: [3,5,4], 3: [5,7], 4: [6,7], 5: [8], 6: [], 7: [], 8: []}
print(graph)
print(bfs(1))
assert(bfs(1)) == [1, 2, 3, 5, 4, 7, 8, 6], "Not equal"

graph = setupRandomGraph()
print(graph)
print(bfs(1))