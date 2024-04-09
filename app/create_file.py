from sys import argv
from os import makedirs, getcwd, path
from datetime import datetime


def create_dirs(dir_1: str, dir_2: str) -> None:
    makedirs(path.join(getcwd(), dir_1, dir_2))


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


if __name__ == "__main__":
    terminal_arguments = argv[1:]
    if terminal_arguments[0] == "-d" and "-f" not in terminal_arguments:
        create_dirs(terminal_arguments[1], terminal_arguments[2])

    if terminal_arguments[0] == "-f" and "-d" not in terminal_arguments:
        filling_file_with_content(terminal_arguments[1])

    if "-d" in terminal_arguments and "-f" in terminal_arguments:
        create_dirs(terminal_arguments[1], terminal_arguments[2])
        file_path = new_dir_path = path.join(
            getcwd(),
            terminal_arguments[1],
            terminal_arguments[2],
            terminal_arguments[4]
        )
        filling_file_with_content(file_path)
