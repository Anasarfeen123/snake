import random
class Food():
    def __init__(self, grid, snake_body):
        while True:
            self.position = (random.randint(0, grid.columns - 1), random.randint(0, grid.rows - 1))
            if self.position not in snake_body:
                break
        self.color = (0, 0, 255)
        self.grid = grid
    def draw(self):
        self.grid.draw_cell(self.position, self.color)