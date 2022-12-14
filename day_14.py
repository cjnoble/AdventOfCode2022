from itertools import tee


def read_text_file (file_path):

    with open(file_path, "r") as f: # open file in read only mode
        data = f.readlines() # read in as a list
        data = [line.replace("\n","") for line in data] #remove new line charachters

    return data



def get_max (data):

    max_column = 0
    max_row = 0

    for row in data:
        blocks = row.split(" -> ")
        for block in blocks:
            x,y = prep_block(block)
            max_column = max(max_column, x)
            max_row = max(max_row, y)

    return max_row + 1, max_column + 1

def parse_data (data, max_rows, max_columns):

    grid = [["." for column in range(max_columns)] for row in range(max_rows)]

    for row in data:
        blocks = row.split(" -> ")
        for block_1, block_2 in pairwise(blocks):
            x1, y1 = prep_block(block_1)
            x2, y2 = prep_block(block_2)

            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2)+1):
                    grid[y][x1] = "#"
            elif y1 == y2:
                for x in range(min(x1, x2), max(x1, x2)+1):
                    grid[y1][x] = "#"


    return grid

def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def prep_block(block):
    x, y = block.split(",")
    x = int(x)
    y = int(y)
    return x, y


def part_1(grid, max_row, max_column):
    print(len(grid))
    print(len(grid[0]))

    sand = 0
    start_pos = (500, 0)

    while True:
        sand += 1
        pos = start_pos
        while True:

            if pos[1] == len(grid) - 1:
                return sand - 1

            if grid[pos[1] + 1][pos[0]] == ".":
                pos = (pos[0], pos[1] + 1)

            elif grid[pos[1] + 1][pos[0] - 1] == ".":
                pos = (pos[0] - 1, pos[1] + 1)

            elif grid[pos[1] + 1][pos[0] + 1] == ".":
                pos = (pos[0] + 1, pos[1] + 1)

            else:
                grid[pos[1]][pos[0]] = "o"
                if pos ==start_pos:
                    return sand
                break

            #print(pos)


def part_2(grid, max_row, max_column):

    max_row += 2

    grid.append(["." for column in range(max_column + 2)])
    grid.append(["#" for column in range(max_column + 2)])

    return part_1(grid, max_row, max_column)

if __name__ == "__main__":
    data = read_text_file("14.txt")
    max_row, max_column = get_max(data)
    print(max_row, max_column)
    grid = parse_data(data, max_row, max_column)
    print(part_1(grid, max_row, max_column))

    column_bunce = max_row*2
    max_column += column_bunce
    grid = parse_data(data, max_row, max_column)
    print(part_2(grid, max_row, max_column))