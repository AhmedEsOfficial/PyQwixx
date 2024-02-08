import random


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
        self.over=False


    def roll_dice(self):
        for i in range(6):
            self.dice_numbers[i] = random.randint(1, 6)

    def new_turn(self):
        #print(self.boards[self.active_player].rows)

        self.active_player = (self.active_player + 1) % self.players

        self.roll_dice()


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
        scoring = []
        add = [r+1 for r in range(12)]
        for x in range(12):
            scoring.append(x + 1 + add[x] )
        return row_score
    def cross_off_box(self, player, move):
        row, index = move
        white_dice = self.dice_numbers[0] + self.dice_numbers[1]
        legal_moves = [(row, white_dice - 2) for row in range(2)]
        legal_moves = legal_moves + [(row, 8 - white_dice)]

        if player != self.active_player:
            if move in legal_moves:
                result = self.boards[player].cross(move)
                return result


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
