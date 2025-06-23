import tempfile
import csv
from core.reader import read_csv


def test_read_csv():
    with tempfile.NamedTemporaryFile(mode="w",
                                     suffix=".csv",
                                     delete=False) as tmp:
        writer = csv.DictWriter(tmp, fieldnames=["name", "price"])
        writer.writeheader()
        writer.writerow({"name": "test", "price": "100"})
        tmp.flush()
        tmp_name = tmp.name

    data = read_csv(tmp_name)
    assert len(data) == 1
    assert data[0]["name"] == "test"
    assert data[0]["price"] == "100"
