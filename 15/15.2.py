with open("example.txt", "r") as f:
    move_dict = {
        "<": [-1, 0],
        ">": [1, 0],
        "^": [0, -1],
        "v": [0, 1]
    }
    subs_dict = {
        "#": "##",
        ".": "..",
        "O": "[]",
        "@": "@."
    }
    m, moves = f.read().split("\n\n")
    map_coord = []
    robot = []
    for y, row in enumerate(m.split("\n")):
        r = []
        for x, col in enumerate(row):
            r += subs_dict[col]
        if "@" in r:
            robot = [r.index("@"), y]
        map_coord.append(r)
    print(*map_coord, sep='\n')
    print(robot)
    for move in moves:
        next_coord = [robot[0]+move_dict[move][0], robot[1]+move_dict[move][1]]
        if map_coord[next_coord[1]][next_coord[0]] == ".":
            map_coord[next_coord[1]][next_coord[0]] = "@"
            map_coord[robot[1]][robot[0]] = "."
            robot = next_coord
        elif map_coord[next_coord[1]][next_coord[0]] in ["[", "]"]:
            if move in ["<", ">"]:
                push_coord = [robot[0]+(move_dict[move][0]*2), robot[1]+(move_dict[move][1]*2)]
                while map_coord[push_coord[1]][push_coord[0]] in ["[", "]"]:
                    push_coord = [push_coord[0]+move_dict[move][0], push_coord[1]+move_dict[move][1]]
                if map_coord[push_coord[1]][push_coord[0]] == ".":
                    if move == "<":
                        map_coord[push_coord[1]][push_coord[0]:next_coord[0]] = map_coord[push_coord[1]][push_coord[0]+1:next_coord[0]+1]
                    else:
                        breakpoint()
                        map_coord[push_coord[1]][next_coord[0]+1:push_coord[0]+1] = map_coord[push_coord[1]][next_coord[0]:push_coord[0]]
                    map_coord[next_coord[1]][next_coord[0]] = "@"
                    map_coord[robot[1]][robot[0]] = "."
                    robot = next_coord
            else:
                boxes_to_move = [next_coord]
                empty = False
                if move == "^":
                    if map_coord[next_coord[1]][next_coord[0]] == "[":
                        boxes_to_move.append([next_coord[0]+1, next_coord[1]])
                    else:
                        boxes_to_move.append([next_coord[0]-1, next_coord[1]])
                    while not any(map_coord[x[1]-1][x[0]] == "#" for x in boxes_to_move):
                        #print(boxes_to_move)
                        last_boxes = []
                        for next_box in [[x[0], x[1]-1] for x in boxes_to_move]:
                            if map_coord[next_box[1]][next_box[0]] != ".":
                                if map_coord[next_box[1]][next_box[0]] == "[":
                                    cont_box = [next_box[0]+1, next_box[1]]
                                else:
                                    cont_box = [next_box[0]-1, next_box[1]]
                                if next_box not in boxes_to_move:
                                    boxes_to_move.append(next_box)
                                    last_boxes.append(next_box)
                                if cont_box not in boxes_to_move:
                                    boxes_to_move.append(cont_box)
                                    last_boxes.append(next_box)
                        if all(map_coord[x[1]-1][x[0]] == "." for x in last_boxes):
                            empty = True
                            break
                    if empty:
                        breakpoint()
                        saved_boxes = [[x, map_coord[x[1]][x[0]]] for x in boxes_to_move]
                        for box_to_delete in boxes_to_move:
                            map_coord[box_to_delete[1]][box_to_delete[0]] = "."
                        for b in saved_boxes:
                            saved_box, symbol = b
                            map_coord[saved_box[1]-1][saved_box[0]] = symbol
                        next_robot = [robot[0], robot[1]-1]
                        map_coord[robot[1]][robot[0]] = "."
                        map_coord[next_robot[1]][next_robot[0]] = "@"
                        robot = next_robot
                    
        print(move)
        print(*map_coord, sep='\n')
    """total = 0
    for y, row in enumerate(map_coord):
        for x, col in enumerate(row):
            if col == "O":
                total += 100*y + x
    print(total)"""