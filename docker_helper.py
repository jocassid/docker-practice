#!/usr/bin/env python3

from argparse import ArgumentParser, Namespace
from json import loads
from os import getuid
from re import compile as re_compile, IGNORECASE
from subprocess import CompletedProcess, run
from sys import exit, stderr
from typing import Iterator, List


def get_lines_as_json(args: List[str]) -> Iterator[dict]:
    completed_process = run(
        args,
        capture_output=True,
        text=True,
    )
    for line in completed_process.stdout.split('\n'):
        line = line.strip()
        if not line:
            break
        yield loads(line)


def get_container_info() -> Iterator[dict]:
    yield from get_lines_as_json(
        ['docker', 'container', 'ls', '--format', 'json', '--all'],
    )


def get_volume_info() -> Iterator[dict]:
    yield from get_lines_as_json(
        ['docker', 'volume', 'ls', '--format', 'json'],
    )


def remove_exited_containers():
    for container_json in get_container_info():
        if not container_json['Status'].startswith('Exited'):
            continue
        run(['docker', 'container', 'rm', container_json['ID']])


def remove_unnamed_volumes():
    hex_name_pattern = re_compile(r'^[0-9a-f]{64}$', IGNORECASE)
    for volume_json in get_volume_info():
        volume_name = volume_json['Name']
        if hex_name_pattern.match(volume_name):
            print(f"Removing unnamed volume {volume_name}")
            run(['docker', 'volume', 'rm', volume_name])



def build_argument_parser() -> ArgumentParser:
    parser = ArgumentParser(description='Helper script for Docker')
    subparsers = parser.add_subparsers(dest='command', help='sub-command help')
    subparsers.add_parser('rm_exited_containers', help='remove exited containers')
    subparsers.add_parser('rm_unnamed_volumes', help='remove unnamed volumes')
    return parser


def main():
    if getuid() != 0:
        print("This script must be run w/ root permissions", file=stderr)
        exit(1)

    arg_parser = build_argument_parser()
    args = arg_parser.parse_args()

    if args.command == 'rm_exited_containers':
        remove_exited_containers()
    elif args.command == 'rm_unnamed_volumes':
        remove_unnamed_volumes()
    else:
        arg_parser.print_help()


if __name__ == '__main__':
    main()
