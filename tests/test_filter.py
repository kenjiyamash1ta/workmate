import pytest
from core.filter import filter_data, parse_condition


def test_filter_data_equal(sample_data):
    filtered = filter_data(sample_data, "name=redmi")
    assert len(filtered) == 1
    assert filtered[0]["name"] == "redmi"


def test_filter_data_greater(sample_data):
    filtered = filter_data(sample_data, "price>500")
    assert len(filtered) == 2
    assert all(float(row["price"]) > 500 for row in filtered)


def test_filter_data_less(sample_data):
    filtered = filter_data(sample_data, "price<500")
    assert len(filtered) == 1
    assert all(float(row["price"]) < 500 for row in filtered)


def test_filter_data_greater_equal(sample_data):
    filtered = filter_data(sample_data, "price>=999")
    assert all(float(row["price"]) >= 999 for row in filtered)


def test_filter_data_less_equal(sample_data):
    filtered = filter_data(sample_data, "price<=199")
    assert all(float(row["price"]) <= 199 for row in filtered)


def test_parse_condition():
    assert parse_condition("price>500") == ("price", ">", "500")
    assert parse_condition("name=redmi") == ("name", "=", "redmi")
    assert parse_condition("rating<4.7") == ("rating", "<", "4.7")


def test_parse_condition_invalid():
    with pytest.raises(ValueError):
        parse_condition("price!500")


def test_filter_data_invalid_column(sample_data):
    with pytest.raises(KeyError):
        filter_data(sample_data, "unknown=redmi")


def test_filter_data_invalid_operator(sample_data):
    with pytest.raises(KeyError):
        filter_data(sample_data, "price!=500")


def test_filter_data_no_match(sample_data):
    filtered = filter_data(sample_data, "name=nonexistent")
    assert len(filtered) == 0
    assert all(row["name"] != "nonexistent" for row in sample_data)
