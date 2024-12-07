with open("input.txt", "r") as f:
    total = 0
    for line in f.read().split("\n"):
        solution, operants = line.split(": ")
        solution = int(solution)
        operants = [int(x) for x in operants.split()]
        #print(solution, operants)
        sol = []
        for op in operants:
            if not sol:
                sol.append(op)
            else:
                new_sol = []
                for s in sol:
                    new_sol.append(s+op)
                    new_sol.append(s*op)
                    new_sol.append(int(str(s)+str(op)))
                sol = new_sol
        if solution in sol:
            total += solution
    print(total)
