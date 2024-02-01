rowarray = [0 for x in range(12)]


class board:

    def __init__(self):
        self.rows = [[0 for x in range(12)] for x in range(4)]
        print(self.rows)

    def cross(self, row, index):
        if self.rows[row][index] == 1:
            # locked
            return 0
        self.rows[row][index] = 2
        self.lock(row, index)
        return 1

    def lock(self, row, index):
        for j in range(index):
            if self.rows[row][j] == 0 or self.rows[row][j] == 2:
                self.rows[row][j] = self.rows[row][j] + 1


k = board()
print(k.cross(0, 4))
print(k.rows)
print(k.cross(0, 9))
print(k.rows)
print(k.cross(0, 11))
print(k.rows)
print(k.cross(0, 4))
print(k.rows)