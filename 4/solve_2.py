with open("input.txt") as f:
    matrix = [line.strip() for line in f]

    rows = len(matrix)
    cols = len(matrix[0])
    count = 0

    for x in range(rows):
        for y in range(cols):
            if matrix[x][y] == 'A' and x + 1 < rows and y + 1 < cols and x > 0 and y > 0:

                if matrix[x-1][y-1] == 'M' and matrix[x-1][y+1] == 'M' and matrix[x+1][y-1] == 'S' and matrix[x+1][y+1] == 'S':
                    count += 1

                if matrix[x-1][y-1] == 'M' and matrix[x-1][y+1] == 'S' and matrix[x+1][y-1] == 'M' and matrix[x+1][y+1] == 'S':
                    count += 1

                if matrix[x-1][y-1] == 'S' and matrix[x-1][y+1] == 'M' and matrix[x+1][y-1] == 'S' and matrix[x+1][y+1] == 'M':
                    count += 1

                if matrix[x-1][y-1] == 'S' and matrix[x-1][y+1] == 'S' and matrix[x+1][y-1] == 'M' and matrix[x+1][y+1] == 'M':
                    count += 1

    print(count)