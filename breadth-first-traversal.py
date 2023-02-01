"""
Breadth First Search Traversal with a queue
"""

# adjacency list
graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

# always iterative
def breadthFirstPrint(graph, source):
    # initialize queue with source node
    # pop() first index or pop() last
    queue = [source]

    while queue:
        current = queue.pop(0)
        print(current)
        for neighbor in graph[current]:
            queue.append(neighbor)


breadthFirstPrint(graph, 'a')


