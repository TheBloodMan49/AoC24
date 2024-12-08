def main(input: str) -> None:
    with open(input) as f:
        map = f.readlines()
        map = [line.strip() for line in map]

        guard_pos = (0, 0)
        guard_direction = 0  # 0 = up, 1 = right, 2 = down, 3 = left
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == '^':
                    guard_pos = (i, j)

        running = True
        while running:

            x, y = guard_pos

            map[x] = map[x][:y] + 'X' + map[x][y + 1:]

            if guard_direction == 0:
                if x == 0 or map[x - 1][y] != '#':
                    x -= 1
                else:
                    guard_direction = 1
            elif guard_direction == 1:
                if y == len(map[0]) - 1 or map[x][y + 1] != '#':
                    y += 1
                else:
                    guard_direction = 2
            elif guard_direction == 2:
                if x == len(map) - 1 or map[x + 1][y] != '#':
                    x += 1
                else:
                    guard_direction = 3
            elif guard_direction == 3:
                if y == 0 or map[x][y - 1] != '#':
                    y -= 1
                else:
                    guard_direction = 0

            guard_pos = (x, y)

            # Check if the guard has reached the end of the map
            if x == -1 or x == len(map) or y == -1 or y == len(map[0]):
                running = False

        unique_steps = 0
        for line in map:
            print(line)
            unique_steps += line.count('X')

        print(unique_steps)

main('input.txt')