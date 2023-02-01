"""
Write a function, hasPath, that takes in an object representing the adjacency list
of a directed, acylic graph and two nodes, src and dst. The function should return
a boolean indicating whether or not there exists a directed path between the source
and destination nodes.


Plain English:
Consider a source and a destination.

Is there a path that exists between two nodes?

Can use DFS or BFS


acyclic = no cycles, or, no paths between
nodes where you could end up where you first
started
"""


# each key is a node
# directed graph
graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

def hasPath(graph, src, dest):
    if src == dest:
        return True
    
    for neighbor in graph[src]:
        # update current to neightbor; keep destination the same
        if hasPath(graph, neighbor, dest):
            return True
    return False

def hasPathBFS(graph, src, dest):
    # initialize queue w src node
    queue = [src]

    while queue:
        current = queue.pop(0)
        if current == dest:
            return True
        for neighbor in graph[current]:
            queue.append(neighbor)
    return False

print(hasPathBFS(graph, 'k', 'i'))
# print(hasPath(graph, 'f', 'k'))

    

