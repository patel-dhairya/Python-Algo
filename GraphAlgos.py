# Algorithms related to Graph data structure

from DStructures import Graph


def dfs(graph: Graph, start, seen: list):
    seen[start] = True
    to_see = [start]
    while to_see:
        current = to_see.pop()
        for neighbor in graph[current]:
            if not seen[neighbor]:
                seen[neighbor] = True
                to_see.append(neighbor)
