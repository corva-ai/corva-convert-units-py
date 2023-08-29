from .utils import convert_units

# test cases
cases = [
    {"from": "hp", "amount": 1, "to": "watt", "expected": 745.7152996},
    {"from": "watt", "amount": 1, "to": "hp", "expected": 0.0013409943453},
    {"from": "hp", "amount": 1, "to": "mhp", "expected": 1.013890297},
]


def test():
    convert_units(cases)
