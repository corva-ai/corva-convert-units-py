from .utils import convert_units

# test cases
cases = [
    {"from": "C", "amount": 0, "to": "F", "expected": 32},
    {"from": "F", "amount": 32, "to": "C", "expected": 0},
    {"from": "K", "amount": 0, "to": "C", "expected": -273.15},
    {"from": "C", "amount": 0, "to": "K", "expected": 273.15},
    {"from": "F", "amount": 32, "to": "K", "expected": 273.15},
    {"from": "K", "amount": 0, "to": "F", "expected": -459.67},
]


def test():
    convert_units(cases)
