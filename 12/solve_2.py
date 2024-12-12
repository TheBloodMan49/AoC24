from collections import deque

def flood_fill(grid: list[list[str]], done_grid: list[list[int]], start: tuple[int, int], target: str) -> tuple[int, int, int]:
    queue = deque([start])
    area = 0
    horizontal_fences = set()
    vertical_fences = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()
        if done_grid[x][y] == 1:
            continue
        done_grid[x][y] = 1
        area += 1

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if grid[nx][ny] == target:
                    if done_grid[nx][ny] == 0:
                        queue.append((nx, ny))
                else:
                    if dx == 0:
                        horizontal_fences.add((x, y, y + dy))
                    else:
                        vertical_fences.add((x, y, x + dx))
            else:
                if dx == 0:
                    horizontal_fences.add((x, y, y + dy))
                else:
                    vertical_fences.add((x, y, x + dx))

    return area, len(sift_horizontal_fences(horizontal_fences)), len(sift_vertical_fences(vertical_fences))

def sift_vertical_fences(vertical_fences: set[tuple[int, int, int]]) -> set[tuple[int, int, int]]:
    new_vertical_fences = set()
    for x, y1, y2 in vertical_fences:
        if y1 > y2:
            y1, y2 = y2, y1
        new_vertical_fences.add((x, y1, y2))
    return new_vertical_fences

def sift_horizontal_fences(horizontal_fences: set[tuple[int, int, int]]) -> set[tuple[int, int, int]]:
    new_horizontal_fences = set()
    for x1, y, x2 in horizontal_fences:
        if x1 > x2:
            x1, x2 = x2, x1
        new_horizontal_fences.add((x1, y, x2))
    return new_horizontal_fences

def main(filename: str) -> None:
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file]

    done_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    total_price = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if done_grid[i][j] == 0:
                area, horizontal_fences, vertical_fences = flood_fill(grid, done_grid, (i, j), grid[i][j])
                total_price += area * (horizontal_fences + vertical_fences)

    print(total_price)

main('input_test.txt')