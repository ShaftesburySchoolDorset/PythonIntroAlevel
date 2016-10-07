"""
Here is our maze:

  ABCDEFGH
1 *****
2 *   *
3 *S***
4 *   ****
5 * *    *
6 *   *  *
7 ***** E*
8     ****

There is also a picture of the maze in the challenges folder.
"""

# The following code has been written to determine whether not the maze is
# solveable, but it doesn't quite work. Can you fix it?

theMaze = [
    ['*', '*', '*', '*', '*', '', '', ''],
    ['*', '', '', '', '*', '', '', ''],
    ['*', 'S', '*', '*', '*', '', '', ''],
    ['*', '', '', '', '*', '*', '*', '*'],
    ['*', '', '*', '', '', '', '', '*'],
    ['*', '', '', '', '*', '', '', '*'],
    ['*', '*', '*', '*', '*', '', 'E', '*'],
    ['', '', '', '', '*', '*', '*', '*']
]

def isMazeSolveable(maze):
    startX = -1
    startY = -1

    # Look throu grid to find our starting point
    for x in range(8):
        for y in range(8):
            if maze[y][x] == 'S':
                startX = x
                startY = y

    # If we didn't find starting point, maze isn't solveable
    if startX == -1:
        return False

    # If we did find starting point, start exploring from that point
    print('explore at:', y, x)
    return exploreMaze(maze, startX, startY)

def exploreMaze(maze, x, y):

    print('working at', y, x)
    # If the current position is off the grid then we can't keep going this way
    if y > 7 or y < 0 or x > 7 or x < 0:
        return False

    # If the current position is a '*', then we can't continue this way
    if maze[y][x] == '*':
        return False

    # If the current position is an 'E' then we're at the end so the maze
    # is solveable
    if maze[y][x] == 'E':
        print('result at: ', y, x)
        return True

    # Otherwise keep exploring by trying each possible next decision from this
    # point. If any of the options allow us to solve the maze, the return true.
    # We don't have to worry about going off the grid or through a wall - we
    # can just trust our recursive call to handle those posibilities correctly.

    if exploreMaze(maze, x, y-1):
        return True # Search up
    if exploreMaze(maze, x, y+1):
        return True # Search down
    if exploreMaze(maze, x-1, y):
        return True # Search left
    if exploreMaze(maze, x+1, y):
        return True # Search right

    # None of the options worked, so we can't solve the maze using this path.
    return False

print('And the result is: ', isMazeSolveable(theMaze))
