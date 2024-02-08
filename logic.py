import random

rowarray = [0 for x in range(12)]


class board:

    def __init__(self):
        self.rows = [[0 for x in range(12)] for x in range(4)]
        print(self.rows)

    def cross(self, move):
        row, index = move
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


# k = board()
# print(k.cross(0, 4))
# print(k.rows)
# print(k.cross(0, 9))
# print(k.rows)
# print(k.cross(0, 11))
# print(k.rows)
# print(k.cross(0, 4))
# print(k.rows)


class game:

    # Pass the number of players and the first player
    def __init__(self, players, first_player):
        self.current_turn = 0
        self.players = players
        self.penalties = [0 for _ in range(players)]
        self.row_locked = [False for _ in range(4)]
        self.active_player = first_player
        self.dice_numbers = [random.randint(1, 6) for _ in range(6)]
        self.boards = [board() for player in range(players)]

    def roll_dice(self):
        for i in range(6):
            self.dice_numbers[i] = random.randint(1, 6)

    def new_turn(self):
        self.active_player = (self.active_player + 1) % self.players

    def cross_off_box(self, player, move):
        row, index = move
        white_dice = self.dice_numbers[0] + self.dice_numbers[1]
        legal_moves = [(row, white_dice - 2) for row in range(2)]
        legal_moves = legal_moves + [(row, self.matching_numbers(white_dice - 2))]

        if player != self.active_player:
            if move in legal_moves:
                result = self.boards[player].cross(move)
                return result

    def matching_numbers(self, index):
        return 10 - index

    def get_active_player(self):
        return self.active_player

    def get_row_score(self, move):
        row_score = 0
        row, index = move
        for x in range(index):
            if self.rows[row][index] == 2:
                row_score += 1
        if row_score == 2:
            row_score = 3
        if row_score == 3:
            row_score = 6
        if row_score == 4:
            row_score = 10
        if row_score == 5:
            row_score = 15
        if row_score == 6:
            row_score = 21
        if row_score == 7:
            row_score = 28
        if row_score == 8:
            row_score = 36
        if row_score == 9:
            row_score = 45
        if row_score == 10:
            row_score = 55
        if row_score == 11:
            row_score = 66
        if row_score == 12:
            row_score = 78
        return row_score
