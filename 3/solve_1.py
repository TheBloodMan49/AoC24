import re

with open("input.txt") as f:
    sum = 0

    reg = re.compile(r"mul\((\d+),(\d+)\)")

    for line in f:
        for match in reg.finditer(line):
            sum += int(match.group(1)) * int(match.group(2))

    print(sum)