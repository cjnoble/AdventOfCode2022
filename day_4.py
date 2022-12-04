def read_text_file (file_path):

    with open(file_path, "r") as f:
        data = f.readlines()
        data = [line.replace("\n","") for line in data]

    return data



def part_1(data):

    total = 0

    for row in data:
        p1 = row[0]
        p2 = row[1]

        if (p1[0] <= p2[0] and p1[1] >= p2[1]) or (p1[0] >= p2[0] and p1[1] <= p2[1]):
            total += 1

    print(total)


def part_2(data):

    total = 0

    for row in data:
        p1 = row[0]
        p2 = row[1]

        if p1[1] >= p2[1]:
            if p2[1] >= p1[0]:
                total += 1
        else:
            if (p1[1] >= p2[0]):
                total += 1

    return total


def prepare_data (data):

    data = [row.split(",") for row in data]
    data = [[i.split("-") for i in row] for row in data]
    data = [[[int(j) for j in i] for i in row] for row in data]

    return data


if __name__ == "__main__":
    data = read_text_file("4.txt")

    data = prepare_data(data)

    part_1(data)
    print(part_2(data))