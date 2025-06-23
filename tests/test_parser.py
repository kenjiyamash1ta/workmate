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


def test_parse_with_order_by(monkeypatch):
    test_args = [
        "prog", "--file", "products.csv",
        "--order-by", "brand=desc"
    ]
    monkeypatch.setattr(sys, "argv", test_args)
    args = parser.parse()
    assert args["file"] == "products.csv"
    assert args["order_by"] == "brand=desc"


def test_parse_with_all_args(monkeypatch):
    test_args = [
        "prog", "--file", "products.csv",
        "--where", "price>500",
        "--aggregate", "price=avg",
        "--order-by", "brand=asc"
    ]
    monkeypatch.setattr(sys, "argv", test_args)
    args = parser.parse()
    assert args["file"] == "products.csv"
    assert args["where"] == "price>500"
    assert args["aggregate"] == "price=avg"
    assert args["order_by"] == "brand=asc"
