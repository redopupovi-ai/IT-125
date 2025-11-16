from Karta import box
from player import player_x, player_y, get_move
from Game import draw_map, check_cell



while True:
    draw_map(box, player_x, player_y)

    dx, dy = get_move()
    new_x = player_x + dx
    new_y = player_y + dy

    result = check_cell(box, new_x, new_y)

    if result == "wall":
        print("Ты врезался в стену, игра закончена.")
        break
    elif result == "exit":
        print("Ты выбрался!")
        break
    else:
        player_x, player_y = new_x, new_y
