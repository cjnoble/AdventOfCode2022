import re


def read_text_file (file_path):

    with open(file_path, "r") as f: # open file in read only mode
        data = f.readlines() # read in as a list
        data = [line.replace("\n","") for line in data] #remove new line charachters

    return data


def parse_data(data):
    

    gird = dict(default=".")

    


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



def part_2():

    min_b = 0
    max_b = 4000000


if __name__ == "__main__":

    data = read_text_file("15.txt")
    print(part_1(data, 2000000))