# Example file showing a basic pygame "game loop"
import pygame


def get_num_players():
    num_players = 0
    while num_players < 2 or num_players > 6 :
        num_players = int(input("How many players?: "))

    return num_players


def screen_update(screen, players):
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    board1_location = (50, 100)
    board2_location = (50, 470)
    create_board(board1_location, screen)
    create_board(board2_location, screen)

    if players >= 3:
        board3_location = (830, 100)
        create_board(board3_location, screen)

    if players >= 4:
        board4_location = (830, 470)
        create_board(board4_location, screen)

    if players >= 5:
        board5_location = (50, 840)
        create_board(board5_location, screen)

    if players >= 6:
        board5_location = (830, 840)
        create_board(board5_location, screen)

    # flip() the display to put your work on screen
    pygame.display.flip()


def main():
    players = get_num_players()
    pygame.init()
    clock = pygame.time.Clock()
    running = True

    screen = pygame.display.set_mode((810, 850))

    if players == 3 or players == 4:
        screen = pygame.display.set_mode((1610, 850))

    if players == 5 or players == 6:
        screen = pygame.display.set_mode((1610, 1220))

    screen_update(screen, players)


    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                print("mouse clicked at", position)
                pygame.draw.rect(screen, "gray", pygame.Rect(position[0] - 10, position[1] - 10, 50, 50))
                pygame.display.flip()




        clock.tick(60)  # limits FPS to 60

    pygame.quit()

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

    #create background rectangle - 730 by 320 pixels
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

    workingy=y

    for color in colors:
        c += 1
        workingx=x
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
