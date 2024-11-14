from edu_converter.src import functions as fn
from edu_converter.src.my_args import my_parser, args_handle
from edu_converter.src import csv_functions as csv_fn
from edu_converter.src import xml_functions as xml_fn
from edu_converter.src import json_functions as json_fn
from pprint import pp
# ---


def verb(obj):
    """Displays an object (obj) on the screen if the script is run with
    the '-v'(--verbose) option."""
    if args.verbose:
        pp(obj)
        print()
# ---


def main():
    global args
    args = my_parser()
    args = args_handle(args)
    verb(vars(args))

    funcion_name = fn.data_type_recognition(args.path)
    from_function = None

    for module in (csv_fn, xml_fn, json_fn):
        if hasattr(module, funcion_name):
            from_function = getattr(module, funcion_name)
    verb({"from_function": from_function.__name__})

    out_path = from_function(args.path, args.out_path)
    msg = f'Results were saved to:\n\t{out_path}\n'
    print(msg)
    
if __name__ == '__main__':
    main()
