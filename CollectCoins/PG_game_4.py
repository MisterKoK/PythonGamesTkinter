# Чтобы не выходил за пределы игрового поля см. строки 52

import pygame

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


# Создание игрока через класс
player = Player(width // 2, height // 2)


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

    # Обновление экрана
    pygame.display.flip()

# Завершение работы
pygame.quit()
