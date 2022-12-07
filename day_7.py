from collections import deque
from functools import reduce
import re

def read_text_file (file_path):

    with open(file_path, "r") as f:
        data = f.readlines()
        data = deque(line.replace("\n","") for line in data)

    return data

def folder_size (data: deque, name: str, data_dict: dict):

    size = 0

    while data:

        next_c = data.popleft()

        if next_c == "$ cd ..":
            data_dict[name] = size
            return name, size

        elif f:= re.match("(\d+) [A-Za-z]+", next_c):
            size += int(f.groups(0)[0])

        elif f:= re.match("\$ cd ([A-Za-z]+[.]*[A-Za-z]*)", next_c):
            sub_name, sub_size = folder_size(data, f.groups(0)[0], data_dict)
            size += sub_size

        elif f:= re.match("\$ ls", next_c):
            pass

        elif f:= re.match("dir ([A-Za-z]+)", next_c):
            pass

        else:
            print(next_c)
    
    data_dict[name] = size
    return name, size

def part_1(data):
    data_dict = {}

    print(folder_size(data, "\.", data_dict))

    MAX_SIZE = 100000

    data_dict_max = {name: size for name, size in data_dict.items() if size <= MAX_SIZE}
    print(data_dict_max)

    total = reduce(lambda x,y:x+y, data_dict_max.values())
    print(total)
    return total

if __name__ == "__main__":
    data = read_text_file("7.txt")
    part_1(data)
