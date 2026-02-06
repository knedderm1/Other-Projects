import pygame
import Board


def game_loop():
    screen_size = (600, 600)
    board_offset = 25
    game = Board.Board()
    selected = game.get_checker(0, 1)

    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    in_game = True
    jump_count = 0

    black = (0, 0, 0)
    font = pygame.font.Font("freesansbold.ttf", 22)

    text = font.render('End Turn', True, black)
    text_rect = text.get_rect()
    text_rect.center = (512.5, 475)

    menu_text = font.render("Play Again", True, black)
    menu_rect = menu_text.get_rect()
    menu_rect.center = (512.5, 475)

    while in_game and not game.is_game_over():

        screen.fill((30, 30, 50))
        game.reset()
        game.draw(screen, board_offset, board_offset, selected)
        pygame.draw.rect(screen, (110, 230, 110), (450, 450, 125, 50))
        screen.blit(text, text_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_game = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                # if the player has a double jump available and presses
                # green button in these coordinates, end turn
                if 450 <= pos[0] <= 575 and 450 <= pos[1] <= 500:
                    if jump_count > 0:
                        selected = game.change_turn(selected)
                        jump_count = 0

                col = (pos[1] - board_offset) // 50
                row = (pos[0] - board_offset) // 50
                # if selected location to move to is occupied
                if game.is_occupied(row, col):
                    # if the occupant is a teammate the teammate becomes the selected
                    if selected.get_team() == game.get_checker(row, col).get_team():
                        selected = game.get_checker(row, col)

                    else:
                        # if enemy then jump the piece
                        if game.jump(selected, game.get_checker(row, col), True):
                            jump_count += 1

                            # if the jump moves the piece into the final row it becomes a king
                            if selected.is_new_king():
                                row, col = selected.get_loc()
                                selected = game.king(row, col, selected.get_team())

                            # if the piece doesn't have any valid double jumps the other team's
                            # piece becomes selected
                            if not game.valid_extra_jump(selected):
                                selected = game.change_turn(selected)
                                jump_count = 0

                else:
                    # (row+col)%2 makes sure the selected square is in the light squares
                    if (row + col) % 2 == 1:
                        # if the current color to move doesn't have any valid jumps they can move freely
                        # if valid jump this prevents moving until the jump is performed
                        if not game.is_valid_jump(selected.get_team()):
                            if game.move(selected, row, col):
                                if selected.is_new_king():
                                    row, col = selected.get_loc()
                                    selected = game.king(row, col, selected.get_team())
                                selected = game.change_turn(selected)

    # when round ends the end turn button is replaced with the play again button
    pygame.draw.rect(screen, (110, 230, 110), (450, 450, 125, 50))
    screen.blit(menu_text, menu_rect)
    pygame.display.update()


game_loop()
in_menu = True

while in_menu:
    # loop for allowing play again to occur
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            in_menu = False

        if action.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if 450 <= mouse_pos[0] <= 575 and 450 <= mouse_pos[1] <= 500:
                game_loop()
