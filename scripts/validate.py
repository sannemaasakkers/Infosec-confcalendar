#!/usr/bin/env python3
#
# Validate events.csv
import argparse
import csv
import pathlib


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', required=True, help='Path to CSV to validate')
    args = parser.parse_args()

    input_path = pathlib.Path(args.file)

    if not input_path.is_file():
        print(f'ERROR: Provided argument ("{args.input_path}") is not a file or not readable.')
        return 1

    fieldnames = ['Title', 'Start', 'End', 'Mark', 'URL']

    # Attempt to parse the CSV file and ensure all fields contain data.
    # Actual values aren't validated (yet).
    try:
        lineno = 1
        with open(input_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',', fieldnames=fieldnames)
            for row in reader:
                for field in fieldnames:
                    if not row.get(field):
                        print(f"Failed to validate line {lineno + 1}: {row}")
                        return 1
    except Exception as e:
        print(f'Failed to parse/validate {args.input_path}: {e}')
        return 1

    return 0

if __name__ == '__main__':
    main()
