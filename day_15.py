import re
from functools import reduce


def read_text_file (file_path):

    with open(file_path, "r") as f: # open file in read only mode
        data = f.readlines() # read in as a list
        data = [line.replace("\n","") for line in data] #remove new line charachters

    return data


def parse_data(data):
    

    gird = dict(default=".")

    
class EdgeSet(set):

    def __init__ (self, data, min_a, max_a):
        self.min_a = min_a
        self.max_a = max_a
        super().__init__(data)

    def add(self, a:tuple):
        if a[0] >= self.min_a and a[0] <= self.max_a and a[1] >= self.min_a and a[1] <= self.max_a:
            super().add(a)

class Sensor(object):
    def __init__(self, x ,y ,beacon_x, beacon_y):
        self.x = x
        self.y = y
        self.beacon_x = beacon_x
        self.beacon_y = beacon_y
        self.beacon_dist = self.dist(self.beacon_x, self.beacon_y)

    def dist (self, x, y):
        return abs(self.x-x) + abs(self.y-y)


    def within_beacon_dist(self, x, y):

        if self.dist(x, y) > self.beacon_dist:
            return False
        else:
            return True

    def on_beacon(self, x, y):

        if self.beacon_x == x and self.beacon_y == y:
            return True
        else:
            return False

    def end_row (self, y):
        '''
        last x in a given row y that is in range of beacon
        '''

        if not self.within_beacon_dist(self.x, y):
            raise Exception("y not in range")

        return (self.beacon_dist - abs(y - self.y)) + self.x

    def gen_edges(self, min_b, max_b):

        edges = EdgeSet([], min_b, max_b)

        point_1 = (self.x, self.y + self.beacon_dist + 1)
        point_2 = (self.x, self.y + self.beacon_dist + 1)
        edges.add(point_1)

        for i in range(self.beacon_dist + 1):
            point_1 = (point_1[0] + 1, point_1[1] - 1)
            point_2 = (point_2[0] + 1, point_2[1] - 1)
            edges.add(point_1)
            edges.add(point_2)

        for i in range(self.beacon_dist + 1):
            point_1 = (point_1[0] - 1, point_1[1] - 1)
            point_2 = (point_2[0] - 1, point_2[1] - 1)
            edges.add(point_1)
            edges.add(point_2)

        return edges

def part_1(data, y):

    sensors = []
    min_x = 0
    max_x = 0
    max_beacon_dist = 0
    for row in data:
        print(row)

        match = re.match("Sensor at x=(-*\d+), y=(-*\d+): closest beacon is at x=(-*\d+), y=(-*\d+)", row)
        sensors.append(Sensor(*(int(i) for i in match.groups())))

        min_x = min(sensors[-1].x, min_x)
        max_x = max(sensors[-1].x, max_x)
        max_beacon_dist = max(sensors[-1].beacon_dist, max_beacon_dist)

    no_beacon_count = 0
    for x in range(min_x - max_beacon_dist, max_x + max_beacon_dist, 1):
        for sensor in sensors:
            if sensor.within_beacon_dist(x, y):
                if not sensor.on_beacon(x, y):
                    no_beacon_count += 1
                    #print(x, y)
                break

    return no_beacon_count

def part_2(data, max_b):
    min_b = 0

    sensors = []

    for row in data:
        print(row)

        match = re.match(r"Sensor at x=(-*\d+), y=(-*\d+): closest beacon is at x=(-*\d+), y=(-*\d+)", row)
        sensors.append(Sensor(*(int(i) for i in match.groups())))

    for y in range(min_b, max_b+1):
        for x in range(min_b, max_b+1):            
            test = [sensor.within_beacon_dist(x, y) for sensor in sensors]
            test = reduce(lambda x,y: x|y , test)
            if not test:
                return x*4000000 + y

def part_2_fast(data, max_b):

    sensors = []

    for row in data:
        print(row)

        match = re.match("Sensor at x=(-*\d+), y=(-*\d+): closest beacon is at x=(-*\d+), y=(-*\d+)", row)
        sensors.append(Sensor(*(int(i) for i in match.groups())))

    min_b = 0
    x = 0
    y = 0
    in_range_flag = False

    while True:
        while True:
            
            for sensor in sensors:
                if sensor.within_beacon_dist(x, y):
                    x = sensor.end_row(y)
                    in_range_flag = True
                    break

            if not in_range_flag:
                print(x, y)
                return x*4000000 + y

            x += 1
            in_range_flag = False
            if x >= max_b:
                x = 0
                break
        y+= 1
        if y >= max_b:
            y = 0
            break


def part_2_morefast(data, max_b):
    sensors = gen_sensors(data)

    start_set = sensors[0].gen_edges(0, max_b+1)

    for sensor in sensors[1:]:
        start_set.intersection(sensor.gen_edges(0, max_b+1))

    return start_set 


def gen_sensors(data):

    sensors = []

    for row in data:
        print(row)

        match = re.match(r"Sensor at x=(-*\d+), y=(-*\d+): closest beacon is at x=(-*\d+), y=(-*\d+)", row)
        sensors.append(Sensor(*(int(i) for i in match.groups())))

    return sensors

if __name__ == "__main__":

    data = read_text_file("15.txt")
    #print(part_1(data, 2000000))

    print(part_2_morefast(data, 4000000))
