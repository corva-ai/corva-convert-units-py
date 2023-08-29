from .utils import convert_units

# test cases
cases = [
    {"from": "i-psi", "amount": 1, "to": "i-pa", "expected": 0.00014503774},
    {"from": "i-pa", "amount": 1, "to": "i-psi", "expected": 6894.757},
]


def test():
    convert_units(cases)
