from typing import List, Dict, Any, Union


def aggregate_data(
    data: List[Dict[str, Any]], aggregate: str
) -> Dict[str, Union[float, str]]:      
    if not aggregate:
        return {}

    column, operation = aggregate.split("=")
    numeric_values = [float(row[column]) for row in data]

    if operation == "avg":
        result = sum(numeric_values) / len(numeric_values)
    elif operation == "min":
        result = min(numeric_values)
    elif operation == "max":
        result = max(numeric_values)
    else:
        raise ValueError(f"Unknown aggregation operation: {operation}")

    return {"column": column, operation: result}