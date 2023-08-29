from .utils import convert_units

# test cases
cases = [
    {"from": "lb", "amount": 1, "to": "kg", "expected": 0.453592},
    {"from": "kg", "amount": 1, "to": "lb", "expected": 2.20462442018},
]


def test():
    convert_units(cases)
