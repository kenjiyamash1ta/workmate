import argparse
from typing import Dict, Any


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Process CSV file.")
    parser.add_argument("file", type=str, help="Path to the CSV file")
    parser.add_argument(
        "--where",
        type=str,
        default="",
        help='Filter, "price>500"',
    )
    parser.add_argument(
        "--aggregate",
        type=str,
        default="",
        help='Aggregate, "price=avg"',
    )
    return parser


def parse() -> Dict[str, Any]:
    parser = create_parser()
    args = parser.parse_args()
    return vars(args)
