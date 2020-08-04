def create_cast_list(filename):
    cast_list = []
    with open(filename, 'r') as f:
        for line in f:
            cast_list.append(line.split(',')[0])

    return cast_list


# traditional read
def read_file(file_name):
    f = open(file_name, 'r')
    file_data = f.read()
    f.close()
    return file_data


# read file using with
def read_file_with(file_name):
    file_lines = []
    # with open ('./data-w.txt', 'r') as f1:
    with open(file_name, 'r') as f:
        for line in f:
            file_lines.append(line.strip())
    return file_lines

# write a file in append
def append_file(file_name):
    file_data = read_file('./data.txt')
    f = open(file_name, 'a')
    written_data = f.write(file_data)
    f.close()

    return written_data


def main():
    print('1 - Testing Read file function')
    data = read_file('data.txt')
    data = append_file('data-w.txt')
    print('File data is --> ', data)

    print('\n 2 - Testing create_cast_list function')
    data = create_cast_list('list_cast.txt')
    print('create_cast_list data is --> ', data)


# write all the executable statements here
if __name__ == '__main__':
    main()

