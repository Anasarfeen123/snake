import pygame
class Snake():
    def __init__(self, grid, paused = False) -> None:
        self.grid = grid
        self.head = (4, 1)
        self.body = [self.head, (3, 1), (2, 1)]
        self.direc = (1,0)
        self.color = (0, 255, 100)
        self.velocity = 1
        self.last_move_time = pygame.time.get_ticks()
        self.paused = paused
    def draw(self):
        for segment in self.body:
            self.grid.draw_cell(segment[0], segment[1], self.color, 8)

    def move(self, grow = False):
        dx, dy = self.direc
        if pygame.time.get_ticks() - self.last_move_time >= 200:
            new_head = (self.head[0] + dx, self.head[1] + dy)
            self.head = new_head
            if not grow:
                self.body = [new_head] + self.body[:-1]
            self.last_move_time = pygame.time.get_ticks()
        if grow:
            new_head = (self.head[0] + dx, self.head[1] + dy)
            self.head = new_head
            self.body = [new_head] + self.body
            self.last_move_time = pygame.time.get_ticks()

    def grow(self):
        self.move(grow=True)
            
    def chng_dir(self, dircn):
        if dircn == "W" and self.direc != (0, -1):
            self.direc = (0, -1)
        elif dircn == "S" and self.direc != (0, 1):
            self.direc = (0, 1)
        elif dircn == "A" and self.direc != (1, 0):
            self.direc = (-1, 0)
        elif dircn == "D" and self.direc != (-1, 0):
            self.direc = (1, 0)

    def kill(self, grid):
        if self.head in self.body[1:] or not (0 <= self.head[0] < grid.columns and 0 <= self.head[1] < grid.rows):
            self.color = (255, 0, 0)
            self.paused = True