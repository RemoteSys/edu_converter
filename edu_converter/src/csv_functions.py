import csv
import json
from collections import Counter, defaultdict


def scan_csv(path: str, n: int):
    with open(path) as f:
        txt = [f.readline() for _ in range(n)]

    txt = "".join(txt)
    counts = Counter(txt)
    separators = [".", ",", ";", "\t"]
    count_sep = [(s, counts.get(s, 0)) for s in separators]
    sep = max(count_sep, key=lambda item: item[-1])
    count_sep.remove(sep)
    decimal = max(count_sep, key=lambda item: item[-1])
    return sep[0], decimal[0]


def convert2numeric(x: str):
    if x.isdigit():
        return int(x)
    else:
        try:
            return float(x)
        except ValueError:
            return x


def read_csv(path: str, n: int = 5) -> list[list]:
    sep, decimal = scan_csv(path, n=n)
    with open(path) as f:
        reader = csv.reader(f, delimiter=sep)
        # reader = csv.DictReader(f, delimiter=delimiter)
        data = []
        for line in reader:
            if decimal != ".":
                line = [item.replace(decimal, ".") for item in line]
            line = [convert2numeric(item) for item in line]
            data.append(line)
        return data


def csv_to_dict(data: list[list]) -> dict:
    """Converts a list of data of type:
      - [[headers], [values], values],...]
    to a dictionary of columns:
      - {head: [...], head: [...], ...}"""
    data = data[:]
    data_dict = defaultdict(list)
    headers = data.pop(0)

    for row in data:
        for key, val in zip(headers, row):
            data_dict[key].append(val)

    return dict(data_dict)


# ---


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


# ---


def save_as_json(data: dict, path: str, indent=2):
    if isinstance(data, dict):
        keys = data.keys()
        rows = zip(*data.values())
        data = [dict(zip(keys, val)) for val in rows]

    with open(path, "w") as f:
        json.dump(data, f, indent=indent)


# ---


def from_csv(path: str, out_path: str) -> dict:
    """Function called in `main()` to handle `csv` input data."""
    data = read_csv(path)
    data = csv_to_dict(data)
    out_path = f"{out_path}.json"
    save_as_json(data, out_path)
    return out_path


# ---
