import re
from functools import reduce
from collections import deque, defaultdict

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

def part_2(data):

    drops = set(tuple(int(t) for t in row) for row in data) 

    max_search = max([max([row[i] for row in data]) for i in range(3)]) + 2
    min_search = min([min([row[i] for row in data]) for i in range(3)]) - 2

    already_searched = set()
    search = deque()
    search.append(tuple([min_search, min_search, min_search]))
    faces = 0

    while search:
        
        next = search.popleft()

        #print(next)

        if next in drops:
            faces += 1

        else:
            already_searched.add(next)
            new = [(next[0] + 1, next[1], next[2]), (next[0], next[1]+1, next[2]), (next[0], next[1], next[2] + 1), (next[0] - 1, next[1], next[2]), (next[0], next[1]-1, next[2]), (next[0], next[1], next[2] - 1)]
            new = [p for p in new if (p in drops or p not in search) and (p not in already_searched) and (max(p) < max_search) and (min(p) >= min_search)]

            search.extend(new)

    return faces


if __name__ == "__main__":

    data = read_text_file("18.txt")
    print(part_1(data))
    print(part_2(data))

