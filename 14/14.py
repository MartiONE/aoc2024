import re
from pprint import pp
def sum_quadrant(quadrant):
    sum = 0
    for row in quadrant:
        for col in row:
            if col != ".":
                sum += col
    return sum
with open("input.txt", "r") as f:
    robots = []
    limit_x = 101
    limit_y = 103
    for line in f.read().split("\n"):
        px = int(re.search(r"p=(\d+),(\d+)", line).group(1))
        py = int(re.search(r"p=(\d+),(\d+)", line).group(2))
        vx = int(re.search(r"v=([\d-]+),([\d-]+)", line).group(1))
        vy = int(re.search(r"v=([\d-]+),([\d-]+)", line).group(2))
        robots.append([[px, py],[vx, vy]])
    for step in range(100):
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
        #pp(m)
    h = len(m)
    w = len(m[1])
    top_left =  [m[i][:w // 2] for i in range(h // 2)]
    top_right = [m[i][(w // 2)+1:] for i in range(h // 2)]
    bot_left =  [m[i][:w // 2] for i in range(h // 2, h)][1:]
    bot_right = [m[i][(w // 2)+1:] for i in range(h // 2, h)][1:]
    #print(bot_left, top_left)
    #print(bot_right, top_right)
    print(sum_quadrant(top_left)*sum_quadrant(top_right)*sum_quadrant(bot_left)*sum_quadrant(bot_right))