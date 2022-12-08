def read_text_file (file_path):

    with open(file_path, "r") as f: # open file in read only mode
        data = f.readlines() # read in as a list
        data = [line.replace("\n","") for line in data] #remove new line charachters
        data = [[tree for tree in line] for line in data]

    return data


class Tree(object):
    def __init__(self, x, y, height, visible: bool):
        self.x = x
        self.y = y
        self.visible = visible
        self.height = height
        self.score = 1

    def check_visability(self, h):
        if self.height > h:
            self.visible = True
            h = self.height
        return h

    def scenic_check(self, h):
        if self.height < h:
            return True
        return False

def iterate_trees_h (trees, i_iter, j_iter, h_init=-1):
    for i in i_iter:
        h_seen = h_init
        for j in j_iter:
            h_seen = trees[i][j].check_visability(h_seen)

def iterate_trees_v (trees, i_iter, j_iter,h_init=-1):
    for j in j_iter:
        h_seen = h_init
        for i in i_iter:
            h_seen = trees[i][j].check_visability(h_seen)

def iterate_row (trees, i_iter, j, h):
    view = 0
    for i in i_iter:
        tree = trees[i][j]
        view += 1
        if not tree.scenic_check(h):
            break
    return view

def iterate_column (trees, i, j_iter, h):
    view = 0
    for j in j_iter:
        tree = trees[i][j]
        view += 1
        if not tree.scenic_check(h):
            break
    return view

def part_1 (data):
    trees = [[Tree(x, y, int(height), False) for y, height in enumerate(row)] for x, row in enumerate(data)]

    rows = len(trees)
    columns = len(trees[0])

    iterate_trees_h(trees, range(columns), range(rows))
    iterate_trees_h(trees, range(columns), range(-1, -rows-1, -1))
    iterate_trees_v(trees, range(columns), range(rows))
    iterate_trees_v(trees, range(-1, -columns-1, -1), range(rows))

    visible_trees = 0

    for row in trees:
        for tree in row:
            if tree.visible:
                visible_trees += 1

    return visible_trees

def part_2(data):
    trees = [[Tree(x, y, int(height), False) for y, height in enumerate(row)] for x, row in enumerate(data)]

    rows = len(trees)
    columns = len(trees[0])

    best_tree = Tree(0, 0, 0, False)

    for tree in [tree for row in trees for tree in row]:
        tree.score *= iterate_row(trees, range(tree.x+1, rows), tree.y, tree.height)
        tree.score *= iterate_row(trees, range(tree.x-1, -1, -1), tree.y, tree.height)

        tree.score *= iterate_column(trees, tree.x, range(tree.y+1, columns), tree.height)
        tree.score *= iterate_column(trees, tree.x, range(tree.y-1, -1, -1), tree.height)

        if tree.score > best_tree.score:
            best_tree = tree

    return best_tree.score


if __name__ == "__main__":

    data = read_text_file("8.txt")
    print(part_1(data))
    print(part_2(data))

