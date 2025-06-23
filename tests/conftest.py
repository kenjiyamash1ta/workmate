import pytest


@pytest.fixture
def sample_data():
    return [
        {"name": "iphone", "price": "999", "rating": "4.9"},
        {"name": "galaxy", "price": "1199", "rating": "4.8"},
        {"name": "redmi", "price": "199", "rating": "4.6"},
    ]