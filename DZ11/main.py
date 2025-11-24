import pygame
from buttons import Button
from media import load_image, play_sound

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Интерфейс с кнопками")

FONT = pygame.font.SysFont("arial", 28)

current_image = None
IMAGE_SIZE = (400, 400)

def set_image(path):
    global current_image
    img = load_image(path)
    if img:
        current_image = pygame.transform.scale(img, IMAGE_SIZE)
    else:
        current_image = None

def load_image_and_play_sound(image_path, sound_path="assets/sound.mp3"):
    set_image(image_path)
    play_sound(sound_path)

buttons = [
    Button(50, 100, 250, 60, "Картинка 1", 
           lambda: load_image_and_play_sound("assets/1img.jpg", "assets/1sound.mp3")),
           
    Button(50, 180, 250, 60, "Картинка 2", 
           lambda: load_image_and_play_sound("assets/2img.jpg", "assets/2sound.mp3")),
           
    Button(50, 260, 250, 60, "Картинка 3", 
           lambda: load_image_and_play_sound("assets/3img.jpg", "assets/3sound.mp3")),
           
    Button(50, 340, 250, 60, "Картинка 4", 
           lambda: load_image_and_play_sound("assets/4img.jpg", "assets/4sound.mp3")),
           
    Button(50, 420, 250, 60, "Картинка 5", 
           lambda: load_image_and_play_sound("assets/5img.jpg", "assets/5sound.mp3")),
]

running = True
while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for btn in buttons:
                btn.check_click(event.pos)

        for btn in buttons:
            btn.handle_event(event)

    if current_image:
        screen.blit(current_image, (350, 100))

    for btn in buttons:
        btn.draw(screen, FONT)

    pygame.display.update()

pygame.quit()
