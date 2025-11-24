# media.py
import pygame

def load_image(path):
    # ... (код для загрузки и конвертации, который возвращает Surface или None)
    try:
        img = pygame.image.load(path)
        # ... (конвертация)
        return img
    except pygame.error as e:
        print(f"Ошибка загрузки изображения {path}: {e}")
        return None # <-- Это критично!


def play_sound(path):
    """Загружает и проигрывает звуковой файл как эффект."""
    try:
        # Используем Sound для коротких эффектов (вместо pygame.mixer.music)
        sound = pygame.mixer.Sound(path)
        sound.play()
    except pygame.error as e:
        print(f"Ошибка загрузки/воспроизведения звука {path}: {e}")
    except Exception as e:
        # Эта ветка ловит ошибки, если микшер не был инициализирован
        print(f"Общая ошибка воспроизведения звука: {e}")