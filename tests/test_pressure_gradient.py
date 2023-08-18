from .utils import convert_units

# test cases
cases = [
    {"from": "psi/ft", "amount": 1, "to": "kPa/m", "expected": 22.6206},
    {"from": "kPa/m", "amount": 1, "to": "psi/ft", "expected": 0.0442075},
]


def test():
    convert_units(cases)
