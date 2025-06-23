import csv
from typing import List, Dict, Any


def read_csv(file_path: str) -> List[Dict[str, Any]]:
    with open(file_path, mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        return [row for row in reader]