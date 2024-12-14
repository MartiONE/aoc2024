import re
import matplotlib.pyplot as plt
import numpy as np
def sum_quadrant(quadrant):
    sum = 0
    for row in quadrant:
        for col in row:
            if col != ".":
                sum += col
    return sum
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
with open("input.txt", "r") as f:
    robots = []
    limit_x = 101
    limit_y = 103
    max_neighbours = 0
    for line in f.read().split("\n"):
        px = int(re.search(r"p=(\d+),(\d+)", line).group(1))
        py = int(re.search(r"p=(\d+),(\d+)", line).group(2))
        vx = int(re.search(r"v=([\d-]+),([\d-]+)", line).group(1))
        vy = int(re.search(r"v=([\d-]+),([\d-]+)", line).group(2))
        robots.append([[px, py],[vx, vy]])
    for step in range(1, 10000):
        neighbours = 0
        m = [["." for _ in range(limit_x)] for __ in range(limit_y)]
        for i, robot in enumerate(robots):
            robot_pos = robot[0]
            robot_vel = robot[1]
            next_pos = [
                ((robot_pos[0]+robot_vel[0])%limit_x) if robot_pos[0]+robot_vel[0]>=0 else limit_x+(robot_pos[0]+robot_vel[0]),
                ((robot_pos[1]+robot_vel[1])%limit_y) if robot_pos[1]+robot_vel[1]>=0 else limit_y+(robot_pos[1]+robot_vel[1])
                        ]
            # print(f"Robot pos: {robot_pos} with velocity {robot_vel} now becomes {next_pos}")
            
            if m[next_pos[1]][next_pos[0]] != ".":
                m[next_pos[1]][next_pos[0]] = m[next_pos[1]][next_pos[0]]+1
            else:
                m[next_pos[1]][next_pos[0]] = 1
                
            robots[i][0] = next_pos
        robots_positions = [x[0] for x in robots]
        for position in robots_positions:
            for direction in directions:
                new_pos = [position[0]+direction[0], position[1]+direction[1]]
                if new_pos in robots_positions:
                    neighbours += 1
        if neighbours > max_neighbours:
            max_neighbours = neighbours
            x = [i[0][0] for i in robots]
            y = [i[0][1] for i in robots]
            plt.scatter(x,y)
            plt.savefig('foo.png')
            plt.clf()
            print(step)
            breakpoint()
