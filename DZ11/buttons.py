import pygame


class Button:
    def __init__(self, x, y, w, h, text, action):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.action = action
        self.color = (80, 80, 200)  # Основной синий цвет
        self.hover_color = (100, 100, 250)  # Цвет при наведении
        self.current_color = self.color

    def draw(self, screen, font):
        # Обновляем цвет в зависимости от положения курсора
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.current_color = self.hover_color
        else:
            self.current_color = self.color

        # Рисуем прямоугольник кнопки
        pygame.draw.rect(screen, self.current_color, self.rect, border_radius=10)

        # Рендерим текст
        txt = font.render(self.text, True, (255, 255, 255))

        # Центрируем текст внутри кнопки
        text_rect = txt.get_rect(center=self.rect.center)
        screen.blit(txt, text_rect)

    def check_click(self, pos):
        """Проверяет, был ли клик внутри кнопки, и выполняет действие."""
        if self.rect.collidepoint(pos):
            self.action()

    def handle_event(self, event):
        """Для обработки событий, если нужно добавить дополнительные эффекты (напр. отпускание кнопки).
        В этом базовом варианте можно не вызывать, но оставлено для расширяемости.
        """
        pass