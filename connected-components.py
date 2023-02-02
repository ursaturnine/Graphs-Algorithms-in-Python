""" Write a function, connectedComponentsCount, that takes
in an adjacency list of an undirected graph. The function
should return the number of connected components within the
graph.


"""
# should return 2
graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}


# need iterative code to jump from component to component
# need traversal code to traverse individual components
def connectedComponentsCount(graph):
    count = 0
    visited = set()
    
    for node in graph:

        # DFS from node as far as possible
        if explore(graph, node, visited) == True:
            count += 1

    return count



def explore(graph, current, visited):
    if current in visited:
        return False
    
    visited.add(current)

    for neighbor in graph[current]:
        explore(graph, neighbor, visited)
    
    return True

print(connectedComponentsCount(graph))