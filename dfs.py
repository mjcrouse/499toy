#Depth-First-Search

from graph import setupRandomGraph
import unittest

graph = setupRandomGraph()
print(graph)

visited = []

def dfs(v):
    visited.append(v)
    print(v, end=" ")

    for values in graph[v]:
        if values not in visited:
            dfs(values)

dfs(1)