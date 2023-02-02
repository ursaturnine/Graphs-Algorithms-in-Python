""" Write a function, undirected path, that takes in an array
of edges for an undirected graph and two nodes, nodeA and nodeB.
The function should return a boolean indicating whether or not
there exists a path between nodeA and nodeB
"""

edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]

def undirectedPath(edges, nodeA, nodeB):
    graph = buildGraph(edges)
    print(graph)
    return hasPath(graph, nodeA, nodeB, set())


def hasPath(graph, src, dest, visited):

    # avoid infinite recursion
    if src in visited:
        return False
    
    # add src to visited set
    visited.add(src)

    # found a path
    if src == dest:
        return True
    
    for neighbor in graph[src]:
        return hasPath(graph, neighbor, dest, visited)

    return False

def buildGraph(edges):
    graph = {}

    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        
        # inverse connection for undirected graphs
        graph[a].append(b)
        graph[b].append(a)


    return graph

# print(undirectedPath(edges, 'k', 'n'))