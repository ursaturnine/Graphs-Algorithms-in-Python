"""Write a function, islandCount, that takes in a grid containing
Ws and Ls. W represents water and L represents land. The function
should return the number of islands on the grid. An island is a vertically
or horizontally connected region of land.
"""

# 3 islands
grid = [
    ['w', 'l', 'w', 'w', 'w'],
    ['w', 'l', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'l', 'w'],
    ['w', 'w', 'l', 'l', 'w'],
    ['l', 'w', 'w', 'l', 'l'],
    ['l', 'l', 'w', 'w', 'w']
]

def islandCount(grid):
    visited = set()
    count = 0
    for r, geography in enumerate(grid):
        for c, feature in enumerate(geography):
            if explore(grid, r, c, feature, visited ) == True:
                count += 1
    return count


def explore(grid, r, c, feature, visited):

    # if not land
    if feature == 'w':
        return False

    # add to set() as string, so we can check for membership later
    # cannot do above w/ array bc it's not a primitive
    pos = str(r) + ',' + str(c)


    if pos in visited:
        return False
    
    visited.add(pos)

    # up
    explore(grid, r - 1, c, feature, visited)
    # down
    explore(grid, r + 1, c, feature, visited)
    # left
    explore(grid, r, c - 1, feature, visited)
    # right
    explore(grid, r, c + 1, feature, visited)

    # finished with traversal for a new island
    return True


print(islandCount(grid))