import pygame as pg
from pygame import mixer
import random

pg.display.set_caption('snake tripgraff')
icon = pg.image.load("img/snake-icon-new.png")
pg.display.set_icon(icon)

wsize = (1020, 750)

screen = pg.display.set_mode(wsize)

tside = 30
msize = wsize[0] // tside, wsize[1] // tside

start_pos = msize[0] // 2, msize[1] // 2
snake = [start_pos]
alive = True

direction = 0
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

apple = random.randint(0, msize[0]), random.randint(0, msize[1])

fps = 5
clock = pg.time.Clock()

pg.font.init()
font_score = pg.font.SysFont("Poppins", 45)
font_gameover = pg.font.Font("fonts/PressStart2P-Regular.ttf", 50)
font_space = pg.font.Font("fonts/RussoOne-Regular.ttf", 30)
font_table = pg.font.SysFont("Poppin", 30)
font_hero = pg.font.SysFont("Poppins", 25)
font_version =pg.font.Font("fonts/RussoOne-Regular.ttf", 15)
font_tg = pg.font.Font("fonts/Raleway-Light.ttf", 11)

image = pg.image.load('img/qr-code.png').convert_alpha()
apple_img=pg.image.load('img/apple.png').convert_alpha()
byme=pg.image.load('img/vodznak.png').convert_alpha()


running = True
while running:
    clock.tick(fps)
    screen.fill("#5d6d7e")
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if alive:
                if event.key == pg.K_d:
                    direction = 0
                if event.key == pg.K_s:
                    direction = 1
                if event.key == pg.K_a:
                    direction = 2
                if event.key == pg.K_w:
                    direction = 3
            else:
                if event.key == pg.K_SPACE:
                    alive = True
                    snake = [start_pos]
                    apple = random.randint(0, msize[0]-1), random.randint(0, msize[1]-1)
                    fps = 5

#9bffa5
    [pg.draw.rect(screen, "#9bffa5", ( x * tside, y * tside, tside -1, tside -1)) for x, y in snake]
    pg.draw.rect(screen, "#db7093", (apple[0] * tside, apple[1] * tside, tside-1, tside-1))
#aed6f1
#db7093
    if alive:
        new_pos = snake[0][0] + directions[direction][0], snake[0][1] + directions[direction][1]
        if not (0 <= new_pos[0] < msize[0] and 0 <= new_pos[1] < msize[1]) or \
                new_pos in snake:
            mixer.init()
            mixer.music.load("effects/opium.mp3")
            mixer.music.set_volume(0.7)
            mixer.music.play(0)
            alive = False
        else:
            snake.insert(0, new_pos)
            if new_pos == apple:
                fps += 0.5
                mixer.init()
                mixer.music.load("effects/eat.mp3")
                mixer.music.set_volume(1)
                mixer.music.play(1)
                apple = random.randint(0, msize[0]-1), random.randint(0, msize[1]-1)
            else:
                snake.pop(-1)

    else:
        text = font_gameover.render(f"GAME OVER", True, "#aed6f1")
        screen.blit(text, (wsize[0] // 2 - text.get_width()//2, wsize[1] // 2 - 50))
        text = font_space.render(f"Press SPACE for restart", True, "white")
        screen.blit(text, (wsize[0] // 2 - text.get_width() // 2, wsize[1] // 2 + 10))
        screen.blit(font_table.render(f"Table of records:", True, "white"), (850, 0))
        screen.blit(font_hero.render(f"1.hekitgm - 85", True, "white"), (892,20))
        screen.blit(font_hero.render(f"2.chipa-75", True, "white"), (892,40))
        screen.blit(font_hero.render(f"3.ITuXa-74", True, "white"), (892,60))
        screen.blit(font_hero.render(f"4.sekaasik-73", True, "white"), (892,80))
        screen.blit(font_hero.render(f"5.kriesper-67", True, "white"), (892,100))
        screen.blit(font_hero.render(f"6.stas-47", True, "white"), (892,120))
        screen.blit(font_tg.render(f"Хочешь попасть сюда? tg:@snake_tripgraff", True, "white"), (790,140))
        screen.blit(font_tg.render(f"Акктуальная таблица рекордов тут ^^^", True, "white"), (790,160))
        screen.blit(image, (765,0))
        screen.blit(byme, (880,640))
        #screen.blit(font_hero.render(f"game by. tripgraff", True, "white"), (870, 720))
        screen.blit(font_version.render(f"version 0.0.13", True, "white"), (5, 720))


    screen.blit(font_score.render(f"{len(snake)}", True, "white"), (50, 9))
    screen.blit(apple_img, (5,5))

    pg.display.flip()



