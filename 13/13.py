import re
with open("input.txt", "r") as f:
    total_cost = 0
    for machine in f.read().split("\n\n"):
        a, b, cost = machine.split("\n")
        a = [int(re.search(r"X\+(\d+)", a).group(1)), int(re.search(r"Y\+(\d+)", a).group(1))]
        b = [int(re.search(r"X\+(\d+)", b).group(1)), int(re.search(r"Y\+(\d+)", b).group(1))]
        cost = [int(re.search(r"X\=(\d+)", cost).group(1)), int(re.search(r"Y\=(\d+)", cost).group(1))]
        matches = []
        for i in range(1, 101):
            if cost[0] > a[0]*i and (cost[0]-a[0]*i)%b[0] == 0:
                x = (cost[0]-a[0]*i)/b[0]
                if (a[1]*i+b[1]*x) == cost[1]:
                    matches.append([i, x, (i*3+x)])
        if matches:
            matches.sort(key=lambda x: x[2], reverse=True)
            total_cost += matches[0][2]
    print(int(total_cost))