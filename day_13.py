import json
from enum import Enum

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

    for left, right in zip(pair1, pair2):
        if isinstance(left, list) or isinstance(right, list):
            if not isinstance(left, list):
                left = [left]
            elif not isinstance(right, list):
                right = [right]

            c = check_pair(left, right)
            if c.RunOut and len(left) < len(right):
                return Match.Match

        else:
            if left < right:
                return Match.Match

    return Match.NoMatch

def part_1(data):

    correct_pairs = 0

    for index, (pair1, pair2) in enumerate(iterate_pairs(data)):
        match = check_pair(pair1, pair2)
        if match == Match.Match:
            correct_pairs += index + 1

    return correct_pairs
        

if __name__ == "__main__":

    data = read_text_file("13.txt")
    data = parse_data(data)
    print(part_1(data))
