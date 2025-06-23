from core.sort import sort_data


def test_sort_data_asc(sample_data):
    sorted_data = sort_data(sample_data, "name=asc")
    assert [row["name"] for row in sorted_data] == ["galaxy", "iphone", "redmi"]


def test_sort_data_desc(sample_data):
    sorted_data = sort_data(sample_data, "name=desc")
    assert [row["name"] for row in sorted_data] == ["redmi", "iphone", "galaxy"]


def test_sort_data_numeric_asc(sample_data):
    sorted_data = sort_data(sample_data, "price=asc")
    assert [row["price"] for row in sorted_data] == ["199", "999", "1199"]


def test_sort_data_numeric_desc(sample_data):
    sorted_data = sort_data(sample_data, "price=desc")
    assert [row["price"] for row in sorted_data] == ["1199", "999", "199"]


def test_sort_data_empty_order_by(sample_data):
    sorted_data = sort_data(sample_data, "")
    assert sorted_data == sample_data
