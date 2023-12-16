from collections import deque, defaultdict
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
            #print(name in data_dict.keys())
            data_dict[name]["size"] += size
            return name, size

        elif f:= re.match(r"(\d+) ([A-Za-z]+)", next_c):
            sub_name = f.groups(1)[0]
            sub_name = "\\".join([name,sub_name])
            if sub_name not in data_dict[name]["folders"]:
                data_dict[name]["folders"].add(sub_name)
                size += int(f.groups(0)[0])

        elif f:= re.match(r"\$ cd ([A-Za-z]+[.]*[A-Za-z]*)", next_c):
            sub_name, sub_size = folder_size(data, "\\".join([name,f.groups(0)[0]]), data_dict)
            #sub_name = "\\".join(name,sub_name)
            if sub_name not in data_dict[name]["folders"]:
                data_dict[name]["folders"].add(sub_name)
                size += sub_size

        elif f:= re.match(r"\$ ls", next_c):
            pass

        elif f:= re.match(r"dir ([A-Za-z]+)", next_c):
            pass

        else:
            print(next_c)
    
    data_dict[name]["size"] += size
    return name, size

def part_1(data):
    data_dict = defaultdict(lambda : {"size": 0, "folders":set()})

    print(folder_size(data, r"\.", data_dict))

    MAX_SIZE = 100000

    data_dict_max = {name: size["size"] for name, size in data_dict.items() if size["size"] <= MAX_SIZE}
    print(data_dict_max)

    total = reduce(lambda x,y:x+y, data_dict_max.values())
    print(total)
    return total


def part_2(data):
    data_dict = defaultdict(lambda : {"size": 0, "folders":set()})

    print(folder_size(data, r"\.", data_dict))

    TOTAL_SIZE = 70000000
    REQUIRED_SIZE = 30000000

    size_used = data_dict[r"\."]["size"]

    del_size = REQUIRED_SIZE - (TOTAL_SIZE - size_used)

    data_dict_req = {name: size["size"] for name, size in data_dict.items() if size["size"] >= del_size}
    print(data_dict_req)

    sorted_folders = sorted(list(data_dict_req.items()), key= lambda x: x[1])

    print(sorted_folders[0])

    return sorted_folders[0]

if __name__ == "__main__":
    part_1(read_text_file("7.txt"))
    part_2(read_text_file("7.txt"))