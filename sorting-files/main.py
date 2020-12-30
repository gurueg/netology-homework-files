import os

CWD = os.getcwd()
FILES_FOLDER = os.path.join(CWD, 'sorted')


def get_files_list():
    files_list = [name for name in os.listdir(FILES_FOLDER) if os.path.isfile(os.path.join(FILES_FOLDER, name))]
    return files_list


def get_lines_count(file_name):
    file_path = os.path.join(FILES_FOLDER, file_name)

    with open(file_path, encoding='utf-8') as f:
        count = 0
        for line in f:
            count += 1

    return count


def main():
    files_list = get_files_list()

#     Предполагаем, что файлы достаточно малы
    sorted_list = sorted(files_list, key=lambda f_name: get_lines_count(f_name))

    result_path = os.path.join(CWD, 'result.txt')

    if os.path.exists(result_path):
        with open(result_path, 'w') as f:
            pass

    for file in sorted_list:
        file_path = os.path.join(FILES_FOLDER, file)
        lines_count = get_lines_count(file)

        with open(result_path, 'a', encoding='utf-8') as f_result, \
                open(file_path, encoding='utf-8') as f_read:

            f_result.write(file + '\n')
            f_result.write(str(lines_count) + '\n')

            for line in f_read:
                f_result.write(line)

            f_result.write('\n')


if __name__ == '__main__':
    main()
