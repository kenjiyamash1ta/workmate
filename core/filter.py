from typing import List, Dict, Any


def parse_condition(condition: str) -> tuple[str, str, str]:
    operators = ["<=", ">=", "=", ">", "<"]
    for op in operators:
        if op in condition:
            parts = condition.split(op)
            if len(parts) == 2:
                return parts[0].strip(), op, parts[1].strip()
    raise ValueError(f"Invalid condition: {condition}")


def filter_data(
    data: List[Dict[str, Any]], condition: str
) -> List[Dict[str, Any]]:
    if not condition:
        return data

    column, operator, value = parse_condition(condition)
    filtered_data = []

    for row in data:
        row_value = row[column]
        if operator == "=":
            if str(row_value) == value:
                filtered_data.append(row)
        elif operator == ">":
            if float(row_value) > float(value):
                filtered_data.append(row)
        elif operator == "<":
            if float(row_value) < float(value):
                filtered_data.append(row)
        elif operator == ">=":
            if float(row_value) >= float(value):
                filtered_data.append(row)
        elif operator == "<=":
            if float(row_value) <= float(value):
                filtered_data.append(row)

    return filtered_data
