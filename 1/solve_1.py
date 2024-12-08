with open("input.txt") as f:

    L1 = []
    L2 = []

    for line in f:
        L1.append(int(line.split()[0]))
        L2.append(int(line.split()[1]))

    L1.sort()
    L2.sort()

    sum = 0

    for i in range(len(L1)):
        sum += abs(L1[i] - L2[i])

    print(sum)