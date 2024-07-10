from .utils import convert_units

cases = [
    {"from": "V", "amount": 1, "to": "nV", "expected": 1000000000},
    {"from": "nV", "amount": 1, "to": "V", "expected": 0.000000001},
]


def test():
    convert_units(cases)
