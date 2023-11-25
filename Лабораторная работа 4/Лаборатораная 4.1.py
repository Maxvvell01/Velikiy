import json


FILENAME = "input.json"


def task() -> float:
    with open(FILENAME, encoding="utf-8") as input:
        python_obj = json.load(input)
    sum_ = sum([item["score"] * item["weight"] for item in python_obj])
    return round(sum_, 3)


print(task())
