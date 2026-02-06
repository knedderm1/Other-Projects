import pygame
import random
import Bomb


class Board:
    def __init__(self, size, offset, square_size, bomb_count):
        self.grid = []  # grid of all the mines - added in one by one
        self.offset = offset  # used for drawing the board away from corner
        self.square_size = square_size  # size of each square on the board
        self.selected = (0, 0)  # the coordinates of the selected square
        self.size = size  # the rows/column count on the board
        for i in range(size):
            self.grid.append([])
            for j in range(size):
                self.grid[i].append(Bomb.Square(i, j, False))
        # randomly replaces the slots with bombs if they aren't already bombs
        for i in range(bomb_count):
            row, col = random.randrange(0, size), random.randrange(0, size)
            if not self.grid[row][col].is_bomb():
                self.grid[row][col] = Bomb.Square(row, col, True)
        # checks to see each square's number for when it is revealed
        for i in range(size):
            for j in range(size):
                self.grid[i][j].check_neighbors(self.grid)

    # performs reveal on the selected coordinate in grid
    def click(self):
        return self.grid[self.selected[0]][self.selected[1]].reveal(self.grid, self.size)

    # draws the board squares one by one and gets the square's info to determine if it is revealed
    # if revealed draws the number of adjacent or colored red if bomb
    def draw(self, surface):
        board_background = (218, 220, 146)
        board_size = self.size * self.square_size
        pygame.draw.rect(surface, board_background, (self.offset, self.offset, board_size, board_size))
        for row in range(self.size):
            for col in range(self.size):
                is_selected = (row, col) == self.selected
                self.grid[row][col].draw(surface, self.square_size, self.offset, is_selected)

    # places an "F" icon over the unrevealed square
    def flag(self):
        self.grid[self.selected[0]][self.selected[1]].flag()

    # return true if there is no more unrevealed non-bomb squares
    def is_win(self):
        count = 0
        bombs = 0
        for row in self.grid:
            for square in row:
                if not square.is_bomb():
                    if square.is_revealed() or square.adj_is_revealed():
                        count += 1
                else:
                    bombs += 1
        return (self.size*self.size - count) == bombs

    # moves selected square through the grid depending on direction given
    def move(self, direction):
        row = self.selected[0]
        col = self.selected[1]
        if direction == "Down":
            col = (col + 1) % self.size

        elif direction == "Up":
            col = (self.size + col - 1) % self.size

        elif direction == "Right":
            row = (row + 1) % self.size

        elif direction == "Left":
            row = (self.size + row - 1) % self.size

        self.selected = (row, col)
