import pygame
import random

import logic
from logic import game


def get_num_players():
    num_players = 0
    while num_players < 2 or num_players > 6:
        num_players = int(input("How many players?: "))

    return num_players


def initial_build(screen, game):
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    board1_location = (50, 100)
    board2_location = (50, 470)
    create_board(board1_location, screen)
    create_board(board2_location, screen)

    if game.players >= 3:
        board3_location = (830, 100)
        create_board(board3_location, screen)

    if game.players >= 4:
        board4_location = (830, 470)
        create_board(board4_location, screen)

    if game.players >= 5:
        board5_location = (50, 840)
        create_board(board5_location, screen)

    if game.players >= 6:
        board5_location = (830, 840)
        create_board(board5_location, screen)

    display_dice(screen, game.dice_numbers, game.row_locked)
    new_game(screen)
    end_turn_button(screen)
    # flip() the display to put your work on screen
    pygame.display.flip()


def main():
    # game setup
    # players = get_num_players()
    players = 4
    pygame.init()

    clock = pygame.time.Clock()
    running = True
    g = logic.game(players, 0)
    screen = pygame.display.set_mode((1610, 1220))

    # if players == 3 or players == 4:
    #     screen = pygame.display.set_mode((1610, 850))
    #
    # if players == 5 or players == 6:
    #     screen = pygame.display.set_mode((1610, 1220))

    initial_build(screen, g)
    mark_active_player(screen, players, g.get_active_player())

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        q = []
        q = pygame.event.get()
        for event in q:
            if event.type == pygame.QUIT:
                running = False
        take_turn(screen, q, g)

        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     position = pygame.mouse.get_pos()
        #     print("mouse clicked at", position)
        #     if (position[0] > 140 and position[0] < 160) and (position[1] > 10 and position[1] < 30):
        #         roll_dice()
        screen_update(screen, g)
        clock.tick(600)  # limits FPS to 60

    pygame.quit()


def screen_update(screen, game):
    display_dice(screen, game.dice_numbers, game.row_locked)
    pygame.display.flip()


# def find_active_player(players):
#     for i in range(players):
#         if ACTIVE_PLAYER[i] == 1:
#             return i
#     return 0

def mark_active_player(screen, players, active):
    # active = find_active_player(players)
    left_x = 20
    top_y = 90
    if active == 2 or active == 3:
        left_x += 780
    if active == 1 or active == 3:
        top_y += 370
    if active == 4:
        top_y += 740
    small_box = pygame.Rect(left_x, top_y, 20, 320)
    pygame.draw.rect(screen, "green", small_box)


def remove_active_player(screen, players, active):
    # active = find_active_player(players)
    left_x = 20
    top_y = 90
    if active == 2 or active == 3:
        left_x += 780
    if active == 1 or active == 3:
        top_y += 370
    if active == 4:
        top_y += 740
    small_box = pygame.Rect(left_x, top_y, 20, 320)
    pygame.draw.rect(screen, "white", small_box)


# def switch_active_player(players):
#     print(ACTIVE_PLAYER)
#     active = find_active_player(players)
#     if active == players - 1:
#         ACTIVE_PLAYER[0] = 1
#     else:
#         ACTIVE_PLAYER[active+1] = 1
#     ACTIVE_PLAYER[active] = 0
#     print(ACTIVE_PLAYER)

def take_turn(screen, q, game):
    check_penalty(screen, game)
    for event in q:
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            print(position)
            if (position[0] > 140 and position[0] < 160) and (position[1] > 10 and position[1] < 30):
                game.roll_dice()
                # screen_update(screen, game)
            if (position[0] > 635 and position[0] < 765) and (position[1] > 50 and position[1] < 80):
                print("NEW GAME")
                reset_game(screen)
            if (position[0] > 635 and position[0] < 765) and (position[1] > 15 and position[1] < 45):
                print("NEW TURN")
                remove_active_player(screen, game.players, game.get_active_player())
                game.new_turn()
                mark_active_player(screen, game.players, game.get_active_player())
                check_penalty(screen, game)

            check_grid(screen, position, game.players, game)


def mark_box(screen, x, y):
    cross_font = pygame.font.Font('freesansbold.ttf', 36)
    cross = cross_font.render("X", True, "black", None)
    small_box = pygame.Rect(x + 5, y + 5, 30, 30)
    screen.blit(cross, small_box)


def mark_penalty(screen, player, n):
    left_x = 50
    top_y = 370
    if player == 2 or player == 3:
        left_x += 780
    if player == 1 or player == 3:
        top_y += 370
    if player == 4:
        top_y += 740
    cross_font = pygame.font.Font('freesansbold.ttf', 14)
    cross = cross_font.render("X", True, "black", None)
    for i in range(n):
        small_box = pygame.Rect(left_x, top_y, 30, 30)
        screen.blit(cross, small_box)
        left_x+=30


def check_penalty(screen, game):
    index = 0
    for i in game.penalties:
        if i > 0:
            mark_penalty(screen, index, i)
        index+=1


DICE_COLORS = [pygame.Color(0, 0, 0, 0), pygame.Color(0, 0, 0, 0), pygame.Color(255, 51, 51, 255),
               pygame.Color(255, 209, 51, 207), pygame.Color(67, 182, 25, 227), pygame.Color(51, 51, 255, 248)]


def reset_game(screen):
    screen.fill("white")
    pygame.display.flip()
    players = get_num_players()
    g = game(players, 0)
    initial_build(screen, g)


def check_grid(screen, position, players, game):
    left_edge_x = 50
    right_edge_x = 830
    starting_y = 100
    middle_y = 470
    bottom_y = 840

    y = starting_y
    for p in range(players):
        if p == 1 or p == 3:
            y = middle_y
        if p == 4 or p == 5:
            y = bottom_y
        if p == 2:
            y = starting_y
        for j in range(4):
            if p == 0 or p == 1 or p == 4:
                x = left_edge_x
            else:
                x = right_edge_x
            for i in range(11):
                if position[0] in range(x, x + 50) and position[1] in range(y, y + 50):
                    mark_box(screen, x, y)
                    game.boards[p].cross((j, i))
                x += 60
            y += 60


def end_turn_button(screen):
    end_turn_font = pygame.font.Font('freesansbold.ttf', 24)
    end_turn = end_turn_font.render("End Turn", True, "black", None)
    end_turn_box = pygame.Rect(635, 15, 130, 30)
    pygame.draw.rect(screen, "gray", end_turn_box)
    end_turn_rect = end_turn.get_rect()
    end_turn_rect.center = (700, 30)
    screen.blit(end_turn, end_turn_rect)


def new_game(screen):
    new_game_font = pygame.font.Font('freesansbold.ttf', 24)
    new_game = new_game_font.render("New Game", True, "black", None)
    new_game_box = pygame.Rect(635, 50, 130, 30)
    pygame.draw.rect(screen, "gray", new_game_box)
    new_game_rect = new_game.get_rect()
    new_game_rect.center = (700, 65)
    screen.blit(new_game, new_game_rect)


def display_dice(screen, num, locked):
    dice_x = 20
    dice_y = 20
    # wipe_dice(screen)
    dice_back = pygame.Rect(0, 0, 140, 30)
    pygame.draw.rect(screen, "white", dice_back)

    for i in range(6):
        dice_font = pygame.font.Font('freesansbold.ttf', 32)
        dice = dice_font.render(str(num[i]), True, DICE_COLORS[i], None)
        dice_rect = dice.get_rect()
        dice_rect.center = (dice_x, dice_y)
        screen.blit(dice, dice_rect)
        if (i > 1):
            if (locked[i - 2] == True):
                dice_font = pygame.font.Font('freesansbold.ttf', 32)
                dice = dice_font.render("L", True, DICE_COLORS[i], None)
                dice_rect = dice.get_rect()
                dice_rect.center = (dice_x, dice_y)
                screen.blit(dice, dice_rect)
            else:
                dice_font = pygame.font.Font('freesansbold.ttf', 32)
                dice = dice_font.render(str(num[i]), True, DICE_COLORS[i], None)
                dice_rect = dice.get_rect()
                dice_rect.center = (dice_x, dice_y)
                screen.blit(dice, dice_rect)
        dice_x += 20

    dice_box = pygame.Rect(dice_x, dice_y - 10, 20, 20)
    pygame.draw.rect(screen, "gray", dice_box)


def create_board(location, screen):
    x, y = location
    w = 50
    h = 50

    colors = [pygame.Color(250, 219, 216, 216), pygame.Color(252, 243, 207, 207), pygame.Color(213, 245, 227, 227),
              pygame.Color(214, 234, 248, 248)]
    font = pygame.font.Font('freesansbold.ttf', 32)
    signs_font = pygame.font.Font('freesansbold.ttf', 22)
    penalty_font = pygame.font.Font('freesansbold.ttf', 20)
    c = 0

    # create background rectangle - 730 by 320 pixels
    border = pygame.Rect(x - 10, y - 10, 730, 320)
    pygame.draw.rect(screen, "gray", border)
    workingx = x

    penalty = penalty_font.render("penalty", True, "black", None)
    penaltyRect = penalty.get_rect()
    penaltyRect.center = (workingx + 60, y + 250)
    screen.blit(penalty, penaltyRect)
    for i in range(4):
        box = pygame.Rect(workingx, y + 265, 20, 20)
        pygame.draw.rect(screen, "white", box)
        workingx += 30

    workingx += 20
    for i in range(6):
        score = pygame.Rect(workingx, y + 250, 75, 40)
        pygame.draw.rect(screen, "white", score)
        workingx += 95
        if i < 2:
            signs = signs_font.render("+", True, "black", None)
        if i == 3:
            signs = signs_font.render("-", True, "black", None)
        if i == 4:
            signs = signs_font.render("=", True, "black", None)
        if i == 5:
            signs = signs_font.render(" ", True, "black", None)
        signsRect = penalty.get_rect()
        signsRect.center = (workingx + 23, y + 250 + 20)
        screen.blit(signs, signsRect)

    workingy = y

    for color in colors:
        c += 1
        workingx = x
        for num in range(12):

            board = pygame.Rect(workingx, workingy, w, h)
            pygame.draw.rect(screen, color, board)
            workingx += 60
            if c > 2:
                disp_num = (num - 12) * -1

            else:
                disp_num = num + 2

            if disp_num == 13 or disp_num == 1:
                numbers = font.render("L", True, "grey", None)
            else:
                numbers = font.render(str(disp_num), True, "grey", None)

            numbersRect = numbers.get_rect()
            numbersRect.center = (workingx - (w / 2) - 10, workingy + (h / 2))
            screen.blit(numbers, numbersRect)

        workingy += 60


if __name__ == "__main__":
    main()
