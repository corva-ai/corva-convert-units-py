from .utils import convert_units

cases = [
    {"from": "v/v", "amount": 1, "to": "pu", "expected": 100},
    {"from": "pu", "amount": 50, "to": "v/v", "expected": 0.5},
    {"from": "v/v", "amount": 1, "to": "v/v", "expected": 1}
]


def test():
    convert_units(cases)
