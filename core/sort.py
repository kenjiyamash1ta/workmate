from typing import List, Dict, Any


def sort_data(
    data: List[Dict[str, Any]], order_by: str
) -> List[Dict[str, Any]]:
    if not order_by:
        return data
    column, direction = order_by.split("=")
    reverse = direction.lower() == "desc"

    def key(row):
        value = row[column]
        try:
            return float(value)
        except ValueError:
            return value
    return sorted(data, key=key, reverse=reverse)
