from .utils import convert_units

# test cases
cases = [
    {"from": "us/m", "amount": 1, "to": "us/ft", "expected": 0.3048},
    {"from": "us/ft", "amount": 1, "to": "us/m", "expected": 3.28084}
]


def test():
    convert_units(cases)
