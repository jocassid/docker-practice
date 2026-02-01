
from datetime import datetime
from os import environ
from time import sleep


def get_log_file_path() -> str:
    env_var = 'LOG_FILE_PATH'
    log_file_path: str = environ.get(env_var)
    if not log_file_path:
        raise ValueError(f"Environment variable {env_var} not set")
    return log_file_path


def count_lines_in_file() -> int:
    log_file_path = get_log_file_path()

    line_count = 0
    with open(log_file_path, 'r') as in_file:
        for _ in in_file:
            line_count += 1
    return line_count


def main():
    line_count = count_lines_in_file()

    with open(get_log_file_path(), 'w+') as out_file:
        print(
            f"{datetime.now().strftime('%Y-%m-%dT%H:%M:%S')} there are "
            f"{line_count} lines in the file",
            file=out_file
        )

    sleep(120)


if __name__ == "__main__":
    main()