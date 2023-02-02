"""Write a function, shortestPath, that takes in an array of edges
for an undirected graph and two nodes, nodeA and nodeB. The function
should return the length of the shortest path between A and B. Consider
the length as the number of edges in the path, not the number of nodes.
If there is no path between A and B, return -1
"""

# convert this into an adjacency list
edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
]


# BFS will give shortest path
def shortestPath(edges, nodeA, nodeB):
    graph = buildGraph(edges)

    # catch cycles
    visited = set([nodeA, ])

    # priority queue, store node and distance from nodeA
    # initialize w nodeA and 0 ('...edges away')
    queue = [[nodeA, 0]]

    while queue:
        [node, distance] = queue.pop(0)

        # found path
        if node == nodeB:
            return distance
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append([neighbor, distance + 1])
    
    return -1



# returns an adjacency list
def buildGraph(edges):

    # keys are nodes, values are neighbors
    graph = {}


    for edge in edges:
        a,b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        
        graph[a].append(b)
        graph[b].append(a)
        

    return graph

print(shortestPath(edges, nodeA, nodeB))
