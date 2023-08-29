from .utils import convert_units

# test cases
cases = [
    {"from": "l/m3", "amount": 1, "to": "gal/Mgal", "expected": 1.},
    {"from": "gal/Mgal", "amount": 1, "to": "l/m3", "expected": 1.},
]


def test():
    convert_units(cases)
