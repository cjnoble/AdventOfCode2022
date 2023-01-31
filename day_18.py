import re
from functools import reduce


def read_text_file (file_path):

    with open(file_path, "r") as f: # open file in read only mode
        data = f.readlines() # read in as a list
        data = [line.replace("\n","") for line in data] #remove new line charachters

        data = [[int(i) for i in line.split(",")] for line in data]

    return data


def part_1(data):

    drops = dict()

    for row in data:
        drops[tuple(t for t in row)] = 6

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

if __name__ == "__main__":

    data = read_text_file("18.txt")
    #print(data)
    print(part_1(data))

