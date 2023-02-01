"""
Depth First Search Traversal with a stack
"""


graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

def depthFirstPrint(graph, source):

    # to manipulate the end of the array
    # initialize with starting node
    stack = [source]

    while stack:
        current = stack.pop()
        print(current)
        for neightbor in graph[current]:
            stack.append(neightbor)

def depthFirstPrintRecursive(graph,source):
    print(source)

    for neighbor in graph[source]:
        depthFirstPrintRecursive(graph, neighbor)

        


depthFirstPrintRecursive(graph, 'a')




