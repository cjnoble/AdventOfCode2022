import re
from itertools import tee

def read_text_file (file_path):

    with open(file_path, "r") as f: # open file in read only mode
        data = f.readlines() # read in as a list
        data = [line.replace("\n","") for line in data] #remove new line charachters

    return data

def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

class Head (object):
    def __init__(self, x=0, y=0, n=None):
        self.x = x
        self.y = y
        self.n = n

    def set_tail(self, tail):
        self.tail = tail

    def move(self, dir, n):

        for i in range (n):
            if dir == "L":
                self.x -= 1
            elif dir == "R":
                self.x += 1
            elif dir == "U":
                self.y += 1
            elif dir == "D":
                self.y -= 1

            self.tail.update()

    def update(self, x, y):
        self.x = x
        self.y = y
        self.tail.update()

class Tail (object):
    def __init__(self,head, x=0, y=0, next_head=None, n=None):
        self.x = x
        self.y = y
        self.head = head
        self.head.set_tail(self)
        self.pos_visited = set()
        self.updated_pos_visited()
        self.next_head = next_head
        self.n = n

    def touching (self):
        return abs(self.x - self.head.x) < 2 and abs(self.y - self.head.y) < 2

    def update(self):
        if not self.touching():
            self.x += clamp(self.head.x - self.x, 1, -1)
            self.y += clamp(self.head.y - self.y, 1, -1)
            self.updated_pos_visited()

            if self.next_head:
                self.next_head.update(self.x, self.y)

    def updated_pos_visited(self):
        self.pos_visited.add((self.x, self.y))

    def current_pos (self, grid):
        grid[self.y][self.x] = str(self.n) if self.n else "#"

    def __repr__(self):
        r = [["*" for i in range(20)] for j in range (20)]
        for pos in self.pos_visited:
            r[pos[1]][pos[0]] = "#"

        r = "\n ".join(["".join(line) for line in r])

        return r

    def __str__(self):
        return self.__repr__()

def clamp (x, min_x, max_x):

    return min(max(x, max_x), min_x)

def part_1(moves):

    head = Head()
    tail = Tail(head)

    for move in moves:

        move = re.match(r"([LRUD]) (\d+)", move)
        direction = move.group(1)
        i = int(move.group(2))
        head.move(direction, i)

    print(tail.pos_visited)
    #print(tail)

    return len(tail.pos_visited)

def part_2(moves, N):
    heads = [Head(n=i) for i in range (N)]
    heads.append(None)
    for head_1, head_2 in pairwise(heads):
        tail = Tail(head_1, n=head_1.n+1)
        head_1.set_tail(tail)
        tail.next_head = head_2

    for move in moves:
        move = re.match(r"([LRUD]) (\d+)", move)
        direction = move.group(1)
        i = int(move.group(2))
        heads[0].move(direction, i)

    return len(heads[-2].tail.pos_visited)

def create_gird(n):
    r = [["*" for i in range(n)] for j in range (n)]
    return r

if __name__ == "__main__":

    moves = read_text_file("9.txt")
    print(part_1(moves))
    print(part_2(moves, 9))