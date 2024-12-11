with open("input.txt", "r") as f:
    stones = [int(x) for x in f.read().split()]
    for _ in range(25):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone))%2 == 0:
                string = str(stone)
                new_stones += [int(string[:len(string)//2]), int(string[len(string)//2:])]
            else:
                new_stones.append(stone*2024)
        stones = new_stones
    print(len(stones))