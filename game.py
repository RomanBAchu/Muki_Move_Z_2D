import pygame
from character import Character

# Убедиться, что Pygame был инициализирован

if not pygame.get_init():
    pygame.init()

# Определение размеров окна
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Установка заголовка окна
pygame.display.set_caption("My Game")

def game_loop():
    # Создание фона
    background = pygame.image.load("fon_muk.png").convert()
    bg_scaled = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    # bg_scaled_width, bg_scaled_height = bg_scaled.get_rect().size
    # screen.blit(bg_scaled, ((SCREEN_WIDTH - bg_scaled_width) // 2, (SCREEN_HEIGHT - bg_scaled_height) // 2))
    # pygame.display.update()


    # Получение размеров изображения
    bg_width, bg_height = background.get_size()

    # Создание персонажа
    my_character = Character(136, 349, "muk.png")

    # Создание персонажа
    # my_character = Character(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    # Создаем персонажа и загружаем изображение
    # my_character = Character(136, 349, "muk.png")

    # Основной игровой цикл
    running = True

    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Добавляем возможность выхода из игры по нажатию клавиш Alt+Enter
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and (event.mod & pygame.KMOD_ALT):
                    pygame.display.toggle_fullscreen()


        # Обновление персонажа
        my_character.update(running)

        # Отрисовка экрана
        screen.blit(bg_scaled,
                    ((SCREEN_WIDTH - bg_scaled.get_width()) // 2, (SCREEN_HEIGHT - bg_scaled.get_height()) // 2))
        my_character.draw(screen)
        pygame.display.update()

        # Задержка в цикле
        pygame.time.delay(10)

        # Завершение Pygame
    pygame.quit()

if __name__ == '__main__':
    game_loop()
    # pygame.quit()