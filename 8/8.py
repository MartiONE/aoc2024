from pprint import pp
from collections import defaultdict
from itertools import combinations
with open("input.txt", "r") as f:
    m = []
    count = 0
    char_dict = defaultdict(list)
    for y, line in enumerate(f.read().split("\n")):
        row = []
        for x, col in enumerate(line):
            if col != ".":
                char_dict[col] += [[x, y]]
            row.append(col)
        m.append(row)
    for antenna, locations in char_dict.items():
        if len(locations) > 1:
            for i, j in combinations(locations, 2):
                distance = [j[0] - i[0], j[1] - i[1]]
                antenna_i = [i[0]-distance[0], i[1]-distance[1]]
                antenna_j = [j[0]+distance[0], j[1]+distance[1]]
                if antenna_i[0] >= 0 and antenna_i[0] < len(m) and antenna_i[1] >= 0 and antenna_i[1] < len(m) and m[antenna_i[1]][antenna_i[0]] != "#":
                    count += 1
                    if m[antenna_i[1]][antenna_i[0]] == ".":
                        m[antenna_i[1]][antenna_i[0]] = "#"
                if antenna_j[0] < len(m) and antenna_j[0] >= 0 and antenna_j[1] < len(m) and antenna_j[1] >= 0 and m[antenna_j[1]][antenna_j[0]] != "#":
                    count += 1
                    if m[antenna_j[1]][antenna_j[0]] == ".":
                        m[antenna_j[1]][antenna_j[0]] = "#"
    print(count)