""" [N]     [Q]         [N]            
[R]     [F] [Q]     [G] [M]        
[J]     [Z] [T]     [R] [H] [J]    
[T] [H] [G] [R]     [B] [N] [T]    
[Z] [J] [J] [G] [F] [Z] [S] [M]    
[B] [N] [N] [N] [Q] [W] [L] [Q] [S]
[D] [S] [R] [V] [T] [C] [C] [N] [G]
[F] [R] [C] [F] [L] [Q] [F] [D] [P]
 1   2   3   4   5   6   7   8   9 
 """

from collections import deque
import re

class Stack(object):

    def __init__ (self, init_data=None):
        self.data = deque()
        self.size = 0
        if init_data:
            for i in init_data:
                self.push(i)

    def empty(self):
        if self.size == 0:
            return True
        return False

    def size(self):
        return self.size

    def top(self):
        A = self.pop()
        self.push(A)
        return A

    def push(self, A):
        self.data.append(A)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.data.pop()

    def __repr__ (self):
        tempstack = Stack()
        s = ""
        n = self.size
        for i in range(n):
            A = self.pop()
            s += A
            tempstack.push(A)

        for i in range(n):
            A = tempstack.pop()
            self.push(A)
        
        return s

    def __str__ (self):
        return self.__repr__()

    @staticmethod
    def static_test():
        pass

def read_text_file (file_path):

    with open(file_path, "r") as f:
        data = f.readlines()
        data = [line.replace("\n","") for line in data]

    return data


class Crane (object):
    def __init__(self):

        stacks = ["FDBZTJRN", "RSNJH", "CRNJGZFQ", "FVNGRTQ", "LTQF", "QCWZBRGN", "FCLSNHM", "DNQMTJ", "PGS"]

        self.stacks = [Stack(s) for s in stacks]

    def parse_instruction(self, instruction):

        match = re.findall(("\d+"), instruction)

        n = int(match[0])
        m_from = int(match[1]) - 1
        m_to = int(match[2]) - 1

        for i in range(n):
            A = self.stacks[m_from].pop()
            self.stacks[m_to].push(A)

    def parse_instruction_2(self, instruction):

        match = re.findall(("\d+"), instruction)

        n = int(match[0])
        m_from = int(match[1]) - 1
        m_to = int(match[2]) - 1

        A_list = []

        for i in range(n):
            A_list.append(self.stacks[m_from].pop())
        
        A_list.reverse()

        for A in A_list:
            self.stacks[m_to].push(A)

def part_1(data):

    crane = Crane()

    for row in data:
        print(crane.stacks)
        crane.parse_instruction(row)

    print([s.top() for s in crane.stacks])

    return

def part_2(data):

    crane = Crane()

    for row in data:
        print(crane.stacks)
        crane.parse_instruction_2( row)

    print("".join([s.top() for s in crane.stacks]))

    return

data = read_text_file("5.txt")
part_1(data)
part_2(data)