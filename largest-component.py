"""Write a function, largestComponent, that takes in an
adjacency list of an undirected graph. The function should
return the size of the largest component in the graph.
"""

# return 4
graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}

def largestComponent(graph):
    visited = set()
    largest = 0


    for node in graph:
        largest = max(largest, exploreSize(graph, node, visited))
    
    return largest

# DFS
def exploreSize(graph, current, visited):

    if current in visited:
        return 0
    
    visited.add(current)

    # represents current node
    size = 1

    for neighbor in graph[current]:
        size += exploreSize(graph, neighbor, visited)
    
    return size


print(largestComponent(graph))



