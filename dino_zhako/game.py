from objects import *
from levels import *

pygame.init()

'''кнопка для меню'''
btn_play = Button(465, 250, 350, 100, (170, 139, 231), 'PLAY', 60, (255, 255, 255))
btn_instructions = Button(465, 400, 350, 100, (170, 139, 231), 'INSTRUCTIONS', 60, (255, 255, 255))
btn_exit = Button(465, 500, 350, 100, (170, 139, 231), 'EXIT', 60, (255, 255, 255))

mode = 'menu'

game = True
finish = False
while game:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    if mode == 'menu':
        window.blit(bg, (0,0))
        window.blit(game_name, (200, 50))

        btn_play.draw(120, 30)
        btn_instructions.draw(25, 30)
        btn_exit.draw(120, 30)

    pygame.display.update()
    clock.tick(FPS)