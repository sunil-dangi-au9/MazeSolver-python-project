from collections import deque
import argparse


# Defining a class node to keep track of the shortest path
class Node:
    def __init__(self, x, y):
        self.i = x
        self.j = y
        self.parent = "start"


# Row and Col vector representing the the possible moves
row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]


# Function to check if it is possible to go to position (row, col)
# from current position. The function returns false if row, col:
# is not a valid position or has value 0 or it is already visited
def isValid(mat, visited, row, col):
    return (row >= 0) and (row < M) and (col >= 0) and (col < N) \
            and mat[row][col] == 1 and not visited[row][col]


# Find Shortest Possible Route in a matrix mat from source
# cell (i, j) to destination cell (x, y)
def mazeSolver(mat, i, j, x, y):

    # construct a matrix to keep track of visited cells
    visited = [[False for x in range(N)] for y in range(M)]

    # matrix to keep track of the parent node
    prev = [[False for x in range(N)] for y in range(M)]

    # matrix to generate the solution
    soln = [[0 for x in range(N)] for y in range(M)]

    # create an empty queue
    q = deque()

    # mark source cell as visited and enqueue the source node
    visited[i][j] = True

    # append the starting node as parent
    prev[i][j] = Node(i, j)

    # (i, j, dist) represents matrix cell coordinates and its
    # minimum distance from the source
    q.append((i, j, 0))

    # stores length of longest path from source to destination
    min_dist = float('inf')

    # run till queue is not empty
    while q:

        # pop front node from queue and process it
        (i, j, dist) = q.popleft()

        # (i, j) represents current cell and dist stores its
        # minimum distance from the source

        # if destination is found, update min_dist and stop
        if i == x and j == y:
            min_dist = dist
            break

        # Check for all 4 possible movements from current cell
        # and enqueue each valid movement
        for k in range(4):
            # Check if it is possible to go to position
            # (i + row[k], j + col[k]) from current position
            if isValid(mat, visited, i + row[k], j + col[k]):
                # Mark next cell as visited and enqueue it
                visited[i + row[k]][j + col[k]] = True
                q.append((i + row[k], j + col[k], dist + 1))

                # Append the current visiting node and make the
                # previous node as it's parent
                prev[i + row[k]][j + col[k]] = Node(i + row[k], j + col[k])
                prev[i + row[k]][j + col[k]].parent = prev[i][j]

    # Writing the solution to output file
    # Checking if solution exists
    if min_dist != float('inf'):
        print("The shortest path is ", min_dist, " steps")
        path = prev[x][y]

        # Generating the solution matrix by tracing the parent
        # of each node starting from destination node
        while(path.parent != "start"):
            soln[path.i][path.j] = "1"
            path = path.parent

        # Marking Start and Destination in the solution matrix
        soln[args.j][args.i] = "S"
        soln[x][y] = "D"

        # Writing to output file
        for i in range(M):
            for j in range(N):
                f1.write(str(soln[i][j]) + " ")
            f1.write('\n')
        return

    else:
        print("No path exists!")
        f1.write(str(-1))
        return


# Driver code
if __name__ == '__main__':

    maze = []

    # Taking file, origin and destination values form command line
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', type=str, default='ip1.txt',
                        help="Input file name")
    parser.add_argument('--op', type=str, default='output.txt',
                        help="Output file name")
    parser.add_argument('--i', type=int, default=0, help='origin col num')
    parser.add_argument('--j', type=int, default=0, help='origin row num')
    parser.add_argument('--x', type=int, default=0, help='dest col num')
    parser.add_argument('--y', type=int, default=0, help='dest row num')

    args = parser.parse_args()

    f = open(args.ip, 'r')  # input file
    f1 = open(args.op, 'w')  # output file

    # Generating maze from input file
    for data in f.readlines():
        [line.strip('\n\r') for line in data]
        maze.append([int(x) for x in data.split()])
    f.close()
    M = len(maze)
    N = len(maze[0])

    # If no destination: default = (M,N)
    if ((args.x == 0 and args.y == 0) or (args.x <= 0 and args.y <= 0)
            or ((args.x >= M) or (args.y > N))):
        x = (M - 1)
        y = (N - 1)
    else:
        x = args.y
        y = args.x

    mazeSolver(maze, args.j, args.i, x, y)
