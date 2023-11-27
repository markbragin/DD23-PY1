import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    """Converts data from CSV to JSON."""

    with open(INPUT_FILENAME, "r") as f:
        data = [item for item in csv.DictReader(f)]

    with open(OUTPUT_FILENAME, "w") as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
