from .utils import convert_units

# test cases
cases = [
    {"from": "Mscf", "amount": 5.5, "to": "m3", "expected": 155.8073654390935},
    {"from": "Mscf", "amount": 5.5, "to": "ft3", "expected": 0.0055},
    {"from": "bbl", "amount": 1, "to": "m3", "expected": 0.1586402266},
    {"from": "m3", "amount": 1, "to": "bbl", "expected": 6.30357142857}
]


def test():
    convert_units(cases)
