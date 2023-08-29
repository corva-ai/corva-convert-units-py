from .utils import convert_units

# test cases
cases = [
    {"from": "lb-ft", "amount": 1, "to": "kg-m", "expected": 1.48816},
    {"from": "kg-m", "amount": 1, "to": "lb-ft", "expected": 0.6719707558327062},
]


def test():
    convert_units(cases)
