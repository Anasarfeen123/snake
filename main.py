import pygame
import sys
import grid as gd
import snake as sn
import food as fd
import algo as al

pygame.init()

screen = pygame.display.set_mode((1980//2, 1980//2))
pygame.display.set_caption('Snake')
(width, height) = pygame.display.get_window_size()
print("Debug: ",width, height)
clock = pygame.time.Clock()

Running = True
Autoplay = False
Speed = 0
grid = gd.Grid((10,10), screen)
snake = sn.Snake(grid,False,(4, 1), Speed)
food = fd.Food(grid,snake.body)
assistance = True
while Running:
    screen.fill((0, 0, 40))
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
            if event.key == pygame.K_i:
                Autoplay = not Autoplay
            if event.key == pygame.K_o:
                Speed += 1
                snake.change_speed(Speed)
            if event.key == pygame.K_p:
                Speed -= 1
                snake.change_speed(Speed)
            if event.key == pygame.K_LSHIFT:
                assistance = not assistance

            if not snake.paused:
                if not Autoplay:
                    if event.key == pygame.K_LEFT:
                        snake.chng_dir("A")
                    elif event.key == pygame.K_RIGHT:
                        snake.chng_dir("D")
                    elif event.key == pygame.K_UP:
                        snake.chng_dir("W")
                    elif event.key == pygame.K_DOWN:
                        snake.chng_dir("S")
    if snake.paused and not snake.ended:
        font = pygame.font.SysFont(None, 50)
        text = font.render('Paused', True, (255, 255, 255))
        screen.blit(text, (width // 2 - 100, 20))

    if not snake.paused and not snake.ended:
        SnakeAI = al.snakeai(grid, snake, food)
        if Autoplay:
            ai_dir = SnakeAI.get_direction()
            snake.chng_dir(ai_dir)
        
        snake.kill(grid)
        next_head = (snake.head[0] + snake.direc[0], snake.head[1] + snake.direc[1])
        if next_head == food.position:
            snake.move(grow=True)
            food = fd.Food(grid, snake.body)
        else:
            snake.move()
        if SnakeAI.path and assistance:
            grid.draw_path(SnakeAI.path)
        snake.draw()
        food.draw()
        grid.draw_grid()

        score = len(snake.body) - 3
        font = pygame.font.SysFont(None, 40)
        text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(text, (10, 10))

        pygame.display.flip()