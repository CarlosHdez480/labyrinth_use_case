"""maze solver"""

from collections import deque

class MazeSolver:
    def is_valid_move(matrix, x, y, orientation):
        # Check if the rod can move to the specified position and orientation
        n, m = len(matrix), len(matrix[0])

        if x < 0 or x + 2 >= n or y < 0 or y + 2 >= m:
            return False

        for i in range(x, x + 3):
            for j in range(y, y + 3):
                if matrix[i][j] == 1:
                    return False

        if orientation == "horizontal":
            return matrix[x + 1][y] == 0 and matrix[x + 1][y + 1] == 0 and matrix[x + 1][y + 2] == 0
        elif orientation == "vertical":
            return matrix[x][y + 1] == 0 and matrix[x + 1][y + 1] == 0 and matrix[x + 2][y + 1] == 0
        else:
            raise ValueError("Invalid orientation")

    def get_neighbours(self,
                       matrix,
                       x,
                       y,
                       orientation):
        # Get all valid neighboring positions and orientations
        neighbours = []

        if is_valid_move(matrix, x - 1, y, "horizontal"):
            neighbours.append((x - 1, y, "horizontal"))
        if is_valid_move(matrix, x + 1, y, "horizontal"):
            neighbours.append((x + 1, y, "horizontal"))
        if is_valid_move(matrix, x, y - 1, "vertical"):
            neighbours.append((x, y - 1, "vertical"))
        if is_valid_move(matrix, x, y + 1, "vertical"):
            neighbours.append((x, y + 1, "vertical"))

        if orientation == "horizontal":
            if is_valid_move(matrix, x, y, "vertical"):
                neighbours.append((x, y, "vertical"))
            if is_valid_move(matrix, x + 2, y, "vertical"):
                neighbours.append((x + 2, y, "vertical"))
        elif orientation == "vertical":
            if is_valid_move(matrix, x, y, "horizontal"):
                neighbours.append((x, y, "horizontal"))
            if is_valid_move(matrix, x, y + 2, "horizontal"):
                neighbours.append((x, y + 2, "horizontal"))

        return neighbours

def find_min_moves(matrix):
    def bfs(x, y, orientation):
        visited = set()
        queue = deque([(x, y, orientation)])  # Starting position and orientation
        moves = 0

        while queue:
            for _ in range(len(queue)):
                x, y, orientation = queue.popleft()

                if (x, y, orientation) == (n - 1, m - 1, "horizontal"):
                    return moves

                if (x, y, orientation) not in visited:
                    visited.add((x, y, orientation))
                    neighbours = get_neighbours(matrix, x, y, orientation)
                    queue.extend(neighbours)

            moves += 1

        return -1  # If no path is found

    n, m = len(matrix), len(matrix[0])
    return bfs(0, 0, "horizontal")
