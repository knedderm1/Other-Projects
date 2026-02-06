import pygame
import math


class Checker:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.active = True
        self.king = False

    def defeat(self):
        self.active = False

    def draw(self, surface, x, y):
        pygame.draw.circle(surface, self.get_team(), (x, y), 10)

    def get_loc(self):
        return self.row, self.col

    def get_team(self):
        return self.color

    def is_alive(self):
        return self.active

    def is_king(self):
        return self.king

    # if a piece has moved as far as possible left or right method returns true so piece can become king
    def is_new_king(self):
        row = self.get_loc()[0]
        if self.get_team() == "Black":
            return row == 7

        return row == 0

    # makes sure the new row is in front of, not behind piece
    # makes sure column is one above or below
    def is_valid_move(self, new_r, new_c):
        if self.color == "Black":
            if math.fabs(self.col - new_c) == 1:
                return new_r - 1 == self.row

        if self.color == "Red":
            if math.fabs(self.col - new_c) == 1:
                return new_r + 1 == self.row

    # makes sure the enemy to jump is one row and column away, and in front of piece
    # makes sure enemy isn't on an edge square where it can't be jumped (col 0 or 7 and row 0 or 7)
    def jump(self, enemy):
        e_r, e_c = enemy.get_loc()
        row, col = self.get_loc()
        if self.get_team() == "Red" or self.is_king():
            if e_r + 1 == row and row - 2 >= 0:
                if math.fabs(col - e_c) == 1:
                    if col - e_c == 1:
                        if e_r != 0 and e_c != 0:
                            return True
                        return False

                    if e_r != 0 and e_c != 7:
                        return True

        if self.get_team() == "Black" or self.is_king():
            if e_r - 1 == row and row + 2 <= 7:
                if math.fabs(col - e_c) == 1:
                    if col - e_c == 1:
                        if e_r != 7 and e_c != 0:
                            return True

                    elif e_r != 7 and e_c != 7:
                        return True
        return False

    def move(self, row, col):
        if self.is_valid_move(row, col):
            self.set_loc(row, col)
            return True
        return False

    def set_loc(self, row, col):
        self.row = row
        self.col = col
