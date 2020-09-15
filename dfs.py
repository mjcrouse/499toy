#Depth-First-Search
graph = {1:[2,5], 2:[3,4], 3:[5], 4:[5], 5:[]}
print(graph)

visited = []

def dfs(v):
    visited.append(v)
    print(v)

    for values in graph[v]:
        if values not in visited:
            dfs(values)

dfs(1)