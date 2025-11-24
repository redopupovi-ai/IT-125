import pygame

def load_image(path):
    try:
        img = pygame.image.load(path)
        return img
    except pygame.error as e:
        print(f"Ошибка загрузки изображения {path}: {e}")
        return None


def play_sound(path):
    try:
        sound = pygame.mixer.Sound(path)
        sound.play()
    except pygame.error as e:
        print(f"Ошибка загрузки/воспроизведения звука {path}: {e}")
    except Exception as e:
        print(f"Общая ошибка воспроизведения звука: {e}")
