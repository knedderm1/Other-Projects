import pygame
import Board


def game_loop():
    screen_size = (600, 600)
    game = Board.Board(10, 25, 50, 20)

    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    in_game = True

    black = (0, 0, 0)
    font = pygame.font.Font("freesansbold.ttf", 14)

    menu_text = font.render("Play Again", True, black)
    menu_rect = menu_text.get_rect()
    menu_rect.center = (512.5, 560)

    while in_game:
        screen.fill((30, 30, 50))
        game.draw(screen)  # draws board
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_game = False

            if event.type == pygame.KEYDOWN:
                # flag a square as a bomb
                if event.key == pygame.K_f:
                    game.flag()
                # click a square to reveal it
                if event.key == pygame.K_SPACE:
                    in_game = game.click()
                    if game.is_win():
                        in_game = False
                # move selected in "string" direction
                if event.key == pygame.K_DOWN:
                    game.move("Down")
                if event.key == pygame.K_UP:
                    game.move("Up")
                if event.key == pygame.K_RIGHT:
                    game.move("Right")
                if event.key == pygame.K_LEFT:
                    game.move("Left")

    # when round ends the end turn button is replaced with the play again button
    game.draw(screen)
    pygame.draw.rect(screen, (110, 230, 110), (450, 535, 125, 50))
    screen.blit(menu_text, menu_rect)
    pygame.display.update()
    return False


game_loop()
in_menu = True

while in_menu:
    # loop for allowing play again to occur
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            in_menu = False

        if action.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if 450 <= mouse_pos[0] <= 575 and 535 <= mouse_pos[1] <= 585:
                game_loop()
