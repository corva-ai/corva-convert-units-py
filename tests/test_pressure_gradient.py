from .utils import convert_units

# test cases
cases = [
    {"from": "psi/ft", "amount": 1, "to": "kPa/m", "expected": 22.6206},
    {"from": "kPa/m", "amount": 1, "to": "psi/ft", "expected": 0.0442075},
    {"from": "psi/ft", "amount": 1, "to": "Pa/m", "expected": 22620.59353334},
    {"from": "Pa/m", "amount": 1, "to": "psi/ft", "expected": 4.42075e-5},
]


def test():
    convert_units(cases)
