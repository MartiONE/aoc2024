
from collections import Counter

def blink(stones: Counter) -> Counter:
    """Transform stone counts according to the rules."""
    new_stones = Counter()

    for stone, count in stones.items():
        # Rule 1: If stone is 0, replace with 1
        if stone == 0:
            new_stones[1] += count
        # Rule 2: If number has even number of digits, split in half
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            half = len(s) // 2
            left = int(s[:half])
            right = int(s[half:])
            new_stones[left] += count
            new_stones[right] += count
        # Rule 3: Multiply by 2024
        else:
            new_stones[stone * 2024] += count

    return new_stones

with open("input.txt", "r") as f:
    stones = [int(x) for x in f.read().split()]
    stones = Counter(stones)
    for _ in range(75):
        stones = blink(stones)
    print(sum(stones.values()))