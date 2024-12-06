directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
with open("input.txt", "r") as f:
    map = []
    w_map = []
    for i, line in enumerate(f.read().split("\n")):
        if '^' in line:
            guard = [i, line.index("^")]
        map.append([x for x in line])
        w_map.append([x for x in line])
    direction = [-1, 0]
    w_map[guard[0]][guard[1]] = "X"

    while True:
        next_step = [guard[0] + direction[0], guard[1] + direction[1]]
        if next_step[0] >= 0 and next_step[0] < len(map) and next_step[1] >= 0 and next_step[1] < len(map[0]):
            if map[next_step[0]][next_step[1]] != ".":
                direction = directions[(directions.index(direction) + 1) % len(directions)]
            elif map[next_step[0]][next_step[1]] == ".":
                map[guard[0]][guard[1]] = "."
                guard = next_step
                map[next_step[0]][next_step[1]] = "^"
                w_map[next_step[0]][next_step[1]] = "X"
        else:
            print(sum([sum([1 if y == "X" else 0 for y in x]) for x in w_map]))
            break

