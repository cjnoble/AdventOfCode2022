
def read_text_file (file_path):

    with open(file_path, "r") as f:
        data = f.readlines()
        data = [line.replace("\n","") for line in data]

    return data


def calc(data):

    total_data = []
    part = []
    current_max = 0
    sum_total = []

    for row in data:

        if row == "":
            total_data.append(part)
            current_max = max(current_max, sum(part))
            sum_total.append(sum(part))
            part = []

        else:
            part.append(int(row))

    print(current_max)
    sum_total.sort(reverse=True)
    print(sum_total)
    print(sum(sum_total[:3]))


data = read_text_file ("1_other.txt")

calc(data)