from .utils import convert_units

# test cases
cases = [
    {"from": "C", "amount": 0, "to": "F", "expected": 32},
    {"from": "F", "amount": 32, "to": "C", "expected": 0},
]


def test():
    convert_units(cases)
