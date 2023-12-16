import re
from functools import reduce
from collections import defaultdict

def read_text_file (file_path):

    with open(file_path, "r") as f: # open file in read only mode
        data = f.readlines() # read in as a list
        data = [line.replace("\n","") for line in data] #remove new line charachters

        data = [[int(i) for i in line.split(",")] for line in data]

    return data



def drop_test(drops):
    for key in drops.keys():
        
        test_list = [-1, 0, 1]

        for i in test_list:
            for j in test_list:
                for k in test_list:
                    if abs(i) + abs(j) + abs(k) == 1:
                        t = (key[0]+i, key[1]+j, key[2]+k)
                        if t in drops.keys():
                            drops[key] -= 1

    return sum(drops.values())

def part_1(data):

    drops = dict()

    for row in data:
        drops[tuple(t for t in row)] = 6

    return drop_test(drops)


def part_2(data):

    drops = dict()

    for row in data:
        drops[tuple(t for t in row)] = 6

    x_max = max([d[0] for d in drops.keys()])
    y_max = max([d[1] for d in drops.keys()])
    z_max = max([d[2] for d in drops.keys()])


    print(x_max, y_max, z_max)

    blocked = defaultdict(int)

    # Scan all rows
    in_flag = False
    for j in range (y_max+2):
        for k in range (z_max+2):
            for i in range (x_max+2):
                if (i,j,k) in drops.keys():
                    in_flag = not in_flag
                    if in_flag:
                        blocked_by = (i,j,k)

                elif in_flag:
                    blocked[(i,j,k)] += 1

    # Scan all columns
    in_flag = False
    for k in range (z_max+2):
        for i in range (x_max+2):
            for j in range (y_max+2):
                if (i,j,k) in drops.keys():
                    in_flag = not in_flag
                    if in_flag:
                        blocked_by = (i,j,k)

                elif in_flag:
                    blocked[(i,j,k)] += 1
    
    # scan last direction
    in_flag = False
    for i in range (x_max+2):
        for j in range (y_max+2):
            for k in range (z_max+2):
                if (i,j,k) in drops.keys():
                    in_flag = not in_flag
                    if in_flag:
                        blocked_by = (i,j,k)

                elif in_flag:
                    blocked[(i,j,k)] += 1

                
                if blocked[(i,j,k)] == 3:
                    drops[(i,j,k)] = 6

    return drop_test(drops)

if __name__ == "__main__":

    data = read_text_file("18.txt")
    #print(data)
    print(part_1(data))

    print(part_2(data))

