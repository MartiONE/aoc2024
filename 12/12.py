from collections import defaultdict
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
with open("example.txt", "r") as f:
    m = defaultdict(list)
    ma = []
    count = 0
    groups = []
    for y, row in enumerate(f.read().split("\n")):
        r = []
        for x, col in enumerate(row):
            m[col] += [(y, x)]
            r.append(col)
        ma.append(r)
    print(ma)
    for l, points in m.items():
        area = 0
        perimeter = 0
        for p in points:
            area += 1
            for n in directions:
                neighbour = [p[0]+n[0], p[1]+n[1]]
                
                if neighbour[0] >= 0 and neighbour[1] >= 0 and neighbour[0] < len(ma[0]) and neighbour[1] < len(ma):
                    if ma[neighbour[0]][neighbour[1]] != l:
                        perimeter += 1
                else:
                    perimeter += 1
        print(area, perimeter)
        count += area*perimeter
print(count)