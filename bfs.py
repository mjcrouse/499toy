#Breadth-First-Search

from graph import setupRandomGraph

graph = {1:[2,5], 2:[3,4], 3:[5], 4:[5], 5:[]}
print(graph)


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

print(bfs(1))
assert bfs(1) == [1, 2, 5, 3, 4], "Not equal"

graph = setupRandomGraph()
print(graph)
print(bfs(1))