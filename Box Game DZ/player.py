player_x = 1
player_y = 1

def get_move():
    move = input("Ваш ход (w/a/s/d): ")
    if move == "w":
        return 0, -1
    elif move == "s":
        return 0, 1
    elif move == "a":
        return -1, 0
    elif move == "d":
        return 1, 0
    else:
        print("Используй только w/a/s/d")
        return 0, 0
