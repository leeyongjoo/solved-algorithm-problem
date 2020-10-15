import os
from urllib import parse

site_name = [
    'programmers', 'baekjoon'
]


def get_file_list(dir_name):
    dir_list = os.listdir(dir_name)
    file_list = []  # dir, file_list
    for d in dir_list:
        files = os.listdir(os.path.join(dir_name, d))
        file_list.append((d, files))
    return file_list


def to_md_string(name, url):
    return f'- [{name}]({url})'


def to_md_string_file_list(site_name, file_list):
    for level, files in file_list:
        print(level)

        for file in files:
            name = file.split('.')[0]
            print(to_md_string(name, 'https://' + parse.quote(
                f'github.com/leeyongjoo/solved-algorithm-problem/blob/master/{site_name}/{level}/{file}')))


def load_file_list_txt():
    pass


def save_file_list_txt():
    pass


def main():
    to_md_string_file_list(site_name[0], get_file_list(site_name[0]))


if __name__ == "__main__":
    main()
