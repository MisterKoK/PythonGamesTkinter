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

# Главный игровой цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_image, (0, 0))

    # Обновление экрана
    pygame.display.flip()

# Завершение работы
pygame.quit()
