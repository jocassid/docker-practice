
from datetime import datetime
from os import environ
from pathlib import Path
from time import sleep


def get_log_file_path() -> Path:
    env_var = 'LOG_FILE_PATH'
    log_file_path: str = environ.get(env_var)
    if not log_file_path:
        raise ValueError(f"Environment variable {env_var} not set")
    print(f"{log_file_path=}")
    return Path(log_file_path)


def count_lines_in_file(log_file_path: Path) -> int:
    line_count = 0
    if not log_file_path.exists():
        return 0
    with open(log_file_path, 'r') as in_file:
        for _ in in_file:
            line_count += 1
    return line_count


def main():
    log_file_path = get_log_file_path()
    line_count = count_lines_in_file(log_file_path)

    with open(log_file_path, 'a') as out_file:
        print(
            f"{datetime.now().strftime('%Y-%m-%dT%H:%M:%S')} there were "
            f"{line_count} lines in the file",
            file=out_file
        )


if __name__ == "__main__":
    main()