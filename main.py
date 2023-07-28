import pygame as pg
import random as rd

from time import sleep

# initialize pygame
pg.init()

x = 720  # x dimension
y = 480  # y dimension

# inititalize window
pg.display.set_caption("Snake Game")
window = pg.display.set_mode((x, y))


class Colors:
    black = pg.Color(0, 0, 0)
    white = pg.Color(255, 255, 255)

    background = pg.Color(28, 28, 28)  # dark-gray
    snake = [34, 48, 34]               # light-green
    fruit = [235, 149, 103]            # light-orange


class Snake:
    pos = [200, 100]                                        # start position (x, y)
    bdy = [[200, 100], [180, 100], [160, 100], [140, 100]]  # body (blocks)
    spd = 7.5                                               # speed


class Fruit:
    pos = [rd.randrange(1, (x // 20)) * 20,            # start position (x)
           rd.randrange(1, (y // 20)) * 20]            # start position (y)
    spawn = True                                       # spawn


def displayScore(score):
    font = pg.font.Font('VT323-Regular.ttf', 50)

    surf = font.render(str(score), True, Colors.white)
    rect = surf.get_rect()

    window.blit(surf, rect)


def gameOver(score):
    font = pg.font.Font('VT323-Regular.ttf', 50)

    surf = font.render("GAME OVER\nscore : " + str(score), True, Colors.white)
    rect = surf.get_rect()
    rect.midtop = (x / 2, y / 4)

    window.blit(surf, rect)
    pg.display.flip()

    sleep(1)
    pg.quit()
    quit()


def main():

    score = 0
    direction = 'R'

    while True:

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:

                if event.key == pg.K_UP and direction != 'D':
                    direction = 'U'
                elif event.key == pg.K_DOWN and direction != 'U':
                    direction = 'D'
                elif event.key == pg.K_LEFT and direction != 'R':
                    direction = 'L'
                elif event.key == pg.K_RIGHT and direction != 'L':
                    direction = 'R'

        if direction == 'U':
            Snake.pos[1] -= 20
        elif direction == 'D':
            Snake.pos[1] += 20
        elif direction == 'L':
            Snake.pos[0] -= 20
        elif direction == 'R':
            Snake.pos[0] += 20

        Snake.bdy.insert(0, list(Snake.pos))
        if Snake.pos[0] == Fruit.pos[0] and Snake.pos[1] == Fruit.pos[1]:
            score += 1
            Fruit.spawn = False
        else:
            Snake.bdy.pop()

        if Fruit.spawn is False:
            Fruit.pos = [rd.randrange(1, (x // 20)) * 20,
                         rd.randrange(1, (y // 20)) * 20]

        Fruit.spawn = True
        window.fill(Colors.black)

        RGB = [Colors.snake[0], Colors.snake[1], Colors.snake[2]]
        for p in Snake.bdy:
            for i in range(2):
                if RGB[i] + 10 <= 255:
                    RGB[i] += 10
                else:
                    RGB[i] = 255
            pg.draw.rect(window, pg.Color(RGB[0], RGB[1], RGB[2]), pg.Rect(p[0], p[1], 20, 20))

        pg.draw.rect(window, Colors.fruit, pg.Rect(Fruit.pos[0], Fruit.pos[1], 20, 20))

        if x - 19 > Snake.pos[0] > -1 and y - 19 > Snake.pos[1] > -4:
            pass
        else:
            gameOver(score)
        for b in Snake.bdy[1:]:
            if Snake.pos[0] == b[0] and Snake.pos[1] == b[1]:
                gameOver(score)

        displayScore(score)
        pg.display.update()
        pg.time.Clock().tick(Snake.spd)


main()

