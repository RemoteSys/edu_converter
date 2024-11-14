from collections import defaultdict
from pathlib import Path
# ---


def make_dict_flat(dc: dict, flat_dc=None) -> dict:
    """Converts a nested dictionary:
        {key:
            {key1:
                {key2:
                    { ... }

                }
            }
        }


    into a flat dictionary of type table:
    {key1: [...],
     key2: [...]
     key3: ...
     }

     where:
      - `keys` are column headings
      - lists [...] are column values.
    """
    if flat_dc is None:
        flat_dc = defaultdict(list)

    for key, val in dc.items():
        if not isinstance(val, (dict, list)):
            if key[0] in ("@", "#"):
                key = key[1:]
            flat_dc[key].append(val)
        elif isinstance(val, dict):
            make_dict_flat(val, flat_dc)
        elif isinstance(val, list):
            for item in val:
                if isinstance(item, dict):
                    make_dict_flat(item, flat_dc)
                else:
                    flat_dc[key].append(item)
    return dict(flat_dc)


def data_type_recognition(path: str):
    suffix = Path(path).suffix
    if suffix == ".xml":
        return "from_xml"
    elif suffix == ".csv":
        return "from_csv"
    elif suffix == ".json":
        return "from_json"
    else:
        return None


def columns_to_list(dc: dict[list]) -> list[dict]:
    """Converts a table-type data dictionary, i.e. keys are column names
    and dictionary values are lists of values:
            {
             key: [ ... ],
             key: [ ... ],
               ...,
            }
    into a list of dictionaries where each dictionary has the same keys:
         [{key: val, ...}, {key: val, ...}, ... ]
    """
    res = []
    headers = dc.keys()
    vals = zip(*dc.values())
    for val in vals:
        res.append(dict(zip(headers, val)))
    return res


def list_to_columns(ll: list[dict]) -> dict[list]:
    """Converts a list of dictionaries where each dictionary has the
    same keys:
         [{key: val, ...}, {key: val, ...}, ... ]


    into a table-type data dictionary, i.e. keys are column names
    and dictionary values are lists of values:
            {
             key: [ ... ],
             key: [ ... ],
               ...,
            }
    """

    res = defaultdict(list)
    for row in ll:
        for key, val in row.items():
            res[key].append(val)
    data = dict(res)
    return data
