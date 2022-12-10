import re

def read_text_file (file_path):

    with open(file_path, "r") as f: # open file in read only mode
        data = f.readlines() # read in as a list
        data = [line.replace("\n","") for line in data] #remove new line charachters

    return data

class CRT(object):
    
    def __init__(self, N=240):
        self.N = N
        self.display = ["." for i in range(N)]
        self.sprite_width = 3
        self.pos = 0
        self.width = 40

    def update(self, sprite_pos):
        if abs(sprite_pos-self.pos%self.width) <= self.sprite_width //2:
            self.display[self.pos] = "#"
        self.pos += 1

    def show(self):
        rows = self.N//self.width
        r = []
        for row in range(rows):
            r.append("".join(self.display[row*self.width:(row+1)*self.width]))
        print("\n".join(r))


class CPU (object):
    def __init__(self, crt, refs=[]):
        self.x = 1
        self.cycles = 0
        self.ref_cycles = refs
        self.strengths = {}
        self.crt = crt

    def check_ref_cycles(self):
        if self.cycles in self.ref_cycles:
            self.strengths[self.cycles] = self.x*self.cycles

        #print(self.cycles, self.x, self.x*self.cycles)

    def cycle(self, cycles):
        for i in range(cycles, 0, -1):
            self.cycles += 1
            self.crt.update(self.x)
            self.check_ref_cycles()

    def noop(self):
        cycles = 1
        self.cycle(cycles)

    def addx(self, x):
        cycles = 2
        self.cycle(cycles)
        self.x += x




def part_1(data, refs):
    cpu = CPU(CRT(), refs)

    for instruct in data:
        if re.match("noop", instruct):
            cpu.noop()

        elif i := re.match("addx (-*\d+)", instruct):
            cpu.addx(int(i.group(1)))
            
        else:
            print(instruct)

    return cpu.strengths

def part_2(data):
    cpu = CPU(CRT())

    for instruct in data:
        if re.match("noop", instruct):
            cpu.noop()

        elif i := re.match("addx (-*\d+)", instruct):
            cpu.addx(int(i.group(1)))
            
        else:
            print(instruct)

    cpu.crt.show()
    

if __name__ == "__main__":

    data = read_text_file("10.txt")
    res = part_1(data, [20, 60, 100, 140, 180, 220])
    print(sum(res.values()))
    
    part_2(read_text_file("10.txt"))


