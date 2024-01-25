# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    x =50
    y =50
    w =50
    h =50


    colors = [pygame.Color(250,219,216,216), pygame.Color(252,243,207,207), pygame.Color(213,245,227,227), pygame.Color(214,234,248,248)]
    font = pygame.font.Font('freesansbold.ttf', 32)
    signs_font = pygame.font.Font('freesansbold.ttf', 22)
    penalty_font = pygame.font.Font('freesansbold.ttf', 20)
    c = 0
    border = pygame.Rect(x-10, y-10, (x+10)*12+10, (y+10)*6+10)
    pygame.draw.rect(screen, "gray", border)
    workingx = x

    penalty = penalty_font.render("penalty", True, "black", None)
    penaltyRect = penalty.get_rect()
    penaltyRect.center = (workingx+60, y * 6)
    screen.blit(penalty, penaltyRect)
    for i in range(4):
        box = pygame.Rect(workingx, y*6+15, 20, 20)
        pygame.draw.rect(screen, "white", box)
        workingx+=30


    workingx+=20
    for i in range(6):
        score = pygame.Rect(workingx, y*6, 75, 40)
        pygame.draw.rect(screen, "white", score)
        workingx+=95
        if i < 2:
            signs = signs_font.render("+", True, "black", None)
        if i == 3:
            signs = signs_font.render("-", True, "black", None)
        if i == 4:
            signs = signs_font.render("=", True, "black", None)
        if i == 5:
            signs = signs_font.render(" ", True, "black", None)
        signsRect = penalty.get_rect()
        signsRect.center = (workingx +23, y*6 +20)
        screen.blit(signs, signsRect)


    for color in colors:
        c+= 1

        for num in range(12):
            board = pygame.Rect(x, y, w, h)
            pygame.draw.rect(screen, color, board)
            x += 60
            if c > 2:
                disp_num = (num-12)*-1

            else:
                disp_num = num+2

            if disp_num == 13 or disp_num ==1:
                numbers = font.render("L", True, "grey", None)
            else:
                numbers = font.render(str(disp_num), True, "grey", None)

            numbersRect = numbers.get_rect()
            numbersRect.center = (x-(w/2)-10, y+(h/2) )
            screen.blit(numbers, numbersRect)
        x = 50
        y += 60

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()