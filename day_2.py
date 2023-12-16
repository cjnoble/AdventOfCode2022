from enum import Enum

class Result(Enum):
    WIN = 1
    DRAW = 2
    LOOSE = 3



WIN_SCORE = 6
DRAW_SCORE = 3
LOOSE_SCORE = 0

def read_text_file (file_path):

    with open(file_path, "r") as f:
        data = f.readlines()
        data = [line.replace("\n","") for line in data]

    return data


def calc(data):

    base_score = {"X": 1, "Y": 2, "Z": 3}

    win_combos = {"A": "Y", "B": "Z", "C": "X"}
    draw_combos = {"A": "X", "B": "Y", "C": "Z"}
    loose_combos = {"A": "Z", "B": "X", "C": "Y"}

    score = 0

    for row in data:
        opponents_throw = row[0]
        your_throw = row[1]
        score += base_score[your_throw]

        if win_combos[opponents_throw] == your_throw:
            score += WIN_SCORE
        elif draw_combos[opponents_throw] == your_throw:
            score += DRAW_SCORE

    print(score)

def calc_2(data):

    base_score = {"A": 1, "B": 2, "C": 3}

    win_combos = {"A": "B", "B": "C", "C": "A"}
    draw_combos = {"A": "A", "B": "B", "C": "C"}
    loose_combos = {"A": "C", "B": "A", "C": "B"}

    score = 0

    for row in data:
        
        if row[1] == "Z":
            # You need to win
            res = win_combos[row[0]]
            score += WIN_SCORE
        elif row[1] == "Y":
            # You need to draw
            score += DRAW_SCORE
            res = draw_combos[row[0]]
        else:
            # You need to loose
            res = loose_combos[row[0]]
        
        score += base_score[res]

    print(score)

data = read_text_file("2.txt")
data = [row.split(" ") for row in data]


calc_2(data)

test_data = [["A", "Y"], ["B", "X"], ["C", "Z"]]

calc_2(test_data)