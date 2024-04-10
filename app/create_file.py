import argparse
import os
from datetime import datetime


def create_dirs(dir_1: str, dir_2: str) -> None:
    os.makedirs(os.path.join(os.getcwd(), dir_1, dir_2), exist_ok=True)


def filling_file_with_content(file_name: str) -> None:
    with open(file_name, "a") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        line_index = 0
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            line_index += 1
            file.write(f"{line_index} {line}\n")


def main():
    parser = argparse.ArgumentParser(description="Create directories and fill a file with content")
    parser.add_argument("-d", "--dir", nargs=2, help="Directory names", metavar=("dir_1", "dir_2"))
    parser.add_argument("-f", "--file", help="File name")
    args = parser.parse_args()

    if args.dir and args.file:
        create_dirs(args.dir[0], args.dir[1])
        file_path = os.path.join(os.getcwd(), args.dir[0], args.dir[1], args.file)
        filling_file_with_content(file_path)

    if args.dir:
        create_dirs(args.dir[0], args.dir[1])

    if args.file:
        filling_file_with_content(args.file)


if __name__ == "__main__":
    main()
