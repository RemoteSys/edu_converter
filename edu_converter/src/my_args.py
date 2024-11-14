import argparse
from pathlib import Path


def my_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="Path to data file (*.csv)")
    parser.add_argument(
        "-o", "--out_name", type=str, help="Name of file with resualts."
    )
    parser.add_argument("-s", "--sep",
                        type=str,
                        help="If the script incorrectly detects the column \
                                separator in the '*.csv' file, you can \
                                specify it manually")
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Option to enable displaying additional \
                                information.",
    )

    args = parser.parse_args()
    return args


def args_handle(args):
    args.path = str(Path(args.path).resolve())

    if args.out_name is None:
        stem = Path(args.path).stem
        args.out_name = f"{stem}_results"

    args.out_path = str(Path(args.path).parent / args.out_name)
    return args
