rowarray = [0 for x in range(12)]
class board:

    def __init__(self):
        self.rows=[rowarray for x in range(4)]
        print(self.rows)

k = board()