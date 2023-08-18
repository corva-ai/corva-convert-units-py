from .utils import convert_units

# test cases
cases = [
    {"from": "m2", "amount": 1, "to": "ft2", "expected": 10.7639},
    {"from": "ft2", "amount": 1, "to": "m2", "expected": 0.0929031299},
]


def test():
    convert_units(cases)
