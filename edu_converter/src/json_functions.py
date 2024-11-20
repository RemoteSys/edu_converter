# coding: utf-8
import json
import csv
from collections import defaultdict


def read_json(path: str) -> dict:
    with open(path) as f:
        data = json.load(f)
    return data


def save_as_csv(data: dict, path):
    if isinstance(data, dict):
        headers = data.keys()
        data = zip(*data.values())
    else:
        tmp = defaultdict(list)
        for row in data:
            for key, val in row.items():
                tmp[key].append(val)
        data = dict(tmp)
        headers = data.keys()
        data = zip(*data.values())

    with open(path, mode="w", newline="") as fp:
        writer = csv.writer(fp)
        writer.writerow(headers)
        writer.writerows(data)


def from_json(path: str, out_path):
    """Function called in `main()` to handle `json` input data."""
    data = read_json(path)
    out_path = f"{out_path}.csv"
    save_as_csv(data, out_path)
    return out_path
