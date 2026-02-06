import pygame
import math
import Checkers


class King(Checkers.Checker):

    # same set up as regular checker, but self.king is set to true
    # this is useful for some methods, since kings can go backwards, but regular checkers can't
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.king = True

    # surface - the pygame window screen to be drawn on
    # x - the x coordinate of the center of the checker to be drawm
    # y - the y coordinate of the center of the checker to be drawn
    def draw(self, surface, x, y):
        # the super method draws a checker at the location x,y with radius 15
        super().draw(surface, x, y)

        # Adds the white "K" on top of the checker
        white = (240, 240, 240)
        king_font = pygame.font.Font('freesansbold.ttf', 12)
        king_text = king_font.render('K', True, white)
        king_rect = king_text.get_rect()
        king_rect.center = (x, y)
        surface.blit(king_text, king_rect)

    # if the row is within one away from new_col and the column is within one move of new_row it is true
    # same as is_valid_move in checker, but doesn't check if for piece going backwards
    def is_valid_move(self, new_r, new_c):
        row, col = self.get_loc()
        if math.fabs(col - new_c) == 1 and math.fabs(row - new_r) == 1:
            return True
        return False
