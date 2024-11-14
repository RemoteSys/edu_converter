import xmltodict

# local imports
from edu_converter.src.functions import make_dict_flat, columns_to_list
from edu_converter.src.json_functions import save_as_csv

# ---


def xml_to_dict(path: str) -> dict:
    with open(path, "r") as f:
        data = xmltodict.parse(f.read(), dict_constructor=dict)

    data = make_dict_flat(data)
    return data


# ---


def from_xml(path: str, out_path: str) -> dict:
    """Function called in `main()` to handle `xml` input data."""
    data = xml_to_dict(path)
    data = columns_to_list(data)
    out_path = f"{out_path}.csv"
    save_as_csv(data, out_path)
    return out_path


# ---
