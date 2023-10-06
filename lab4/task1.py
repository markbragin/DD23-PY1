import json


def task() -> float:
    """Sums products of weights and scores.

    Reads the list of dicts from json file. Dicts have "score" and "weight"
    keys whose values will be multiplied.

    Returns:
        A float which is the sum of such products. Rounded to 3 digits after the
        decimal point.
    """

    with open("input.json", "r") as f:
        data = json.load(f)

    return round(sum(item["score"] * item["weight"] for item in data), 3)


if __name__ == "__main__":
    print(task())
