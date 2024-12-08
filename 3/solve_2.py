import re

with open("input.txt") as f:
    total_sum = 0
    enabled = True

    reg_do = re.compile(r"do\(\)")
    reg_dont = re.compile(r"don't\(\)")
    reg_mul = re.compile(r"mul\((\d+),(\d+)\)")

    for line in f:
        pos = 0
        while pos < len(line):
            match_do = reg_do.search(line, pos)
            match_dont = reg_dont.search(line, pos)
            match_mul = reg_mul.search(line, pos)

            if match_mul and (not match_do or match_mul.start() < match_do.start()) and (not match_dont or match_mul.start() < match_dont.start()):
                if enabled:
                    total_sum += int(match_mul.group(1)) * int(match_mul.group(2))
                pos = match_mul.end()
            elif match_do and (not match_dont or match_do.start() < match_dont.start()):
                enabled = True
                pos = match_do.end()
            elif match_dont and (not match_do or match_dont.start() < match_do.start()):
                enabled = False
                pos = match_dont.end()

            else:
                break

    print(total_sum)