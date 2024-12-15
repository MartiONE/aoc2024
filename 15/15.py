from pprint import pp
with open("input.txt", "r") as f:
    move_dict = {
        "<": [-1, 0],
        ">": [1, 0],
        "^": [0, -1],
        "v": [0, 1]
    }
    m, moves = f.read().split("\n\n")
    map_coord = []
    robot = []
    for y, row in enumerate(m.split("\n")):
        r = []
        for x, col in enumerate(row):
            if col == "@":
                robot = [x, y]
            r.append(col)
        map_coord.append(r)
    for move in moves:
        next_coord = [robot[0]+move_dict[move][0], robot[1]+move_dict[move][1]]
        if map_coord[next_coord[1]][next_coord[0]] == ".":
            map_coord[next_coord[1]][next_coord[0]] = "@"
            map_coord[robot[1]][robot[0]] = "."
            robot = next_coord
        elif map_coord[next_coord[1]][next_coord[0]] == "O":
            push_coord = [robot[0]+(move_dict[move][0]*2), robot[1]+(move_dict[move][1]*2)]
            while map_coord[push_coord[1]][push_coord[0]] == "O":
                push_coord = [push_coord[0]+move_dict[move][0], push_coord[1]+move_dict[move][1]]
            if map_coord[push_coord[1]][push_coord[0]] == ".":
                map_coord[push_coord[1]][push_coord[0]] = "O"
                map_coord[next_coord[1]][next_coord[0]] = "@"
                map_coord[robot[1]][robot[0]] = "."
                robot = next_coord
        #print(move)
        #pp(map_coord)
    total = 0
    for y, row in enumerate(map_coord):
        for x, col in enumerate(row):
            if col == "O":
                total += 100*y + x
    print(total)