import re
from collections import deque
from functools import reduce
from math import lcm

def read_text_file (file_path):

    with open(file_path, "r") as f: # open file in read only mode
        data = f.readlines() # read in as a list
        data = deque(line.replace("\n","") for line in data) #remove new line charachters

    return data

def parse_input(data:deque, worry_reduction):

    monkeys = []

    while data:
        next_line = data.popleft()

        if s := re.match(r"Monkey (\d+)", next_line):
            monkeys.append(Monkey(s.group(1), worry_reduction))

        elif re.search("Starting items", next_line):
            items = re.findall(r"\d+", next_line)
            items = [int(i) for i in items]
            monkeys[-1].add_items(items)

        elif re.search("Operation", next_line):
            monkeys[-1].set_operation(next_line)

        elif re.search("Test", next_line):
            monkeys[-1].set_test(next_line)
            monkeys[-1].m1 = int(re.search(r"(\d+)", data.popleft()).group(1))
            monkeys[-1].m2 = int(re.search(r"(\d+)", data.popleft()).group(1))     

    
    divs = [monkey.div for monkey in monkeys]
    div = lcm(*divs)

    for monkey in monkeys:
        monkey.m1 = monkeys[monkey.m1]
        monkey.m2 = monkeys[monkey.m2]
        monkey.total_div = div
    
    return monkeys    


class Monkey(object):
    def __init__(self, N, worry_reduction):
        self.N = N
        self.items = deque()
        self.m1 = None
        self.m2= None
        self.handeled = 0
        self.worry_reduction = worry_reduction
        self.total_div = 1

    def add_item(self, item):
        self.items.append(item)

    def add_items(self, items):
        self.items.extend(items)

    def inspect_item (self):
        item = self.items.popleft()
        item = self.operation(item)
        item = self.reduce_worry(item)

        if self.test(item):
            self.m1.add_item(item)
        else:
            self.m2.add_item(item)

        self.handeled += 1

    def inspect_all(self):
        while self.items:
            self.inspect_item()

    def reduce_worry (self, item):
        return (item //self.worry_reduction)%self.total_div

    def handeled_str(self):
        return f"Monkey {self.N} inspected items {self.handeled} times"

    def item_str(self):
        return f"Monkey {self.N}: {self.items}"

    def set_operation(self, line):
        if s:= re.search(r"(old) ([+*]) (\d+)", line):
            operator = s.group(2)
            self.operand = int(s.group(3))
            if operator == "+":
                self.operation = lambda x: x + self.operand
            elif operator == "*":
                self.operation = lambda x: x * self.operand
            else:
                raise NotImplementedError(f"{operator} not implemented")

        elif s:= re.search("(old) ([+*]) (old)", line):
            operator = s.group(2)
            if operator == "+":
                self.operation = lambda x: x + x
            elif operator == "*":
                self.operation = lambda x: x * x
            else:
                raise NotImplementedError(f"{operator} not implemented")

    def set_test(self, line):
        s = re.search(r"divisible by (\d+)", line)
        self.div = int(s.group(1))
        self.test = lambda x: x%self.div==0

def part_1(data, N, worry_reduction):

    monkeys = parse_input(data, worry_reduction)

    for round in range(N):

        #print(f"   {round}")

        for monkey in monkeys:
            monkey.inspect_all()

        # for monkey in monkeys:
        #     print(monkey.item_str())
        #     print(monkey.handeled_str())

    for monkey in monkeys:
        print(monkey.handeled_str())

    inspected = [monkey.handeled for monkey in monkeys]
    inspected.sort(reverse=True)
    return inspected[0] * inspected[1]

if __name__ == "__main__":

    data = read_text_file("11.txt")
    print(part_1(data, 20, 3))

    data = read_text_file("11.txt")
    print(part_1(data, 10000, 1))
