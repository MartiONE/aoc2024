import re
with open("input.txt", "r") as f:
    total_cost = 0
    for machine in f.read().split("\n\n"):
        a, b, cost = machine.split("\n")
        a = [int(re.search(r"X\+(\d+)", a).group(1)), int(re.search(r"Y\+(\d+)", a).group(1))]
        b = [int(re.search(r"X\+(\d+)", b).group(1)), int(re.search(r"Y\+(\d+)", b).group(1))]
        cost = [int(re.search(r"X\=(\d+)", cost).group(1))+10000000000000, int(re.search(r"Y\=(\d+)", cost).group(1))+10000000000000]
        matches = []

        ax, ay = a
        bx, by = b
        px, py = cost
        W = ax * by - bx * ay
        Wi = px * by - py * bx
        Wj = py * ax - px * ay

        if W != 0:
            fi = int(Wi / W)
            fj = int(Wj / W)
        for i in range(fi-10, fi+10):
            for j in range(fj-10, fj+10):
                x = i * ax + j * bx
                y = i * ay + j * by
                if x == px and y == py:
                    tokens = i * 3 + j * 1
                    total_cost += tokens
    print(int(total_cost))