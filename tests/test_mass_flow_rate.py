from .utils import convert_units

# test cases
cases = [
    {"from": "lb/min", "amount": 1, "to": "kg/min", "expected": 0.453592},
    {"from": "kg/min", "amount": 1, "to": "lb/min", "expected": 2.2046244201},
    {"from": "g/s", "amount": 1, "to": "lb/s", "expected": 0.00220462442},
    {"from": "lb/s", "amount": 1, "to": "g/s", "expected": 453.592},
]


def test():
    convert_units(cases)
