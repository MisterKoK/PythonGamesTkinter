import pygame

FPS = 70  # частота кадров в секунду
pygame.init()
window = pygame.display.set_mode((1280, 720))
pygame.display.set_icon(pygame.image.load("images/icon.png"))
pygame.display.set_caption("Alchemy")
# слои
screen = pygame.Surface((1280, 720))
layout_image_1 = pygame.Surface((200, 200))  # слой под 1 картинку
layout_image_2 = pygame.Surface((200, 200))  # слой под 2 картинку
layout_image_3 = pygame.Surface((200, 200))
layout_image_4 = pygame.Surface((200, 200))

# загружаем рисунки
background_image = pygame.image.load('images/background.png')
image_1 = pygame.image.load('images/1.png')
image_2 = pygame.image.load('images/2.png')
image_3 = pygame.image.load('images/3.png')
image_4 = pygame.image.load('images/4.png')
image_1.set_colorkey((0, 0, 0))  # убираем черный цвет
image_2.set_colorkey((0, 0, 0))
image_3.set_colorkey((0, 0, 0))
image_4.set_colorkey((0, 0, 0))

# Загрузка мелодий игры
shoot_sound = pygame.mixer.Sound('images/pew.wav')

# Координаты картинок
x_1 = 50
y_1 = 100
x_2 = 50
y_2 = 400
x_3 = 1000
y_3 = 1000
x_4 = 1000
y_4 = 1000


done = False
clock = pygame.time.Clock()
selected_element = None
mouse_x, mouse_y = 0, 0
is_dragging = False
left_keypressed = False  # нажата левая кнопка

# selected_element = None

while not done:  # игровой цикл
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = True
            pygame.quit()
            quit()

        # движение игрока, обратабываем нажатие кнопок
        if y_1 < 360 and e.type == pygame.KEYDOWN and e.key == pygame.K_s:  # вниз
            y_1 += 10
        elif e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            print('MOUSEBUTTONDOWN', mouse_x, mouse_y)
            if x_1 <= mouse_x <= x_1 + layout_image_1.get_width() and \
                    x_1 <= mouse_y <= x_1 + layout_image_1.get_height():
                selected_element = layout_image_1
                left_keypressed = True
            elif x_2 <= mouse_x <= x_2 + layout_image_2.get_width() and \
                    y_2 <= mouse_y <= y_2 + layout_image_2.get_height():
                selected_element = layout_image_2
                left_keypressed = True

            elif x_3 <= mouse_x <= x_3 + layout_image_3.get_width() and \
                    y_3 <= mouse_y <= y_3 + layout_image_3.get_height():
                selected_element = layout_image_3
                left_keypressed = True

        # следим за передвижением мыши
        elif e.type == pygame.MOUSEMOTION:
            # mouse_x, mouse_y = pygame.mouse.get_pos()
            # print('MOUSEMOTION', mouse_x, mouse_y)
            if left_keypressed:
                player_position = pygame.mouse.get_pos()
                mouse_x = player_position[0]
                mouse_y = player_position[1]
                print('MOUSEMOTION', mouse_x, mouse_y)

        # Отпускаем кнопку мыши
        elif e.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()  # получаем координаты
            left_keypressed = False
            print('MOUSEBUTTONUP', mouse_x, mouse_y)
            # Наложились слои один на другой. Первая комбинация.
            if abs(x_1 - x_2) < 150 and \
                    abs(y_1 - y_2) < 150:
                print('наложились 1-2')
                shoot_sound.play()  # звук при попадании
                # раскидываем элементы по координатам
                x_3, y_3 = mouse_x, mouse_y
                x_1 = 50
                y_1 = 100
                x_2 = 50
                y_2 = 400
            # вторая комбинация
            elif abs(x_2 - x_3) < 150 and \
                    abs(y_2 - y_3) < 150:
                print('наложились 2-3')
                shoot_sound.play()  # звук при попадании
                # раскидываем элементы по координатам
                x_4, y_4 = mouse_x, mouse_y
                x_1 = 50
                y_1 = 100
                x_2 = 50
                y_2 = 400

                x_3 = 1000
                y_3 = 100

        # если нажата ЛКМ и выбран элемент
        if left_keypressed and selected_element:
            selected_element_x, selected_element_y = selected_element.get_size()
            selected_element_x /= 2
            selected_element_y /= 2
            x = mouse_x - selected_element_x
            y = mouse_y - selected_element_y
            if selected_element == layout_image_1:
                x_1, y_1 = x, y
            elif selected_element == layout_image_2:
                x_2, y_2 = x, y

            elif selected_element == layout_image_3:
                x_3, y_3 = x, y

        #  Отображение рисунков
        layout_image_1.blit(image_1, (0, 0))
        layout_image_2.blit(image_2, (0, 0))
        layout_image_3.blit(image_3, (0, 0))
        layout_image_4.blit(image_4, (0, 0))
        # zet.blit(img_z,(0,0))

        screen.blit(background_image, (0, 0))  # сначала фон
        screen.blit(image_1, (x_1, y_1))  # позиция отображения первой картинки
        screen.blit(image_2, (x_2, y_2))  # позиция отображения второй картинки
        screen.blit(image_3, (x_3, y_3))
        screen.blit(image_4, (x_4, y_4))

        # screen.blit(player, (x_p, y_p)) # позиция отображения игрока

        window.blit(screen, (0, 0))  # координаты это фон
        # pygame.display.update()  # обновить команду
        pygame.display.flip()
        clock.tick(FPS)  # Держим цикл на правильной скорости

pygame.quit()
