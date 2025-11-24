import pygame
class Button:
    def __init__(self, x, y, w, h, text, action):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.action = action
        self.color = (80, 80, 200)  
        self.hover_color = (100, 100, 250)  
        self.current_color = self.color

    def draw(self, screen, font):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.current_color = self.hover_color
        else:
            self.current_color = self.color

        pygame.draw.rect(screen, self.current_color, self.rect, border_radius=10)

        txt = font.render(self.text, True, (255, 255, 255))

        text_rect = txt.get_rect(center=self.rect.center)
        screen.blit(txt, text_rect)

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            self.action()

    def handle_event(self, event)
        pass
