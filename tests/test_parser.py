import sys
from cli import parser


def test_create_parser_exists():
    p = parser.create_parser()
    assert p is not None


def test_parse_file_only(monkeypatch):
    test_args = ["prog", "--file", "products.csv"]
    monkeypatch.setattr(sys, "argv", test_args)
    args = parser.parse()
    assert args["file"] == "products.csv"
    assert args["where"] == ""
    assert args["aggregate"] == ""


def test_parse_with_where_and_aggregate(monkeypatch):
    test_args = [
        "prog", "--file", "products.csv",
        "--where", "price>500",
        "--aggregate", "price=avg"
    ]
    monkeypatch.setattr(sys, "argv", test_args)
    args = parser.parse()
    assert args["file"] == "products.csv"
    assert args["where"] == "price>500"
    assert args["aggregate"] == "price=avg"
