from .utils import convert_units

# test cases
cases = [
    {"from": "psi", "amount": 1, "to": "kPa", "expected": 6.89476},
    {"from": "kPa", "amount": 1, "to": "psi", "expected": 0.14503768},
    {"from": "Pa", "amount": 1, "to": "bar", "expected": 1e-5},
    {"from": "hsf", "amount": 1, "to": "Pa", "expected": 0.4788027778},
    {"from": "Pa", "amount": 1, "to": "hsf", "expected": 2.0885426},
    {"from": "ksi", "amount": 1, "to": "kPa", "expected": 6894.76},
    {"from": "kPa", "amount": 1, "to": "ksi", "expected": 0.00014503768078},
]


def test():
    convert_units(cases)
