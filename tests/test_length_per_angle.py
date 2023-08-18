from .utils import convert_units

# test cases
cases = [
    {"from": "in/rev", "amount": 1, "to": "mm/rev", "expected": 25.4},
    {"from": "mm/rev", "amount": 1, "to": "in/rev", "expected": 0.0393701},
]


def test():
    convert_units(cases)
