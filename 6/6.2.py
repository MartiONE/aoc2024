from pprint import pprint
from copy import deepcopy
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def solve_map(start, directions, map):
    guard = start
    visited_nodes = []
    direction = [-1, 0]
    while True:
        visited_nodes.append([guard, direction])
        next_step = [guard[0] + direction[0], guard[1] + direction[1]]
        if next_step[0] >= 0 and next_step[0] < len(map) and next_step[1] >= 0 and next_step[1] < len(map[0]):
            if map[next_step[0]][next_step[1]] != ".":
                direction = directions[(directions.index(direction) + 1) % len(directions)]
            elif map[next_step[0]][next_step[1]] == ".":
                if [next_step, direction] in visited_nodes:
                    return False
                map[guard[0]][guard[1]] = "."
                guard = next_step
                map[next_step[0]][next_step[1]] = "^"
        else:
            return True

with open("input.txt", "r") as f:
    map = []
    w_map = []
    original_map = []
    count = 0
    for i, line in enumerate(f.read().split("\n")):
        if '^' in line:
            guard = [i, line.index("^")]
            initial_pos = guard
        map.append([x for x in line])
        w_map.append([x for x in line])
        original_map.append([x for x in line])
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
            break
    for y, row in enumerate(w_map):
        for x, col in enumerate(row):
            if col == "X" and [x,y] != initial_pos:
                gen_map = deepcopy(original_map)
                gen_map[y][x] = "#"
                result = solve_map(initial_pos, directions, gen_map)
                #breakpoint()
                if not result:
                    count += 1
    print(count)

