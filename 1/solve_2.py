with open("input.txt") as f:

    L1 = []
    L2 = []

    for line in f:
        L1.append(int(line.split()[0]))
        L2.append(int(line.split()[1]))

    sum = 0

    for i in L1:
        sum += i * L2.count(i)

    print(sum)