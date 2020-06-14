from collections import deque
import argparse
import sys


def main(mat):
    parser = argparse.ArgumentParser(description='Solve a Binary Maze!')
    parser.add_argument('--i', type=int, default=0, help='origin column num?')
    parser.add_argument('--j', type=int, default=0, help='origin row num?')
    parser.add_argument('--x', type=int, default=2, help='dest col num?')
    parser.add_argument('--y', type=int, default=2, help='dest row num?')
    args = parser.parse_args()
    sys.stdout.write(str(BFS(mat, args.i, args.j, args.x, args.y)))


# Below lists details all 4 possible movements from a cell
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
def BFS(mat, i, j, x, y):

    # construct a matrix to keep track of visited cells
    visited = [[False for x in range(N)] for y in range(M)]

    # create an empty queue
    q = deque()
    trace = q

    # mark source cell as visited and enqueue the source node
    visited[i][j] = True

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
            trace.append(i, j, dist)
            break

        # check for all 4 possible movements from current cell
        # and enqueue each valid movement
        for k in range(4):
            # check if it is possible to go to position
            # (i + row[k], j + col[k]) from current position
            if isValid(mat, visited, i + row[k], j + col[k]):
                # mark next cell as visited and enqueue it
                visited[i + row[k]][j + col[k]] = True
                q.append((i + row[k], j + col[k], dist + 1))
# row = [-1, 0, 0, 1]
# col = [0, -1, 1, 0]
    if min_dist != float('inf'):
        op = [[0 for x in range(N)] for y in range(M)]
        print("The shortest path length", min_dist)
        while (q):
            a = q.popleft()
            b = q.popleft()
            q.popleft()
            op[a][b] = 1
    else:
        print("Destination can't be reached from given source")

# Shortest path in a Maze
if __name__ == '__main__':

    mat = [
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
        ]

    # M x N matrix
    M = len(mat)
    N = len(mat[0])

    # Find shortest path from source (0, 0) to destination (7, 5)
    # BFS(mat, 0, 0, 7, 5)
    main(mat)


