import re
from functools import reduce
from collections import deque
from math import inf

def read_text_file (file_path):

    with open(file_path, "r") as f: # open file in read only mode
        data = f.readlines() # read in as a list
        data = [line.replace("\n","") for line in data] #remove new line charachters

    return data



class Valve(object):

    def __init__(self, id, flow_rate, connected):
        self.id = id
        self.flow_rate = flow_rate
        self.connected = connected
        self.dist_weight = inf
        self.potential = 0
        self.next_potential = 0

    def __repr__(self):
        
        return f"Valve {self.id} has flow rate={self.flow_rate}; tunnels lead to valves {','.join(self.connected)}; dist is {self.dist_weight}; potential is {self.potential}"

    def __str__(self):
        return self.__repr__()

def parse_data(data):

    valves = {}

    for row in data:
        match = re.search(r"Valve ([A-Z]+) has flow rate=(\d+)", row)
        valve = match.group(1)
        flow_rate = int(match.group(2))
        match = re.findall(r"([A-Z]+)", row)
        paths = [i for i in match[2:]]

        valves[valve] = Valve(valve, flow_rate, paths)
    return valves

def part_1(data, time):
    valves = parse_data(data)

    START = "AA"

    current_valves = deque([valves[START]])
    current_time = 0

    seen_valves = set()
    while current_valves:

        current_time += 2
        next_valves = deque()
        while current_valves:
            current_valve = current_valves.popleft()
            current_valve.dist_weight = min(current_time, current_valve.dist_weight)
            current_valve.potential = max((time - current_valve.dist_weight)*current_valve.flow_rate , current_valve.potential)

            if current_valve not in seen_valves:
                next_valves.extend([valves[id] for id in current_valve.connected])
                seen_valves.add(current_valve)
        current_valves = next_valves
        

    for valve in valves.values():
        print (valve)

    # while True:

    #     current_potential = time * current_valve.flow_rate

    #     for id in current_valve.connected:
    #         valves[id]
    #         valve_potential = valves[id].flow_rate * max(time-2, 0)
    #         if valve_potential > current_potential:
    #             pass

TIME = 30


if __name__ == "__main__":

    
    data = read_text_file("16.txt")

    print(part_1(data, TIME))

