def draw_map(box, player_x, player_y):
    for y in range(len(box)):
        line = box[y]
        if y == player_y:
            line = line[:player_x] + "A" + line[player_x + 1:]
        print(line)


def check_cell(box, x, y):
    cell = box[y][x]
    if cell == "#":
        return "wall"
    elif cell == "*":
        return "exit"
    else:
        return "empty"
