from collections import defaultdict
good_rows = []
count = 0
with open("input.txt", "r") as f:
    rules, updates = f.read().split("\n\n")
    rule_dict = defaultdict(list)
    for rule in rules.split("\n"):
        rule_dict[rule.split("|")[0]] += rule.split("|")[1].split(",")
    print(rule_dict)
    for update in updates.split("\n"):
        for row in update.split("\n"):
            row = row.split(",")
            prev = [row[0]]
            good = True
            for i in row[1:]:
                if any([x in rule_dict[i] for x in prev]):
                    good = False
                    break
                prev.append(i)
            if not good:
                # print(row)
                good_rows.append(row)
    for row in good_rows:
        while True:
            altered = False
            for x in range(len(row)-1):
                # print(row[x], row[x+1])
                if row[x] in rule_dict[row[x+1]]:
                    cache = row[x]
                    row[x] = row[x+1]
                    row[x+1] = cache
                    altered = True
            if not altered:
                break
        count += int(row[len(row)//2])
    print(count)
