import pygame
class Grid():
    def __init__(self, row_columns =(20,20),screen=None, block_size=30) -> None: 
        (self.width, self.height) = pygame.display.get_window_size()
        self.BLOCK = block_size
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
            pygame.draw.line(self.screen, self.GRIDCOLOR, (self.offset_x, y), (self.offset_x + self.grid_width, y)) #type: ignore
        for i in range(self.columns + 1):
            x = i * self.BLOCK + self.offset_x
            pygame.draw.line(self.screen, self.GRIDCOLOR, (x, self.offset_y), (x, self.offset_y + self.grid_height)) #type: ignore

    def to_pixel(self, grid_x, grid_y):
        x = self.offset_x + grid_x * self.BLOCK
        y = self.offset_y + grid_y * self.BLOCK
        return (x, y)

    def draw_cell(self, grid_x, grid_y, color, br = 0):
        x, y = self.to_pixel(grid_x, grid_y)
        pygame.draw.rect(self.screen, color, (x, y, self.BLOCK, self.BLOCK), border_radius = br) #type: ignore
    
    def get_neighbor_pos(self, pos:tuple):
        neighbors = []
        
        # Check right neighbor
        if pos[0] < self.columns - 1:
            neighbors.append((pos[0] + 1, pos[1]))
        
        # Check left neighbor
        if pos[0] > 0:
            neighbors.append((pos[0] - 1, pos[1]))
            
        # Check bottom neighbor
        if pos[1] < self.rows - 1:
            neighbors.append((pos[0], pos[1] + 1))
            
        # Check top neighbor
        if pos[1] > 0:
            neighbors.append((pos[0], pos[1] - 1))
            
        return neighbors

    def draw_path(self, path, color=(89, 102, 95), border_radius=4):
        for pos in path:
            self.draw_cell(pos[0], pos[1], color, br=border_radius)
