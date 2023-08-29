from .utils import convert_units

# test cases
cases = [
    {"from": "year", "amount": 1, "to": "day", "expected": 365.25},
    {"from": "s", "amount": 1, "to": "mu", "expected": 1e6},
]


def test():
    convert_units(cases)
