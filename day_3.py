from functools import reduce

def read_text_file (file_path):

    with open(file_path, "r") as f:
        data = f.readlines()
        data = [line.replace("\n","") for line in data]

    return data


def score(c):

    n = ord(c)

    if ord("A") <= n <= ord("Z"):
        offset = 27
        return (n - ord("A")) + offset

    elif ord("a") <= n <= ord("z"):
        offset = 1
        return (n - ord("a")) + offset

    else:
        return 0


def part_1 (data):

    total_score = 0

    for row in data:
        split = len(row)//2
        pack_1 = row[:split]

        pack_2 = row[split:]

        items_1 = set(pack_1)
        for item in pack_2:
            if item in items_1:
                total_score += score(item)
                break

    return total_score

def trip_groups (data):

    iterator = iter(data)

    while True:
        try:
            yield (next(iterator), next(iterator), next(iterator))

        except StopIteration:
            break

def part_2 (data):

    badge_total = 0

    for group in trip_groups(data):

        group = [set(g) for g in group]
        badge = reduce (lambda x, y: x.intersection(y), group).pop()
        badge_total += score(badge)

    return badge_total



if __name__ == "__main__":

    data = read_text_file("3.txt")

    print(part_2(data))


