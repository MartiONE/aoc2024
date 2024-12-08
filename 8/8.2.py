from pprint import pp
from collections import defaultdict
from itertools import combinations
with open("input.txt", "r") as f:
    m = []
    char_dict = defaultdict(list)
    antinodes = []
    for y, line in enumerate(f.read().split("\n")):
        row = []
        for x, col in enumerate(line):
            if col != ".":
                char_dict[col] += [[x, y]]
            row.append(col)
        m.append(row)
    for antenna, locations in char_dict.items():
        if len(locations) > 1:
            for i in locations:
                if i not in antinodes:
                    antinodes.append(i)
            for i, j in combinations(locations, 2):
                distance = [j[0] - i[0], j[1] - i[1]]
                antenna_i = []
                antenna_j = []
                i = [i[0]-distance[0], i[1]-distance[1]]
                j = [j[0]+distance[0], j[1]+distance[1]]
                while i[0] >= 0 and i[0] < len(m) and i[1] >= 0 and i[1] < len(m):
                    if i not in antinodes:
                        antinodes.append(i)
                    if m[i[1]][i[0]] == ".":
                        m[i[1]][i[0]] = "#"
                    i = [i[0]-distance[0], i[1]-distance[1]]
                while j[0] >= 0 and j[0] < len(m) and j[1] >= 0 and j[1] < len(m):
                    if j not in antinodes:
                        antinodes.append(j)
                    if m[j[1]][j[0]] == ".":
                        m[j[1]][j[0]] = "#"
                    j = [j[0]+distance[0], j[1]+distance[1]]
    print(len(antinodes))