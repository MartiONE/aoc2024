with open("input.txt", "r") as f:
    disk_map = f.read()
    blocks = []
    par = True
    count = 0
    empty = {}
    full = {}
    checksum = 0
    for digit in disk_map:
        if par:
            full[len(blocks)] = {"size": int(digit), "stop": len(blocks)+int(digit), "digit": count}
            for i in range(int(digit)):
                blocks.append(count)
            par = False
            count += 1
        else:
            empty[len(blocks)] = {"size": int(digit), "stop": len(blocks)+int(digit)}
            for i in range(int(digit)):
                blocks.append(".")
            par = True
    start = 0
    finish = len(blocks)-1
    for f_start, f in list(full.items())[::-1]:
        for e_start, e in dict(sorted(empty.items())).items():
            if e["size"] >= f["size"] and e_start < f_start:
                blocks[e_start:e_start+f["size"]] = blocks[f_start:f["stop"]]
                empty[e_start]["size"] -= f["size"]
                empty[e_start+f["size"]] = empty[e_start]
                del empty[e_start]
                blocks[f_start:f["stop"]] = ["." for x in  range(f["size"])]
                break
    for i, b in enumerate(blocks):
        if b != ".":
            checksum += int(b)*i
    print(checksum)