

def read_line(file_path):
    with open(file_path) as file:
        return file.readline().strip()



def read_lines(file_path):
    lines = []

    with open(file_path) as file:
        for line in file:
            line = line.strip()
            if line:
                lines.append(line)

    return lines



def read_lines_of_words(file_path):
    lines = []

    with open(file_path) as file:
        for line in file:
            line = line.strip()
            if line:
                lines.append([word for word in line.split()])

    return lines



def read_int(file_path):
    with open(file_path) as file:
        return int(file.readline().strip())



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

