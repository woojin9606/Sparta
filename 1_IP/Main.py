import sys
import pygame as pg
import pygame.image

import Number

YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (150, 150, 150)
temp = [0,0]

def main():
    pg.init()
    pg.display.set_caption('Bulls and Cows')

    clock = pg.time.Clock()
    window = pg.display.set_mode((1000, 800))

    img = pygame.image.load("main.jpg")
    img = pygame.transform.scale(img, (1000,800))

    # white color
    color = (255, 255, 255)

    # light shade of the button
    color_light = (170, 170, 170)

    # dark shade of the button
    color_dark = (100, 100, 100)

    # stores the width of the
    # screen into a variable
    width = 1400

    # stores the height of the
    # screen into a variable
    height = 1000

    # defining a font
    smallfont = pg.font.SysFont('Corbel', 35)

    # rendering a text written in
    # this font
    ball3_text = smallfont.render('3ball-mode', True, color)
    ball4_text = smallfont.render('4ball-mode', True, color)
    main_text = smallfont.render('Bulls and Cows', True, color)

    while True:

        for ev in pg.event.get():

            if ev.type == pg.QUIT:
                pg.quit()

            # checks if a mouse is clicked
            if ev.type == pg.MOUSEBUTTONDOWN:

                # if the mouse is clicked on the
                # button the game is terminated
                if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                    threeball_game = Number.threeNumber()
                    threeball_game.ran()
                    game_3ball(threeball_game)
                if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 + 100 <= mouse[1] <= height / 2 + 140:
                    fourball_game = Number.fourNumber()
                    fourball_game.ran()
                    game_4ball(fourball_game)

        # fills the screen with a color
        window.blit(img,(0,0))

        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pg.mouse.get_pos()

        # if mouse is hovered on a button it
        # changes to lighter shade
        if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
            pg.draw.rect(window, color_light, [width / 2, height / 2, 200, 40])

        else:
            pg.draw.rect(window, color_dark, [width / 2, height / 2, 200, 40])

        if width / 2 <= mouse[0] <= width / 2 + 140 and height  / 2 +100 <= mouse[1] <= height / 2 + 140:
            pg.draw.rect(window, color_light, [width / 2, height / 2 + 100, 200, 40])

        else:
            pg.draw.rect(window, color_dark, [width / 2, height / 2 + 100, 200, 40])

        # superimposing the text onto our button
        window.blit(ball3_text, (width / 2 +25 , height / 2))
        window.blit(ball4_text, (width / 2 +25, height / 2+100))
        window.blit(main_text,(400,200))


        # updates the frames of the game
        pg.display.update()
        clock.tick(10)  # 60 frame 설정


def gameover():
    pg.init()
    pg.display.set_caption('Bulls and Cows')

    clock = pg.time.Clock()
    window = pg.display.set_mode((1000, 800))

    # white color
    color = (255, 255, 255)

    # light shade of the button
    color_light = (170, 170, 170)

    # dark shade of the button
    color_dark = (100, 100, 100)

    # stores the width of the
    # screen into a variable
    width = 1000

    # stores the height of the
    # screen into a variable
    height = 800

    # defining a font
    smallfont = pg.font.SysFont('Corbel', 35)

    # rendering a text written in
    # this font
    ball3_text = smallfont.render('Main Menu', True, color)
    ball4_text = smallfont.render('EXIT', True, color)
    main_text = smallfont.render('Game Over', True, color)

    while True:

        for ev in pg.event.get():

            if ev.type == pg.QUIT:
                pg.quit()

            # checks if a mouse is clicked
            if ev.type == pg.MOUSEBUTTONDOWN:

                # if the mouse is clicked on the
                # button the game is terminated
                if 400 <= mouse[0] <= 400 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                    main()
                if 400 <= mouse[0] <= 400 + 140 and height / 2 + 100 <= mouse[1] <= height / 2 + 140:
                    pg.quit()

        # fills the screen with a color
        window.fill((60,25,60))

        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pg.mouse.get_pos()

        # if mouse is hovered on a button it
        # changes to lighter shade
        if 400 <= mouse[0] <= 400 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
            pg.draw.rect(window, color_light, [400, height / 2, 200, 40])

        else:
            pg.draw.rect(window, color_dark, [400, height / 2, 200, 40])

        if 400 <= mouse[0] <= 400 + 140 and height  / 2 +100 <= mouse[1] <= height / 2 + 140:
            pg.draw.rect(window, color_light, [400, height / 2 + 100, 200, 40])

        else:
            pg.draw.rect(window, color_dark, [400, height / 2 + 100, 200, 40])

        # superimposing the text onto our button
        window.blit(ball3_text, (400 , height / 2))
        window.blit(ball4_text, (400, height / 2+100))
        window.blit(main_text, (400, 200))

        # updates the frames of the game
        pg.display.update()
        clock.tick(10)  # 60 frame 설정


def clear():
    pg.init()
    pg.display.set_caption('Bulls and Cows')

    clock = pg.time.Clock()
    window = pg.display.set_mode((1000, 800))

    # white color
    color = (255, 255, 255)

    # light shade of the button
    color_light = (170, 170, 170)

    # dark shade of the button
    color_dark = (100, 100, 100)

    # stores the width of the
    # screen into a variable
    width = 1000

    # stores the height of the
    # screen into a variable
    height = 800

    # defining a font
    smallfont = pg.font.SysFont('Corbel', 35)

    # rendering a text written in
    # this font
    main_text = smallfont.render('Main Menu', True, color)
    exit_text = smallfont.render('EXIT', True, color)
    clear_text = smallfont.render('Clear', True, color)

    while True:

        for ev in pg.event.get():

            if ev.type == pg.QUIT:
                pg.quit()

            # checks if a mouse is clicked
            if ev.type == pg.MOUSEBUTTONDOWN:

                # if the mouse is clicked on the
                # button the game is terminated
                if 400 <= mouse[0] <= 400 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                    main()
                if 400 <= mouse[0] <= 400 + 140 and height / 2 + 100 <= mouse[1] <= height / 2 + 140:
                    pg.quit()

        # fills the screen with a color
        window.fill((60,25,60))

        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pg.mouse.get_pos()

        # if mouse is hovered on a button it
        # changes to lighter shade
        if 400 <= mouse[0] <= 400 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
            pg.draw.rect(window, color_light, [400, height / 2, 200, 40])

        else:
            pg.draw.rect(window, color_dark, [400, height / 2, 200, 40])

        if 400 <= mouse[0] <= 400 + 140 and height  / 2 +100 <= mouse[1] <= height / 2 + 140:
            pg.draw.rect(window, color_light, [400, height / 2 + 100, 200, 40])

        else:
            pg.draw.rect(window, color_dark, [400, height / 2 + 100, 200, 40])

        # superimposing the text onto our button
        window.blit(main_text, (400 , height / 2))
        window.blit(exit_text, (400, height / 2+100))
        window.blit(clear_text, (400, 200))

        # updates the frames of the game
        pg.display.update()
        clock.tick(10)  # 60 frame 설정



def game_3ball(object):
    pg.init()
    pg.display.set_caption('Bulls and Cows')#상단 제목 설정


    clock = pg.time.Clock()
    screen = pg.display.set_mode((1000, 800))
    font = pg.font.Font(None, 32)
    input_box = pg.Rect(400, 700, 200, 32)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    a=''
    count =0
    img = pygame.image.load("main.jpg")
    img = pygame.transform.scale(img, (1000, 800))
    global temp

    while True:

        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if e.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(e.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if e.type == pg.KEYDOWN:
                if active:
                    if e.key == pg.K_RETURN:
                        if len(text)==3:
                            try:
                                temp=object.cal(int(text[0]),int(text[1]),int(text[2]))
                                text = ''
                                a = 'strike : ' + str(temp[0]) + ' ball : ' + str(temp[1])
                                count += 1
                                if temp[0] == 3:
                                    clear()
                                if count == 9:
                                    gameover()
                            except:
                                a = 'Please input number'
                                text = ''

                        else:
                            text = ''
                            a = '3number please'

                    elif e.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += e.unicode



        screen.blit(img,(0,0))



        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)

        # Text를 surface에 그리기, 안티알리어싱, 검은색
        text_Title = font.render(a, True, BLACK)
        b=9-count
        score_text = font.render('Life : '+str(b), True, BLACK)


        # Text Surface SCREEN에 복사하기, Rect 사용
        screen.blit(text_Title, (400,100))
        screen.blit(score_text, (800, 0))

        pg.display.flip()

        clock.tick(10)  # 60 frame 설정




def game_4ball(object):
    pg.init()
    pg.display.set_caption('Bulls and Cows')#상단 제목 설정

    clock = pg.time.Clock()
    screen = pg.display.set_mode((1000, 800))
    font = pg.font.Font(None, 32)
    input_box = pg.Rect(400, 700, 200, 32)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    a= ''
    count = 0
    img = pygame.image.load("main.jpg")
    img = pygame.transform.scale(img, (1000, 800))
    global temp

    while True:

        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if e.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(e.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if e.type == pg.KEYDOWN:
                if active:
                    if e.key == pg.K_RETURN:
                        if len(text)==4:
                            try:
                                temp=object.cal(int(text[0]),int(text[1]),int(text[2]),int(text[3]))
                                text = ''
                                a = 'strike : '+str(temp[0])+' ball : '+str(temp[1])
                                count += 1
                                if temp[0] == 4:
                                    clear()
                                if count == 9:
                                    gameover()
                            except:
                                a = 'Please input number'
                                text = ''
                        else:
                            text = ''
                            a = '4number please'

                    elif e.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += e.unicode



        screen.blit(img,(0,0))

        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)

        # Text를 surface에 그리기, 안티알리어싱, 검은색
        text_Title = font.render(a, True, BLACK)

        b = 9 - count
        score_text = font.render('Life : ' + str(b), True, BLACK)

        # Text Surface SCREEN에 복사하기, Rect 사용
        screen.blit(text_Title, (400, 100))
        screen.blit(score_text, (800, 0))

        pg.display.flip()

        clock.tick(10)  # 60 frame 설정




if __name__ == '__main__':
    main()

