import json
from enum import Enum
from functools import cmp_to_key

def read_text_file (file_path):

    with open(file_path, "r") as f: # open file in read only mode
        data = f.readlines() # read in as a list
        data = [line.replace("\n","") for line in data] #remove new line charachters

    return data



def parse_data (data):
    data = [json.loads(line) for line in data if line != ""]
    return data


def iterate_pairs(a_itet):
    iterator = iter(a_itet)

    while True:
        try:
            yield(next(iterator), next(iterator))
        except StopIteration:
            break


class Match(Enum):
    Match = 1
    NoMatch = 2
    RunOut = 3


def check_pair(pair1, pair2):

    if isinstance(pair1, list) or isinstance(pair2, list):
        if not isinstance(pair1, list):
            pair1 = [pair1]
        elif not isinstance(pair2, list):
            pair2 = [pair2]

        if len(pair1) == 0:
            return Match.Match
        elif len(pair2) == 0:
            return Match.NoMatch


        for left, right in zip(pair1, pair2):
            c = check_pair(left, right)
            if c == Match.Match or c == Match.NoMatch:
                return c
            elif c == Match.RunOut:
                if len(pair1) < len(pair2):
                    return Match.Match
                elif len(pair1) > len(pair2):
                    return Match.NoMatch

    # for left, right in zip(pair1, pair2):
    #     if isinstance(left, list) or isinstance(right, list):
    #         if not isinstance(left, list):
    #             left = [left]
    #         elif not isinstance(right, list):
    #             right = [right]

    #         c = check_pair(left, right)
    #         if c == Match.Match or c == Match.NoMatch:
    #             return c
    #         elif c == Match.RunOut:
    #             if len(left) < len(right):
    #                 return Match.Match
    #             elif len(left) > len(right):
    #                 return Match.NoMatch

    else:
        if pair1 < pair2:
            return Match.Match
        elif pair1 > pair2:
            return Match.NoMatch

    return Match.RunOut

def part_1(data):

    correct_pairs = 0

    for index, (pair1, pair2) in enumerate(iterate_pairs(data)):
        match = check_pair(pair1, pair2)
        if match == Match.Match:
            correct_pairs += index + 1

    return correct_pairs


def check_pair_cmp(p1, p2):

    results = check_pair(p1, p2)
    if results == Match.Match:
        return -1
    else:
        return 1 

def part_2(data:list):

    m1 = [[2]]
    m2 = [[6]]

    data.extend([m1, m2])

    data.sort(key=cmp_to_key(check_pair_cmp))

    return (data.index(m1) + 1) * (data.index(m2) + 1)

if __name__ == "__main__":

    data = read_text_file("13.txt")
    data = parse_data(data)
    print(part_1(data))
    print(part_2(data))
