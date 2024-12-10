from collections import defaultdict
with open("input.txt", "r") as f:
    m = []
    trailheads = []
    for i, row in enumerate(f.read().split("\n")):
        r = []
        for j, col in enumerate(row):
            r.append(int(col)) if col.isdigit() else r.append(-1)
            if col == "0":
                trailheads.append([[i, j], [i, j]])  
        m.append(r)
    score = 0
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    found_trailheads = defaultdict(list)
    while trailheads:
        trail, origin = trailheads.pop()
        for direction in directions:
            next_location = [direction[0] + trail[0], direction[1] + trail[1]]
            if next_location[0] >= 0 and next_location[1] >= 0 and next_location[0] < len(m) and next_location[1] < len(m[0]):
                previous_number = m[trail[0]][trail[1]]
                next_number = m[next_location[0]][next_location[1]]
                if next_number == 9 and previous_number == 8:
                    if next_location not in found_trailheads[str(origin)]:
                        found_trailheads[str(origin)] += [next_location]
                elif next_number == previous_number+1:
                    trailheads.append([next_location, origin])
    print(sum(len(x) for x in found_trailheads.values()))