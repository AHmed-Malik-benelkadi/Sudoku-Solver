class BacktrackingSolver:
    def __init__(self, grid):
        self.grid = grid

    def is_valid(self, pos, num):
        for i in range(9):
            if self.grid[pos[0]][i] == num or self.grid[i][pos[1]] == num:
                return False

        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.grid[i][j] == num:
                    return False

        return True

    def solve(self):
        empty = self.find_empty()
        if not empty:
            return True

        for i in range(1, 10):
            if self.is_valid(empty, i):
                self.grid[empty[0]][empty[1]] = i

                if self.solve():
                    return True

                self.grid[empty[0]][empty[1]] = 0

        return False

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return i, j
        return None
