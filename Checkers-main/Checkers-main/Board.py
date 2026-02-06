import Checkers
import pygame
import Kings


class Board:

    # self.grid - database for where all checkers are on the board, None where checkers aren't
    # self.reds - a list of all red checkers
    # self.blacks - a list of all black checkers
    # loops through the grid, making a 8x8. Makes three rows of black and red on either side of the board.
    # Every other position is None to make a checkerboard,
    def __init__(self):
        self.grid = []
        self.reds = []
        self.blacks = []
        for i in range(8):
            self.grid.append([] * 8)

        for i in range(8):
            for j in range(8):
                if (i+j) % 2 == 1:
                    if i <= 2:
                        checker = Checkers.Checker(i, j, "Black")
                        self.grid[i].append(checker)
                        self.blacks.append(checker)

                    elif i >= 5:
                        checker = Checkers.Checker(i, j, "Red")
                        self.grid[i].append(checker)
                        self.reds.append(checker)
                    else:
                        self.grid[i].append(None)
                else:
                    self.grid[i].append(None)

    # determines the team of the previously selected piece and searches the opposing teams database for a living piece
    # the returned piece will become the next selected piece to be moved
    def change_turn(self, selected):
        if selected.get_team() == "Red":
            for black in self.blacks:
                if black.is_alive():
                    return black

        for red in self.reds:
            if red.is_alive():
                return red

    # used to draw the checkerboard pattern by make alternating color squares and drawing a checker on
    # the square if one is within the database at that position
    def draw(self, surface, corner_x, corner_y, selected):
        for i in range(8):
            for j in range(8):
                color = (180, 180, 180)
                if (i + j) % 2 == 0:
                    color = (30, 30, 30)
                pygame.draw.rect(surface, color, (corner_x + i * 50, corner_y + j * 50, 50, 50))

                if self.is_occupied(i, j):
                    x = corner_x + i * 50 + 25
                    y = corner_y + j * 50 + 25

                    if selected is not None:
                        row, col = selected.get_loc()
                        if i == row and j == col:
                            pygame.draw.circle(surface, (255, 195, 0), (x, y), 15)

                    self.grid[i][j].draw(surface, x, y)

    def get_checker(self, row, col):
        return self.grid[row][col]

    # returns true if one of the team's databases has no living pieces
    def is_game_over(self):
        return len(self.reds) == 0 or len(self.blacks) == 0

    # determines if the space row, col on the board is occupied by a checker or not
    def is_occupied(self, row, col):
        if 0 <= row <= 7 and 0 <= col <= 7:
            return self.grid[row][col] is not None

    # color - the color of the team who is making the next move
    # loops through both red and black, using jump to determine if a valid jump is possible
    # when using jump perform_move is set to false so the method can search for a valid move without performing it
    def is_valid_jump(self, color):
        for black in self.blacks:
            for red in self.reds:
                if color == "Black":
                    if black.jump(red):
                        return self.jump(black, red, False)

                if color == "Red":
                    if red.jump(black):
                        return self.jump(red, black, False)

    # jumper - the piece moving over another
    # enemy - the piece getting defeated
    # perform move - if true the move is performed, otherwise we just return true
    # returns whether the landing spot is occupied
    # noinspection PyTypeChecker
    def jump(self, jumper, enemy, perform_move):
        if jumper.jump(enemy):
            e_r, e_c = enemy.get_loc()
            row, col = jumper.get_loc()
            # takes enemy's row, col and jumper's row, col
            r_displacement = -1
            c_displacement = -(col - e_c)
            # depending on if the col is > or < the e_col decides if the jumper has to move +2 or -2 in col
            if jumper.get_team() == "Black":
                r_displacement = 1
            # row is dependent on whether the piece is red / black, since each color can't retreat

            if jumper.is_king():
                r_displacement = -(row - e_r)
            # king's +/- row is dependent on the enemy position like col

            if not self.is_occupied(row + 2 * r_displacement, col + 2 * c_displacement):
                # checks row +/- 2 and col +/- to make sure it's unoccupied before jumping
                # perform move - boolean used to determine whether we perform the move or only return legality of move
                if perform_move:
                    jumper.set_loc(row + 2 * r_displacement, col + 2 * c_displacement)
                    self.grid[row][col] = None
                    self.grid[row + 2 * r_displacement][col + 2 * c_displacement] = jumper
                    enemy.defeat()
                return True
        return False

    # replaces the checker at row, col with a king of the same color
    # replaces the checker at row, col in its color database
    # noinspection PyTypeChecker
    def king(self, row, col, color):
        self.grid[row][col] = Kings.King(row, col, color)

        if color == "Black":
            for i in range(len(self.blacks)):
                b_row, b_col = self.blacks[i].get_loc()
                if b_row == row and b_col == col:
                    self.blacks[i] = self.grid[row][col]
                    break

        if color == "Red":
            for i in range(len(self.reds)):
                r_row, r_col = self.reds[i].get_loc()
                if r_row == row and r_col == col:
                    self.reds[i] = self.grid[row][col]
                    break

        return self.grid[row][col]

    # updates the location of the mover to row,col and resets the previous location
    def move(self, mover, row, col):
        if self.is_occupied(row, col):
            return False
        old_row, old_col = mover.get_loc()

        if mover.move(row, col):
            # noinspection PyTypeChecker
            self.grid[old_row][old_col] = None
            self.grid[row][col] = mover
            return True
        return False

    # goes through the board setting positions to None if the piece is defeated
    # deletes defeated pieces from the color databases
    def reset(self):
        for i in range(8):
            for j in range(8):
                if self.grid[i][j] is not None and not self.grid[i][j].is_alive():
                    self.grid[i][j] = None
        for i in range(len(self.reds)-1, -1, -1):
            if not self.reds[i].is_alive():
                del self.reds[i]

        for i in range(len(self.blacks)-1, -1, -1):
            if not self.blacks[i].is_alive():
                del self.blacks[i]

    # if a piece has already jumped once this method is used to see if it has any legal jumps
    # by comparing it with the other team's database
    # Needs to be separate from other extra_jump method to prevent a different piece from performing
    # a second jump
    def valid_extra_jump(self, checker):
        if checker.get_team() == "Black":
            for red in self.reds:
                if self.jump(checker, red, False) and red.is_alive():
                    return True

        if checker.get_team() == "Red":
            for black in self.blacks:
                if self.jump(checker, black, False) and black.is_alive():
                    return True
