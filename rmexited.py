#!/usr/bin/env python3

from json import loads
from os import getuid
from subprocess import run
from sys import exit, stderr


def main():
    if getuid() != 0:
        print("This script must be run w/ root permissions", file=stderr)
        exit(1)

    completed_process = run(
        ['docker', 'container', 'ls', '--format', 'json', '--all'],
        capture_output=True,
        text=True,
    )

    exited_container_ids = []
    for line in completed_process.stdout.split('\n'):
        line = line.strip()
        if not line:
            break
        json = loads(line)
        if not json['Status'].startswith('Exited'):
            continue
        exited_container_ids.append(json['ID'])

    for container_id in exited_container_ids:
        run(['docker', 'container', 'rm', container_id])


if __name__ == '__main__':
    main()
