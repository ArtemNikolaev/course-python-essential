import io


def read_file(filename):
    f = io.open(filename, 'r', encoding='utf-8')
    string = f.readline()
    while string:
        yield string
        string = f.readline()
