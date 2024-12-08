with open("input.txt") as f:
    matrix = [line.strip() for line in f]

    rows = len(matrix)
    cols = len(matrix[0])
    count = 0

    for x in range(rows):
        for y in range(cols):
            if y + 4 <= cols and matrix[x][y:y+4] == "XMAS":
                count += 1

            if y - 4 >= -1 and matrix[x][y-4+1:y+1][::-1] == "XMAS":
                count += 1

            if x + 4 <= rows and ''.join(matrix[x+i][y] for i in range(4)) == "XMAS":
                count += 1

            if x - 4 >= -1 and ''.join(matrix[x-i][y] for i in range(4)) == "XMAS":
                count += 1

            if x + 4 <= rows and y + 4 <= cols and ''.join(matrix[x+i][y+i] for i in range(4)) == "XMAS":
                count += 1

            if x + 4 <= rows and y - 4 >= -1 and ''.join(matrix[x+i][y-i] for i in range(4)) == "XMAS":
                count += 1

            if x - 4 >= -1 and y + 4 <= cols and ''.join(matrix[x-i][y+i] for i in range(4)) == "XMAS":
                count += 1

            if x - 4 >= -1 and y - 4 >= -1 and ''.join(matrix[x-i][y-i] for i in range(4)) == "XMAS":
                count += 1

    print(count)