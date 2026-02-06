import pygame


class Square:
    def __init__(self, row, col, is_bomb):
        self.revealed = False  # whether this square has been clicked or not
        self.adj_revealed = False  # whether a square adjacent to this one has been clicked
        self.neighboring_bombs = 0  # how many adjacent squares are bombs
        self.bomb = is_bomb  # whether this is a bomb or a regular square
        self.row = row
        self.col = col
        self.flagged = False

    def adj_is_revealed(self):
        return self.adj_revealed

    def bomb_count(self):
        return self.neighboring_bombs

    # checks adjacent squares to see if they're bombs - update neighbor-bomb count
    def check_neighbors(self, board):
        if self.is_bomb():
            return

        length = len(board)
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= self.row + i < length and 0 <= self.col + j < length:
                    if board[self.row + i][self.col + j].is_bomb():
                        self.neighboring_bombs += 1

    def draw(self, surface, square_size, offset, is_selected):
        color = (120, 120, 120)
        outline_color = (50, 50, 50)
        selected_color = (255, 195, 0)
        if self.is_revealed():
            color = (180, 180, 180)  # revealed squares have a lighter color
            if self.is_bomb():
                color = (180, 120, 120)
        if is_selected:
            # selected square has a yellow ring around it
            pygame.draw.rect(surface, selected_color,
                             (self.row * square_size + offset, self.col * square_size + offset,
                              square_size-2.5, square_size-2.5))
        else:
            # darker gray outline of each square
            pygame.draw.rect(surface, outline_color,
                             (self.row * square_size + offset, self.col * square_size + offset,
                              square_size-2.5, square_size-2.5))
        pygame.draw.rect(surface, color,
                         (self.row * square_size + offset, self.col * square_size + offset,
                          square_size - 7.5, square_size - 7.5))

        if self.adj_is_revealed() and not self.is_revealed():
            # if a square is adj_revealed, meaning it was revealed but has a bomb neighbor
            # draw number on the square based on bomb neighbors
            bomb_count = self.bomb_count()
            colors = ["Blue", "Green", "Red", "Yellow", "Orange", "Cyan", "Purple", "White"]
            color = colors[bomb_count - 1]
            font = pygame.font.Font('freesansbold.ttf', 25)
            text = font.render(str(bomb_count), True, color)
            rect = text.get_rect()
            rect.center = (self.row * square_size + (square_size // 2) + offset,
                           self.col * square_size + (square_size // 2) + offset)
            surface.blit(text, rect)

        elif self.flagged:
            color = (240, 60, 60)
            font = pygame.font.Font('freesansbold.ttf', 25)
            text = font.render("F", True, color)
            rect = text.get_rect()
            rect.center = (self.row * square_size + offset + (square_size // 2),
                           self.col * square_size + offset + (square_size // 2))
            surface.blit(text, rect)

    def flag(self):
        self.flagged = not self.flagged

    def is_bomb(self):
        return self.bomb

    def is_revealed(self):
        return self.revealed

    # if a square has no neighbors it is revealed without a number and the method is repeated for neighbors
    # which simulates the fill function when you select a square with no neighbor-bombs. self.revealed = true
    # if a square has a bomb neighbor that count of bombs nearby would be printed on the square self.adj_revealed = true
    def reveal(self, board, size):
        if self.is_bomb():
            self.revealed = True
            return False
        if self.is_revealed():
            return True

        if self.bomb_count() == 0:
            self.revealed = True
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= self.row+i < size and 0 <= self.col+j < size:
                        board[self.row + i][self.col + j].reveal(board, size)
        self.adj_revealed = True
        return True
