with open("input.txt", "r") as f:
    disk_map = f.read()
    blocks = []
    par = True
    count = 0
    for digit in disk_map:
        if par:
            for i in range(int(digit)):
                blocks.append(count)
            par = False
            count += 1
        else:
            for i in range(int(digit)):
                blocks.append(".")
            par = True
    start = 0
    finish = len(blocks)-1
    while start < finish:
        if blocks[start] == ".":
            while blocks[finish] == ".":
                finish -= 1
            blocks[start] = blocks[finish]
            blocks[finish] = "."
        start += 1
    checksum = 0
    for i, b in enumerate(blocks):
        if b != ".":
            checksum += int(b)*i
    print(checksum)
