def read_text_file (file_path):

    with open(file_path, "r") as f: # open file in read only mode
        data = f.readlines() # read in as a list
        data = [line.replace("\n","") for line in data] #remove new line charachters

    return data

def possible_moves (data, x, y, current_h):

    possible = []

    # if y > 39:
    #     print(y)

    if x != 0:
        check_possible(data, x-1, y, current_h, possible)

    if x != len(data[y]) - 1:
        check_possible(data, x+1, y, current_h, possible)

    if y != 0:
        check_possible(data, x, y-1, current_h, possible)

    if y != len(data) - 1:
        check_possible(data, x, y+1, current_h, possible)

    return possible

def height(c):

    if c == "S":
        return ord("a")

    elif c == "E":
        return ord("z")

    else:
        return ord(c)


def check_possible(data, x, y, current_h, possible):
    try:
        h = height(data[y][x])
    except IndexError as e:
        print(x, y)
        raise e
    
    if h  <= current_h + 1:
        possible.append((x, y, h))


def xy_iterate (data):
    for y, row in enumerate(data):
        for x, i in enumerate(row):
            yield x,y,i         


def fewest_steps(data, x_start, y_start, fewest_step_dict):
    print(x_start, y_start)
    for x_end, y_end, i in xy_iterate(data):            
        if i=="E":
            break

    start_h = height(data[y_start][x_start])
    visited = set((x_start, y_start, start_h))
    next_moves = [(x_start, y_start, start_h)]
    steps = 0

    end = (x_end, y_end, height("E"))

    while next_moves:
        
        moves = []
        for move in next_moves:
            if move in fewest_step_dict.keys():
                if fewest_step_dict[move] <= steps:
                    continue
            fewest_step_dict[move] = steps 

            if move == end:
                break

            moves.extend(possible_moves (data, *move))

        next_moves  = []

        for move in moves:
            if move not in visited:
                visited.add(move)
                next_moves.append(move)

        steps += 1
        #print(steps)

    return steps


def part_1(data):
    for x_start, y_start, i in xy_iterate(data):            
        if i=="S":
            break

    fewest_step_dict = {}
    fewest_steps(data, *(x_start, y_start), fewest_step_dict)

    for x_end, y_end, i in xy_iterate(data):            
        if i=="E":
            break
    end_move = (x_end, y_end, height(data[y_end][x_end]))
    return fewest_step_dict[end_move]

def part_2(data):

    start_points = []

    for x, y, h in xy_iterate (data):
        if height(h) == ord("a"):
            start_points.append((x, y))

    fewest_step_dict = {}

    for start in start_points:
        fewest_steps(data, *start, fewest_step_dict)

    #steps = [fewest_steps(data, *start, fewest_step_dict) for start in start_points]

    for x_end, y_end, i in xy_iterate(data):            
        if i=="E":
            break
    end_move = (x_end, y_end, height(data[y_end][x_end]))

    return fewest_step_dict[end_move]

if __name__ == "__main__":
    data = read_text_file ("12.txt")

    print(part_1(data))
    print(part_2(data))

