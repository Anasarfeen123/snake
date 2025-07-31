import pygame
class Grid():
    def __init__(self, row_columns =(20,20),screen = pygame.display.set_mode((1980//2, 1980//2))) -> None:
        (self.width, self.height) = pygame.display.get_window_size()
        self.BLOCK = 30
        self.GRIDCOLOR = (255, 255, 255)
        self.rows = row_columns[0]
        self.columns = row_columns[1]
        self.grid_width = self.columns * self.BLOCK
        self.grid_height = self.rows * self.BLOCK
        self.offset_x = (self.width - self.grid_width) // 2
        self.offset_y = (self.height - self.grid_height) // 2
        self.screen = screen
    
    def draw_grid(self):
        for i in range(self.rows + 1):
            y = i * self.BLOCK + self.offset_y
            pygame.draw.line(self.screen, self.GRIDCOLOR, (self.offset_x, y), (self.offset_x + self.grid_width, y))
        for i in range(self.columns + 1):
            x = i * self.BLOCK + self.offset_x
            pygame.draw.line(self.screen, self.GRIDCOLOR, (x, self.offset_y), (x, self.offset_y + self.grid_height))

    def to_pixel(self, grid_x, grid_y):
        x = self.offset_x + grid_x * self.BLOCK
        y = self.offset_y + grid_y * self.BLOCK
        return (x, y)

    def draw_cell(self, grid_x, grid_y, color, br = 0):
        x, y = self.to_pixel(grid_x, grid_y)
        pygame.draw.rect(self.screen, color, (x, y, self.BLOCK, self.BLOCK), border_radius = br)