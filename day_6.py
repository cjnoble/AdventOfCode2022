def read_text_file (file_path):

    with open(file_path, "r") as f:
        data = f.readlines()
        data = [line.replace("\n","") for line in data]

    return data


def four_wise(iterator):

    iteratror = iter(iterator)

    while True:
        try:
            pass

        except StopIteration:
            break

def part_1(data):
    return(marker(data, 4))

def part_2(data):
    return(marker(data, 14))

def marker (data, marker_len):

    for i in range(len(data) - (marker_len + 1)):
        s = set(data[i:i+marker_len])
        if len(s) == marker_len:
            return i+marker_len  


if __name__ == "__main__":

    data = read_text_file("6.txt")

    print(part_1(data[0]))
    print(part_2(data[0]))