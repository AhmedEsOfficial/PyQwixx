import random

rowarray = [0 for x in range(12)]


class board:

    def __init__(self):
        self.rows = [[0 for x in range(12)] for x in range(4)]
        self.locked = [0,0,0,0]
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
        self.moves = 0
        self.row_locked = [False for _ in range(4)]
        self.active_player = first_player
        self.dice_numbers = [random.randint(1, 6) for _ in range(6)]
        self.boards = [board() for _ in range(players)]
        self.over = False
        self.scoring = []
        add = [x + 2 for x in range(12)]
        for x in range(12):
            if x == 0:
                self.scoring.append(1)
            else:
                self.scoring.append(self.scoring[x - 1] + add[x - 1])

    def roll_dice(self):
        for i in range(6):
            self.dice_numbers[i] = random.randint(1, 6)

    def new_turn(self):
        self.active_player = (self.active_player + 1) % self.players
        self.moves = 0

    def get_row_score(self, row):
        row_score = 0
        total_score = 0
        for x in range(12):
            if self.boards[self.active_player].rows[row][x] == 2 or self.boards[self.active_player].rows[row][x] == 3:
                row_score += 1
        if row_score == 0:
            return 0
        return self.scoring[row_score - 1]



    def cross_off_box(self, player, move):
        row, index = move
        white_dice = [self.dice_numbers[0] , self.dice_numbers[1]]
        white_sum = sum(white_dice)
        color_dice = self.dice_numbers[2:]
        legal_moves = [(r, white_sum - 2) for r in range(2)]
        legal_moves = legal_moves + [(2, self.matching_numbers(white_sum - 2))]
        legal_moves = legal_moves + [(3, self.matching_numbers(white_sum - 2))]

        for i in range(self.players):
            for j in range(4):
                if self.boards[i].rows[j][10] == 2:
                    print("LOCK")
                    for n in legal_moves:
                        if n[0] == i:
                            legal_moves.remove(n)

        if player != self.active_player:
            if move in legal_moves:
                result = self.boards[player].cross(move)
                return result

        if player == self.active_player:

            legal_moves = legal_moves + [(0, color_dice[0] + white_dice[0]-2)]
            legal_moves = legal_moves + [(0, color_dice[0] + white_dice[1]-2)]
            legal_moves = legal_moves + [(1, color_dice[1] + white_dice[0] - 2)]
            legal_moves = legal_moves + [(1, color_dice[1] + white_dice[1] - 2)]
            legal_moves = legal_moves + [(2, 10-((color_dice[2] + white_dice[0]) -2))]
            legal_moves = legal_moves + [(2, 10-((color_dice[2] + white_dice[1] -2)))]
            legal_moves = legal_moves + [(3, 10 - ((color_dice[3] + white_dice[0]) - 2))]
            legal_moves = legal_moves + [(3, 10 - ((color_dice[3] + white_dice[1] - 2)))]

            for i in range(self.players):
                for j in range(4):
                    if self.boards[i].rows[j][10] == 2:
                        self.boards[i].locked[j] =1
                        for n in legal_moves:
                            if n[0] == j:
                                legal_moves.remove(n)

            if move in legal_moves:
                result = self.boards[player].cross(move)
                return result


    def matching_numbers(self, index):
        return 10 - index

    def get_active_player(self):
        return self.active_player

