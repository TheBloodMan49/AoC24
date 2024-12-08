import multiprocessing

def test_map(map: [str], guard_pos: tuple) -> bool:
    guard_direction = 0  # 0 = up, 1 = right, 2 = down, 3 = left
    Xs_in_a_row = 0
    while True:
        x, y = guard_pos

        if map[x][y] == 'X':
            Xs_in_a_row += 1
        else:
            Xs_in_a_row = 0

        if Xs_in_a_row == 1000:
            return True

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
            return False

def process_position(args):
    i, j, map, guard_pos = args
    if map[i][j] == '.':  # Find a spot to place an obstruction
        temp_map = map.copy()
        temp_map[i] = temp_map[i][:j] + '#' + temp_map[i][j + 1:]
        if test_map(temp_map, guard_pos):
            return 1
    return 0

def main(input: str) -> None:
    with open(input) as f:
        map = f.readlines()
        map = [line.strip() for line in map]

        guard_pos = (0, 0)
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == '^':
                    guard_pos = (i, j)

        positions_possible = 0

        # Parallelize this loop
        with multiprocessing.Pool() as pool:
            results = pool.map(process_position, [(i, j, map, guard_pos) for i in range(len(map)) for j in range(len(map[i]))])
            positions_possible = sum(results)

        print(positions_possible)

main('input.txt')