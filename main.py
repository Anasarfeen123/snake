import pygame, time
import sys, random
import grid as gd
import snake as sn
import food as fd

pygame.init()

screen = pygame.display.set_mode((1980//2, 1980//2))
pygame.display.set_caption('Snake')
(width, height) = pygame.display.get_window_size()
print("Debug: ",width, height)
clock = pygame.time.Clock()

Running = True
grid = gd.Grid((20,20), screen)
snake = sn.Snake(grid)
food = fd.Food(grid,snake.body)
while Running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_r:
                snake = sn.Snake(grid)
                food = fd.Food(grid, snake.body)
            if event.key == pygame.K_a:
                snake.paused = not snake.paused

            if not snake.paused:
                if event.key == pygame.K_LEFT:
                    snake.chng_dir("A")
                elif event.key == pygame.K_RIGHT:
                    snake.chng_dir("D")
                elif event.key == pygame.K_UP:
                    snake.chng_dir("W")
                elif event.key == pygame.K_DOWN:
                    snake.chng_dir("S")

    if snake.paused:
        font = pygame.font.SysFont(None, 50)
        text = font.render('Paused', True, (255, 255, 255))
        screen.blit(text, (width // 2 - 50, 20))

    if not snake.paused:
        screen.fill((0, 0, 40))

        if snake.head == food.position:
            snake.grow()
            food = fd.Food(grid, snake.body)
        else:
            snake.kill(grid)
            snake.move()
        snake.draw()
        food.draw()
        grid.draw_grid()
        
        score = len(snake.body) - 3
        font = pygame.font.SysFont(None, 40)
        text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(text, (10, 10))

        pygame.display.flip()
