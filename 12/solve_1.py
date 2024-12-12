from collections import deque

def bfs(grid: list[list[str]], done_grid: list[list[int]], start: tuple[int, int], target: str) -> tuple[int, int]:
    queue = deque([start])
    area = 0
    perimeter = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()
        if done_grid[x][y] == 1:
            continue
        done_grid[x][y] = 1
        area += 1
        local_perimeter = 4

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if grid[nx][ny] == target:
                    if done_grid[nx][ny] == 0:
                        queue.append((nx, ny))
                    local_perimeter -= 1

        perimeter += local_perimeter

    return area, perimeter

def main(filename: str) -> None:
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file]

    done_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    total_price = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if done_grid[i][j] == 0:
                area, perimeter = bfs(grid, done_grid, (i, j), grid[i][j])
                total_price += area * perimeter
                # if area != 0:
                #     print(f'{grid[i][j]}: {area} {perimeter}')
    print(total_price)

main('input.txt')