from .utils import convert_units

# test cases
cases = [
    {"from": "deg", "amount": 1, "to": "rad", "expected": 0.0174533},
    {"from": "rad", "amount": 1, "to": "deg", "expected": 57.2958},
    {"from": "rad", "amount": 1, "to": "grad", "expected": 63.662},
    {"from": "grad", "amount": 1, "to": "rad", "expected": 0.015707963},
]


def test():
    convert_units(cases)
