


def read_ints(file_path):
    ints = []

    with open(file_path) as file:
        for line in file:
            line = line.strip()
            if line:
                ints.append(int(line))

    return ints



def read_lines_of_ints(file_path):
    lines = []

    with open(file_path) as file:
        for line in file:
            line = line.strip()
            if line:
                lines.append([int(i) for i in line.split()])

    return lines


