# Исправляем отображение подсчета монет стр.59

import pygame
import random

# Инициализация пайгейм
pygame.init()

# Определение размеров окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Загружаю рисунки
pygame.display.set_icon(pygame.image.load("images/icon.png"))
background_image = pygame.image.load('images/bg.png')
player_image = pygame.image.load('images/player.png')
coin_image = pygame.image.load('images/coin.png')
pygame.display.set_caption("RPG")

player_image.set_colorkey((0, 0, 0))  # убираем черный цвет

# Для рисования надписи подсчет очков
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

# count_coin переменная сколько монет собрали
coins_count = 0

# Класс для представления игрока
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5

    def move(self, dx, dy):
        self.x += dx * self.speed
        self.y += dy * self.speed

    def draw(self):
        screen.blit(player_image, (self.x, self.y))
        # pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 10)  # можно рисовать круги, так пример



# Класс для представления монетки
class Coin:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        screen.blit(coin_image, (self.x, self.y))


    # Функция для проверки пересечения с монетой.
    # При пересечении кладем монету в корзину
    def update(self):
        global coins_count
        # print('START COIN UPDATE')
       # если персонаж пересекается с монеткой
        print(self.x // 100, self.y // 100, 'координаты монеты')
        print(player.x // 100, player.y // 100, 'координаты плейер')
        if self.x // 100 == player.x // 100 and self.y // 100 == player.y // 100:
            self.x = 700
            self.y = 500
            print('kill')
            coins_count = coins_count + 1


# Создание игрока через класс
player = Player(width // 2, height // 2)
# Создаем монеты. В список их.
coins = []
for _ in range(10):
    x = random.randint(0, width)
    y = random.randint(0, height)
    coins.append(Coin(x, y))
    #print(Coin.__dict__)
    print(Coin.__name__)
    # print(coins) # для проверки можно напечатать, посмотреть создает он объекты ваще или нет

# Главный игровой цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обработка нажатий клавиш
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.x > 0:  # x > 0, это движение налево и проверка границ
        player.move(-1, 0)
    if keys[pygame.K_RIGHT] and player.x < 760:
        player.move(1, 0)
    if keys[pygame.K_UP] and player.y > 0:
        player.move(0, -1)
    if keys[pygame.K_DOWN] and player.y < 560:
        player.move(0, 1)

    # Очистка экрана
    screen.fill((0, 0, 0))

    # Фон
    screen.blit(background_image, (0, 0))

    # Отрисовка игрока и монеток
    player.draw()
    for coin in coins:
        coin.draw()
        coin.update()

#    collide = pygame.sprite.spritecollide(coin, player, False)

#    print(collide)

    # рисуем надпись
    textsurface = myfont.render(f'Coins: {coins_count}', False, (255, 255, 255))
    screen.blit(textsurface, (20, 20))

    # Обновление экрана
    pygame.display.flip()

# Завершение работы
pygame.quit()
