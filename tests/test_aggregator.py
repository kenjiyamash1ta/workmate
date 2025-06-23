import pytest
from core.aggregator import aggregate_data


def test_aggregate_data_avg(sample_data):
    result = aggregate_data(sample_data, "price=avg")
    assert result["column"] == "price"
    assert result["avg"] == pytest.approx((999 + 1199 + 199) / 3)


def test_aggregate_data_min(sample_data):
    result = aggregate_data(sample_data, "price=min")
    assert result["column"] == "price"
    assert result["min"] == 199


def test_aggregate_data_max(sample_data):
    result = aggregate_data(sample_data, "price=max")
    assert result["column"] == "price"
    assert result["max"] == 1199


def test_aggregate_data_invalid_operator(sample_data):
    with pytest.raises(ValueError):
        aggregate_data(sample_data, "price=sum")


def test_aggregate_data_invalid_column(sample_data):
    with pytest.raises(KeyError):
        aggregate_data(sample_data, "unknown=avg")


def test_aggregate_data_empty():
    from core.aggregator import aggregate_data
    assert aggregate_data([], "") == {}


def test_filter_data_empty_condition(sample_data):
    from core.filter import filter_data
    assert filter_data(sample_data, "") == sample_data
