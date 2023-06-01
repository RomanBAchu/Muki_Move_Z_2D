import pygame


class Character:
    def __init__(self, x, y, character_image):
        self.start_x = x  # начальная позиция персонажа по горизонтали
        self.x = 650  # Мук рождается по горизонтали
        self.y = 592  # Мук рождается по вертикали
        self.speed = 5
        self.y_min = 100  # нижняя граница по Y
        self.y_max = 700  # верхняя граница по Y
        self.screen_width, self.screen_height = pygame.display.get_surface().get_size( # получение размеров экрана
            )
        self.scale = 1  # начальный масштаб
        self.character_image = pygame.image.load(character_image).convert_alpha( # изображение персонажа
            )
        self.jump_height = 500
        self.is_jumping = False
        self.gravity = 0.5  # сила гравитации
        self.velocity = 1  # вертикальная скорость
        self.jump_pressed = False

    def update(self, running):
        keys = pygame.key.get_pressed()  # Обработка движения персонажа
        if keys[pygame.K_LEFT]:
            self.x = max(self.x - self.speed, 50)  # ограничение движения по x до левого края экрана
        elif keys[pygame.K_RIGHT]:
            self.x = min(self.x + self.speed,
                         self.screen_width - 110)  # ограничение движения по x до правого края экрана
        elif keys[pygame.K_UP]:
            new_pos_y = max(self.y - self.speed / 200, self.y_min)
            self.move_and_scale(new_pos_y)  # перемещение и масштабирование при движении вверх
        elif keys[pygame.K_DOWN]:
            new_pos_y = min(self.y + self.speed / 200, self.y_max)
            self.move_and_scale(new_pos_y)  # перемещение и масштабирование при движении вниз
        elif keys[pygame.K_SPACE] and not self.is_jumping and not self.jump_pressed:
            self.jump_pressed = True
            self.is_jumping = True
            self.jump()
        if self.is_jumping:
            self.perform_jump()
        else:
            # self.velocity += self.gravity  # изменение вертикальной скорости
            # self.y += self.velocity  # изменение вертикальной позиции
            if self.y >= self.y_max:
                self.y = self.y_max
                self.velocity = 0  # остановка падения на земле
            elif self.y <= self.y_min:
                self.y = self.y_min
                self.velocity = 0  # остановка взлета при достижении верхней границы
        if not running:
            pygame.quit()
        else:
            return

    def perform_jump(self):
        if self.jump_height >= 10:
            self.y -= self.jump_height
            self.jump_height -= 100
        else:
            self.is_jumping = False
            self.jump_height = 100
            # Возвращение на исходную позицию после прыжка
            # self.x = self.start_x
            self.gravity = 0.3  # сила гравитации
            self.velocity = 0  # вертикальная скорость

    def jump(self):
        self.jump_height = 50

    def draw(self, screen):
        # Меняем цвет круга в зависимости от масштаба
        # color_r = max(min(int(self.scale * 100), 255), 0)
        # color_b = max(min(int((1 - self.scale) * 100), 255), 0)
        # pygame.draw.circle(screen, (color_r, 0, color_b), (self.x, self.y), int(60 * self.scale))  # Отрисовка персонажа
        character_rect = self.character_image.get_rect(center=(self.x, self.y))
        character_scaled_image = pygame.transform.scale(self.character_image,
                                                        (int(110 * self.scale), int(280 * self.scale)))
        screen.blit(character_scaled_image, character_rect)

    def move_and_scale(self, new_pos_y):
        if new_pos_y > self.y:
            # Двигаем персонажа вниз и увеличиваем его масштаб
            self.scale += 0.01
            self.y = new_pos_y
        else:
            # Двигаем персонажа вверх и уменьшаем его масштаб
            self.scale -= 0.01
            self.y = new_pos_y
        # Ограничение масштаба персонажа от 0.5 до 1.5
        self.scale = max(min(self.scale, 2), 0.5)  # ограничение масштабирования от 0.5 до 2.0

    def reset_position(self):
        self.x = self.start_x
        self.y = 592
        self.scale = 1
        self.is_jumping = False
        self.jump_pressed = False
        self.gravity = 0.5
        self.velocity = 1

    def set_image(self, character_image):
        self.character_image = pygame.image.load(character_image).convert_alpha()





# import pygame
#
# class Character:
#     def __init__(self, x, y, character_image):
#         self.start_x = x  # начальная позиция персонажа по горизонтали
#         self.x = 100 # Мук рождается по горизонтали
#         self.y = 592    # Мук рождается по вертикали
#         self.speed = 5
#         self.y_min = 100  # нижняя граница по Y
#         self.y_max = 700  # верхняя граница по Y
#         self.screen_width, self.screen_height = pygame.display.get_surface().get_size()  # получение размеров экрана
#         self.scale = 1  # начальный масштаб
#         self.character_image = pygame.image.load(character_image).convert_alpha()  # изображение персонажа
#         self.jump_height = 500
#         self.is_jumping = False
#
#         self.gravity = 0.5  # сила гравитации
#         self.velocity = 1  # вертикальная скорость
#         self.jump_pressed = False
#
#     def update(self, running):
#         keys = pygame.key.get_pressed()  # Обработка движения персонажа
#         if keys[pygame.K_LEFT]:
#             self.x = max(self.x - self.speed, 50)  # ограничение движения по x до левого края экрана
#         elif keys[pygame.K_RIGHT]:
#             self.x = min(self.x + self.speed, self.screen_width - 110)  # ограничение движения по x до правого края экрана
#         elif keys[pygame.K_UP]:
#             new_pos_y = max(self.y - self.speed / 200, self.y_min)
#             self.move_and_scale(new_pos_y)  # перемещение и масштабирование при движении вверх
#         elif keys[pygame.K_DOWN]:
#             new_pos_y = min(self.y + self.speed / 200, self.y_max)
#             self.move_and_scale(new_pos_y)  # перемещение и масштабирование при движении вниз
#         elif keys[pygame.K_SPACE] and not self.is_jumping and not self.jump_pressed:
#
#             self.jump_pressed = True
#             self.is_jumping = True
#             self.jump()
#
#         if self.is_jumping:
#             self.perform_jump()
#
#
#         else:
#             self.velocity += self.gravity  # изменение вертикальной скорости
#             self.y += self.velocity  # изменение вертикальной позиции
#             #
#             if self.y >= self.y_max:
#                 self.y = self.y_max
#                 self.velocity = 0  # остановка падения на земле
#             elif self.y <= self.y_min:
#                 self.y = self.y_min
#                 self.velocity = 0  # остановка взлета при достижении верхней границы
#         if not running:
#             pygame.quit()
#         else:
#             return
#
#     def perform_jump(self):
#         if self.jump_height >= 10:
#             self.y -= self.jump_height
#             self.jump_height -= 100
#         else:
#             self.is_jumping = False
#             self.jump_height = 100
#             # Возвращение на исходную позицию после прыжка
#             # self.x = self.start_x
#
#             self.gravity = 0.3  # сила гравитации
#             self.velocity = 0  # вертикальная скорость
#
#
#     def jump(self):
#         self.jump_height = 50
#
#     def draw(self, screen):
#         # Меняем цвет круга в зависимости от масштаба
#         # color_r = max(min(int(self.scale * 100), 255), 0)
#         # color_b = max(min(int((1 - self.scale) * 100), 255), 0)
#         # pygame.draw.circle(screen, (color_r, 0, color_b), (self.x, self.y), int(60 * self.scale))  # Отрисовка персонажа
#         character_rect = self.character_image.get_rect(center=(self.x, self.y))
#         character_scaled_image = pygame.transform.scale(self.character_image, (int(120 * self.scale), int(280 * self.scale)))
#         screen.blit(character_scaled_image, character_rect)
#
#     def move_and_scale(self, new_pos_y):
#         if new_pos_y > self.y:
#             # Двигаем персонажа вниз и увеличиваем его масштаб
#             self.scale += 0.01
#             self.y = new_pos_y
#         else:
#             # Двигаем персонажа вверх и уменьшаем его масштаб
#             self.scale -= 0.01
#             self.y = new_pos_y
#         # Ограничение масштаба персонажа от 0.5 до 1.5
#         self.scale = max(min(self.scale, 1.5), 0.5)
#
